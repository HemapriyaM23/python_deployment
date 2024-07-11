```yaml
name: Nexus Deployment

on:
  push:
    branches:
      - sit

jobs:
  deploy:
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

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

    - name: Pull latest changes
      run: |
        git reset --hard
        git pull origin sit

    - name: Activate virtual environment
      run: source files/virtual_envs/.NexusEnv/bin/activate

    - name: Collect static files
      run: |
        cd /home/nginx/sit-nexus
        python manage.py collectstatic --noinput

    - name: Restart Gunicorn service
      run: sudo systemctl restart gunicorn-sit_nexus.service

    - name: Reload Nginx
      run: sudo nginx -s reload

    - name: Send SSM command
      id: send_command
      run: |
        COMMAND_ID=$(aws ssm send-command \
          --document-name "AWS-RunShellScript" \
          --targets "Key=instanceids,Values=YOUR_EC2_INSTANCE_ID" \
          --parameters 'commands=["cd /home/nginx/sit-nexus", "source files/virtual_envs/.NexusEnv/bin/activate", "python manage.py migrate", "python manage.py collectstatic --noinput", "sudo systemctl restart gunicorn-sit_nexus.service", "sudo nginx -s reload"]' \
          --region eu-west-1 \
          --query "Command.CommandId" \
          --output text)
        echo "COMMAND_ID=$COMMAND_ID" >> $GITHUB_ENV

    - name: Wait for command to complete
      run: |
        sleep 10  # Adjust the sleep time as necessary

    - name: Get command output
      id: get_output
      run: |
        OUTPUT=$(aws ssm get-command-invocation \
          --command-id ${{ env.COMMAND_ID }} \
          --instance-id YOUR_EC2_INSTANCE_ID \
          --region eu-west-1 \
          --query "StandardOutputContent" \
          --output text)
        echo "$OUTPUT"
        echo "OUTPUT=$OUTPUT" >> $GITHUB_ENV

    - name: Check for errors
      run: |
        if [ -z "${{ env.OUTPUT }}" ]; then
          echo "Error: No output received from SSM command"
          exit 1
        fi

```
