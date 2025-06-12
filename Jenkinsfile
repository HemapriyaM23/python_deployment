@Library('sfdi-devops-tools-infra') _

pipeline {
    agent any
    environment {
        
        snowflake_changeLogFile_COMETL_CONTROL__db = "Backend/data_alignment/snowflake/COMETL_CONTROL/changelog.sf.xml"
        
        snowflake_COMETL_CONTROL__db_url = "${getProperty("${env.BRANCH_NAME}_pfzalgn_snowflake_COMETL_CONTROL_db_url_apac_da")}"
        
        snowflake_credid = "${env.BRANCH_NAME}_pfzalgn_snowflake_credid_apac_da"
        
    }

    
    stages{


        stage ("Deploy to Snowflake Database - COMETL_CONTROL"){
            when {
                 expression { params.Deploy_to_Snowflake_COMETL_CONTROL == "Yes" }
            }
                steps{
                    script{
                        println "Deploying into COMETL_CONTROL ${env.BRANCH_NAME} environment"
                        snowflake_deploy(url: snowflake_COMETL_CONTROL__db_url, cred: snowflake_credid, changelog: snowflake_changeLogFile_COMETL_CONTROL__db, dry_run: dry_run) 
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
