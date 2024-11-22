AWS Serverless Replication Terraform Module
This module provisions the necessary AWS resources to set up a serverless replication environment using ECS, IAM, CloudWatch, and other AWS services.
Features
	•	ECS Cluster: Creates an ECS cluster with Fargate support.
	•	IAM Roles and Policies: Configures execution roles and policies for ECS tasks.
	•	CloudWatch Log Groups: Manages log groups for monitoring task execution.
	•	Task Definitions: Defines ECS task configurations with required CPU, memory, and container settings.
	•	Parameter Store Integration: Supports secure storage of sensitive information using AWS Parameter Store.
Usage
Example
module "serverless_replication" {
  source = "git::ssh://git@github.com/your-repo/terraform-aws-sfdi-serverless-repl-module.git"

  cpu                          = 512
  memory                       = 1024
  org_name                     = "example-org"
  env_type                     = "dev"
  cwlg_retention_in_days       = "30"
  common_tags                  = { Project = "Replication", Environment = "Dev" }
  snowflake_secret_arn         = "arn:aws:secretsmanager:region:account-id:secret:snowflake"
  salesforce_secret_arn        = "arn:aws:secretsmanager:region:account-id:secret:salesforce"
  replication_type             = "full-load"
  aws_region                   = "us-west-2"
  ecr_image                    = "example-image"
  aws_sg_list                  = ["sg-12345678"]
  aws_subnet_list              = ["subnet-12345678", "subnet-87654321"]
  repl_prefix                  = "replication"
  org_parameter_store_name     = "/org/parameter-store"
  control_parameter_store_name = "/control/parameter-store"
}
Inputs
| Name                          | Description                                | Type            | Default | Required |
|-------------------------------|--------------------------------------------|-----------------|---------|----------|
| `cpu`                         | CPU units for the task                    | `number`        |         | Yes      |
| `memory`                      | Memory for the task in MiB                | `number`        |         | Yes      |
| `org_name`                    | Name of the Replication Org               | `string`        |         | Yes      |
| `env_type`                    | Name of the environment where we want to deploy | `string`    |         | Yes      |
| `cwlg_retention_in_days`      | Period for which logs to be retained      | `string`        |         | No       |
| `common_tags`                 | Tags for common resources                 | `map(string)`   | `{}`    | No       |
| `snowflake_secret_arn`        | Snowflake Secret ID                       | `string`        |         | Yes      |
| `salesforce_secret_arn`       | Salesforce Secret ID                      | `string`        |         | Yes      |
| `replication_type`            | Replication type                          | `string`        |         | Yes      |
| `aws_region`                  | AWS Region                                | `string`        |         | Yes      |
| `ecr_image`                   | ECR Image                                 | `string`        |         | Yes      |
| `aws_sg_list`                 | Security Group List                       | `list(string)`  |         | Yes      |
| `aws_subnet_list`             | Subnet IDs List                           | `list(string)`  |         | Yes      |
| `repl_prefix`                 | Replication Prefix                        | `string`        |         | No       |
| `org_parameter_store_name`    | Org Parameter Store                       | `string`        |         | Yes      |
| `control_parameter_store_name`| Control Parameter Store                   | `string`        |         | Yes      |
| `ecr_image_uri`               | ECR Image URI                             | `string`        |         | Yes      |
