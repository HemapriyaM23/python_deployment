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
