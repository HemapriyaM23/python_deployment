```yaml
name: Deploy to Server

on:
  push:
    branches:
      - main  # Trigger the workflow on push to the main branch

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Configure AWS Credentials
      uses: aws-actions/configure-aws-credentials@v2
      with:
        role-to-assume: arn:aws:iam::123456789012:role/YourOIDCRole
        aws-region: us-west-2

    - name: Execute Deployment Commands
      run: |
        instance_id="i-xxxxxxxxxxxxxxxxx"
        aws ssm start-session --target $instance_id --document-name "AWS-StartNonInteractiveCommand" --parameters '{"commands":["cd /home/nginx/sit-nexus","git pull origin sit","stat -c %y .git/FETCH_HEAD","source files/virtual_envs/NexusEnv/bin/activate","chmod +x files/virtual_envs/NexusEnv/bin/activate","source files/virtual_envs/NexusEnv/bin/activate","python manage.py collectstatic","sudo systemctl restart gunicorn-sit_nexus.service","sudo systemctl status gunicorn-sit_nexus.service","sudo nginx -t","sudo nginx -s reload","sudo systemctl status nginx.service"]}' --region us-west-2

```
