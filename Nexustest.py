Here’s the **Confluence-formatted guide** for signing up to a Terraform Cloud account:

---

## **Steps to Sign Up for a Terraform Cloud Account**

### **1. Visit the Signup Page**
- Go to [Terraform Cloud Signup Page](https://app.terraform.io/signup/account).

### **2. Create an Account**
- Fill in the following details:
  - **Username**
  - **Email Address**
  - **Password**
- Agree to the terms and conditions, then click on **"Create Account"**.

### **3. Confirm Your Email**
- Check your email inbox for a confirmation email from Terraform Cloud.
- Click on the confirmation link to verify your email address.

### **4. Create an Organization**
- After verifying your email, you’ll be prompted to create an organization.
- Provide:
  - **Organization Name**: A unique name for your organization.
  - **Organization Email**: You can use the same email as your account.
- Click on **"Create Organization"**.

### **5. Start Using Terraform Cloud**
- Once your organization is set up, you can:
  - Create workspaces.
  - Manage infrastructure as code.

---

### **Notes**
- Terraform Cloud is free for up to 5 users.
- For additional features or team scaling, explore paid plans under the "Settings" tab.

Sources
To ensure that the output of the `aws ssm send-command` is captured and displayed in the GitHub Actions logs, you need to retrieve the command invocation details after sending the command. Here’s how to do it:

### Detailed Steps to Capture and Display SSM Command Output in GitHub Actions

#### **1. Update the IAM Policy**

Ensure the IAM role used by GitHub Actions has the required permissions. Here is an example policy that grants the necessary permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ssm:SendCommand",
        "ssm:ListCommands",
        "ssm:ListCommandInvocations",
        "ssm:GetCommandInvocation"
      ],
      "Resource": [
        "arn:aws:ssm:eu-west-1:YOUR_AWS_ACCOUNT_ID:document/AWS-RunShellScript",
        "arn:aws:ec2:eu-west-1:YOUR_AWS_ACCOUNT_ID:instance/YOUR_EC2_INSTANCE_ID"
      ]
    }
  ]
}
```

Replace `YOUR_AWS_ACCOUNT_ID` and `YOUR_EC2_INSTANCE_ID` with your actual AWS account ID and EC2 instance ID.

#### **2. Attach the Updated Policy to the IAM Role**

1. **Navigate to IAM Console**: Go to the IAM console in AWS.
2. **Select Roles**: Choose the role used by GitHub Actions.
3. **Attach Policy**: Attach the updated policy to the role.

#### **3. Verify the Trust Relationship**

Ensure the trust relationship of the IAM role allows GitHub Actions to assume the role. Here is an example trust policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::YOUR_AWS_ACCOUNT_ID:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:sub": "repo:YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME:ref:refs/heads/main"
        }
      }
    }
  ]
}
```

Replace `YOUR_AWS_ACCOUNT_ID`, `YOUR_GITHUB_USERNAME`, and `YOUR_REPOSITORY_NAME` with your actual AWS account ID, GitHub username, and repository name.

#### **4. Update GitHub Actions Workflow**

Ensure your GitHub Actions workflow is correctly configured to use the updated IAM role and capture the output of the SSM command. Here is the updated workflow script:

```yaml
name: Print Statement Pipeline

on:
  push:
    branches:
      - main
      - develop
      - feature/*  # This will match any branch that starts with 'feature/'

jobs:
  print-statement:
    runs-on: ubuntu-latest

    permissions:
      id-token: write
      contents: read

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v2
      with:
        role-to-assume: arn:aws:iam::YOUR_AWS_ACCOUNT_ID:role/YOUR_ROLE_NAME
        aws-region: eu-west-1  # Ireland region

    - name: Send SSM command
      id: send_command
      run: |
        COMMAND_ID=$(aws ssm send-command \
          --document-name "AWS-RunShellScript" \
          --targets "Key=instanceids,Values=YOUR_EC2_INSTANCE_ID" \
          --parameters 'commands=["echo Hello, this is a print statement from the CI/CD pipeline!"]' \
          --region eu-west-1 \
          --query "Command.CommandId" \
          --output text)
        echo "COMMAND_ID=$COMMAND_ID" >> $GITHUB_ENV

    - name: Wait for command to complete
      run: |
        sleep 10  # Adjust the sleep time as necessary

    - name: Get command output
      run: |
        aws ssm get-command-invocation \
          --command-id ${{ env.COMMAND_ID }} \
          --instance-id YOUR_EC2_INSTANCE_ID \
          --region eu-west-1 \
          --query "StandardOutputContent" \
          --output text
```

### Explanation:
- **Send SSM command**: Sends the SSM command and captures the `CommandId`.
- **Wait for command to complete**: Waits for a few seconds to allow the command to complete execution.
- **Get command output**: Retrieves the output of the command using the `get-command-invocation` command.

### Checking the Output in GitHub Actions Logs

1. **View Workflow Run**: Go to your GitHub repository and click on the **Actions** tab.
2. **Select Workflow Run**: Find and select the workflow run that executed the print statement.
3. **View Logs**: Click on the job and then the specific steps to view the logs. The logs will show the output of the `aws ssm send-command` and `get-command-invocation` executions, including any print statements.

By following these steps, you can resolve the access denied error and ensure that the GitHub Actions workflow can successfully execute commands on EC2 instances using AWS SSM, and capture and display the output in the GitHub Actions logs.

Sources
[1] image.jpg https://pplx-res.cloudinary.com/image/upload/v1720519860/user_uploads/dtdmjrxcn/image.jpg
[2] Setting up Run Command - AWS Systems Manager https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command-setting-up.html
[3] Configuring OpenID Connect in Amazon Web Services - GitHub Docs https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services
[4] get-command-invocation — AWS CLI 1.33.19 Command Reference https://docs.aws.amazon.com/cli/latest/reference/ssm/get-command-invocation.html
[5] Marketplace Actions AWS SSM Send-Command - GitHub https://github.com/marketplace/actions/aws-ssm-send-command
[6] AWS Systems Manager identity-based policy examples https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_id-based-policy-examples.html
[7] Configure AWS credential environment variables for use in ... - GitHub https://github.com/aws-actions/configure-aws-credentials
[8] GetCommandInvocation - AWS Systems Manager https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetCommandInvocation.html
[9] How to pass the output of a bash command to Github Action parameter https://stackoverflow.com/questions/61256824/how-to-pass-the-output-of-a-bash-command-to-github-action-parameter
[10] Fetch command output of command run using ssm #8787 - GitHub https://github.com/cloud-custodian/cloud-custodian/issues/8787
[11] Github runners ssh to ec2 : r/aws - Reddit https://www.reddit.com/r/aws/comments/17fzuj4/github_runners_ssh_to_ec2/
[12] Marketplace Actions AWS SSM Send-Command Action - GitHub https://github.com/marketplace/actions/aws-ssm-send-command-action
### Checking the Output of the CI/CD Pipeline

To verify the output of the CI/CD pipeline that executes a print statement through AWS SSM, follow these steps:

#### **1. Use AWS Systems Manager (SSM) Console**
- **Navigate to SSM Console**: Go to the AWS Management Console and open the Systems Manager console.
- **View Command History**: In the left navigation pane, choose **Run Command** and then **Command history**.
- **Select Command**: Find and select the command that was executed by your GitHub Actions workflow.
- **View Output**: Click on the command ID to see the details, including the output of the executed script. The output will show the print statement executed on the EC2 instance.

#### **2. Use AWS CLI to Retrieve Command Output**
- **Install AWS CLI**: Ensure you have AWS CLI installed and configured with the necessary permissions.
- **Retrieve Command Output**: Use the following command to retrieve the output of the executed command:
  ```sh
  aws ssm get-command-invocation \
    --command-id "COMMAND_ID" \
    --instance-id "YOUR_EC2_INSTANCE_ID"
  ```
  Replace `COMMAND_ID` with the actual command ID from the SSM console and `YOUR_EC2_INSTANCE_ID` with your EC2 instance ID. The output will include the result of the print statement.

#### **3. Use GitHub Actions Logs**
- **View Workflow Run**: Go to your GitHub repository and click on the **Actions** tab.
- **Select Workflow Run**: Find and select the workflow run that executed the print statement.
- **View Logs**: Click on the job and then the specific step to view the logs. The logs will show the output of the `aws ssm send-command` execution, including any print statements.

### Example GitHub Actions Workflow Script

Here is the GitHub Actions workflow script that logs in through AWS SSM client and executes a print statement:

```yaml
name: Print Statement Pipeline

on:
  push:
    branches:
      - main

jobs:
  print-statement:
    runs-on: ubuntu-latest

    permissions:
      id-token: write
      contents: read

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v2
      with:
        role-to-assume: arn:aws:iam::YOUR_AWS_ACCOUNT_ID:role/YOUR_ROLE_NAME
        aws-region: YOUR_AWS_REGION

    - name: Print a statement through SSM
      run: |
        aws ssm send-command \
          --document-name "AWS-RunShellScript" \
          --targets "Key=instanceids,Values=YOUR_EC2_INSTANCE_ID" \
          --parameters 'commands=["echo Hello, this is a print statement from the CI/CD pipeline!"]' \
          --region YOUR_AWS_REGION
```

### Explanation:
- **Checkout code**: Uses the `actions/checkout` action to pull the latest code from the repository.
- **Configure AWS credentials**: Uses the `aws-actions/configure-aws-credentials` action to assume the IAM role using OIDC.
- **Print a statement through SSM**: Uses AWS SSM to send a command to the EC2 instance to execute a print statement.

By following these steps, you can verify the output of your CI/CD pipeline and ensure that the print statement is executed correctly on the EC2 instance.

Sources
[1] How to check output processing status and error message via log table https://userapps.support.sap.com/sap/support/knowledge/en/2446690
[2] How to store verification output message as a variable? - StudioX https://forum.uipath.com/t/how-to-store-verification-output-message-as-a-variable/392452
[3] inspect — Inspect live objects — Python 3.12.4 documentation https://docs.python.org/3/library/inspect.html
[4] Working with check output - IBM https://www.ibm.com/docs/en/zos/2.5.0?topic=zos-working-check-output
[5] Verifying output from a component under test - bUnit https://bunit.dev/docs/verification/index.html
[6] Inspect Module in Python - GeeksforGeeks https://www.geeksforgeeks.org/inspect-module-in-python/
[7] Checking if output of a command contains a certain string in a shell ... https://stackoverflow.com/questions/16931244/checking-if-output-of-a-command-contains-a-certain-string-in-a-shell-script
[8] Testing code where you don't know the output in advance https://stackoverflow.com/questions/15912650/testing-code-where-you-dont-know-the-output-in-advance
[9] What Is Quality Inspection? (With Examples and Methods) - Indeed https://ca.indeed.com/career-advice/career-development/what-is-quality-inspection
[10] Output Window - Visual Studio - Microsoft Learn https://learn.microsoft.com/en-us/visualstudio/ide/reference/output-window?view=vs-2022
[11] Verify output — verify_output - testthat https://testthat.r-lib.org/reference/verify_output.html
[12] Inspection Method - an overview | ScienceDirect Topics https://www.sciencedirect.com/topics/engineering/inspection-method
[13] How to see the output of yr code on notepad - Sololearn https://www.sololearn.com/en/Discuss/2430493/how-to-see-the-output-of-yr-code-on-notepad
[14] Three Ways to Test Output Validation - Think Like a Tester http://thethinkingtester.blogspot.com/2019/03/three-ways-to-test-output-validation.html
[15] INSPECT command - IBM https://www.ibm.com/docs/en/db2/11.5?topic=commands-inspect
