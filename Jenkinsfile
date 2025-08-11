@Library('sfdi-devops-tools-infra') _

pipeline {
    agent any
    environment {
        snowflake_changeLogFile  = "snowflake/changelog.sf.xml"
        
        snowflake_db_url        = "${getProperty("${env.BRANCH_NAME}_snowflake_pvt_test")}"
        snowflake_credid         = "${env.BRANCH_NAME}_snowflake_credid_pvt"
    }

    parameters {
        choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Snowflake Environment', name: 'Deploy_to_Snowflake'
        choice choices: ['Yes', 'No'], description: 'Mention if You want to Dry Run', name: 'dry_run'
        choice choices: ['No', 'Yes'], description: 'If you want to send alerts', name: 'Email_Alert'
        string defaultValue: 'None', description: 'Provide the comma separated Email addresses.', name: 'Notify_to'
    }

    stages {
        stage("Approval for Prod") {
            when {
                expression { "${env.BRANCH_NAME}" == "main" }
            }
            steps {
                script {
                    email_approval()
                }
            }
        }


        stage("Deploy to Snowflake Database") {
            when {
                expression { params.Deploy_to_Snowflake == "Yes" }
            }
            steps {
                script {
                    println "Deploying into Snowflake ${env.BRANCH_NAME} environment"
                    snowflake_deploy(url: snowflake_db_url, cred: snowflake_credid, changelog: snowflake_changeLogFile, dry_run: dry_run)
                }
            }
        }

    }

    post {
        failure {
            notification_email(Email_Alert: Email_Alert, Notify_to: Notify_to) 
        }
        success {
            notification_email(Email_Alert: Email_Alert, Notify_to: Notify_to)
        }
    }
}
