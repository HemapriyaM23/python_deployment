Here's a detailed guide on how to deploy AWS CloudFormation templates across multiple accounts and regions using AWS CloudFormation StackSets, complete with screenshots.

## Setting Up CloudFormation StackSets

### Step 1: Enable Trusted Access

1. **Sign in to the AWS Management Console** and open the AWS CloudFormation console.
2. **Navigate to StackSets** in the left-hand menu.
3. **Enable Trusted Access** between AWS CloudFormation and AWS Organizations if not already enabled.

Enable Trusted Access

### Step 2: Create the Necessary IAM Roles

1. **Create the Administration Role** in the administrator account:
   - Role Name: `AWSCloudFormationStackSetAdministrationRole`
   - Attach the `AWSCloudFormationStackSetAdministrationRolePolicy` managed policy.

2. **Create the Execution Role** in each target account:
   - Role Name: `AWSCloudFormationStackSetExecutionRole`
   - Attach the `AWSCloudFormationStackSetExecutionRolePolicy` managed policy.

Create IAM Roles

## Creating a StackSet

### Step 3: Choose a Template

1. **Open the CloudFormation Console** and select **StackSets** from the left-hand menu.
2. Click **Create StackSet**.

Create StackSet

3. On the **Choose a template** page:
   - Select **Template is ready**.
   - Choose **Upload a template file** or **Amazon S3 URL**.
   - Upload your CloudFormation template file.
   - Click **Next**.

Choose Template

### Step 4: Specify StackSet Details

1. Enter a **StackSet name**.
2. Specify any **parameters** required by your template.
3. Click **Next**.

Specify StackSet Details

### Step 5: Configure StackSet Options

1. Add any **tags** if needed.
2. Under **Permissions**, choose **Service-managed permissions**.
3. For **Execution configuration**, select **Active**.
4. Click **Next**.

Configure StackSet Options

### Step 6: Set Deployment Options

1. Under **Accounts**, choose **Deploy stacks in accounts**.
2. Enter the **account IDs** of your target accounts.
3. Under **Specify regions**, select the regions for deployment.
4. Set **Deployment options**:
   - Maximum concurrent accounts: e.g., Number 1
   - Failure tolerance: e.g., Number 0
5. For **Region concurrency**, choose **Sequential** or **Parallel**.
6. Click **Next**.

Set Deployment Options

### Step 7: Review and Submit

1. Review your choices.
2. Click **Submit** to create the StackSet.

Review and Submit

## Monitoring Deployment

### Step 8: Monitor StackSet Operations

1. On the **StackSet details page**, monitor the **Operations** tab for deployment progress.
2. Check the **Stack instances** tab to see the status of individual stacks in each account and region.

Monitor StackSet Operations

## Updating or Deleting the StackSet

### Step 9: Update or Delete

- To **update**: Use the **Edit** option on the StackSet details page.
- To **delete**: First remove all stack instances, then delete the StackSet.

Update or Delete StackSet

This guide provides a comprehensive walkthrough for deploying CloudFormation templates across multiple AWS accounts and regions using AWS CloudFormation StackSets.

Sources
[1] New: Use AWS CloudFormation StackSets for Multiple Accounts in ... https://aws.amazon.com/blogs/aws/new-use-aws-cloudformation-stacksets-for-multiple-accounts-in-an-aws-organization/
[2] Deploy to Multiple Accounts and Regions - Sumo Logic Docs https://help.sumologic.com/docs/observability/aws/deploy-use-aws-observability/deploy-with-aws-cloudformation/deploy-multiple-accounts-regions/
[3] You can now deploy CloudFormation Stacks concurrently ... - AWS https://aws.amazon.com/about-aws/whats-new/2021/04/deploy-cloudformation-stacks-concurrently-across-multiple-aws-regions-using-aws-cloudformation-stacksets/
[4] CloudFormation Global Resource deployment across multiple regions https://stackoverflow.com/questions/71161462/cloudformation-global-resource-deployment-across-multiple-regions
[5] Deploy CloudFormation Hooks to an Organization with service ... https://aws.amazon.com/blogs/devops/deploy-cloudformation-hooks-to-an-organization-with-service-managed-stacksets/
[6] Deploy CloudFormation stacks across AWS accounts using ... https://repost.aws/knowledge-center/codepipeline-deploy-cloudformation
[7] Adding multiple AWS accounts using CFT for protection - Rubrik https://docs.rubrik.com/en-us/saas/saas/adding_multiple_aws_accounts_using_cft_protection_2.html
[8] What is the proper way to deploy a multi-region CloudFormation ... https://stackoverflow.com/questions/53634750/what-is-the-proper-way-to-deploy-a-multi-region-cloudformation-stack-that-includ
[9] Deploy an AWS CloudFormation template https://octopus.com/docs/deployments/aws/cloudformation
[10] CloudFormation deploying cross-account resources : r/aws - Reddit https://www.reddit.com/r/aws/comments/10pqi16/cloudformation_deploying_crossaccount_resources/
[11] 91. Building a fault tolerant WordPress site – Lab 5 : Cloud Formation http://www.ebsguide.com/91-building-a-fault-tolerant-wordpress-site-lab-5-cloud-formation/
[12] AWS CloudFormation StackSets Tutorial - YouTube https://www.youtube.com/watch?v=KVDt4559cTs
[13] Deploying a virtual machine using AWS CloudFormation https://skofgar.ch/dev/2020/11/deploying-a-vm-using-aws-cloud-formation/
[14] Deploy Using AWS CloudFormation - New Relic https://newrelic.com/blog/how-to-relic/deploy-new-relic-infrastructure-using-aws-cloudformation
