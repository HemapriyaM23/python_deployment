@Library('sfdi-devops-tools-infra') _

pipeline {
    agent any
    environment {
        
        snowflake_changeLogFile_COMETL_CONTROL__db = "Backend/data_alignment/snowflake/COMETL_CONTROL/changelog.sf.xml"
        
        snowflake_COMETL_CONTROL__db_url = "${getProperty("${env.BRANCH_NAME}_pfzalgn_snowflake_COMETL_CONTROL_db_url_apac_da")}"
        
        snowflake_credid = "${env.BRANCH_NAME}_pfzalgn_snowflake_credid_apac_da"
        
    }
    parameters {
        
        choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Snowflake Environment', name: 'Deploy_to_Snowflake_COMETL_CONTROL'
       
        choice choices: ['Yes', 'No'], description: 'Mention if You want to Dry Run', name: 'dry_run'
        
    }
    
    stages{


        stage ("Deploy to Snowflake Database"){
             when {
                 expression { params.Deploy_to_Snowflake_COMETL_CONTROL == "Yes" }
            }
                steps{
                    script{
                        
                       def liquibaseCommand = """
                        liquibase \
                              --url="jdbc:snowflake://emeadev01.eu-west-1.privatelink.snowflakecomputing.com/?user=CMMFRCRO@pfizer.com&privateKeyFile=/home/srvamr-sfaops/test_private_key/test.p8&privateKeyFilePwd=${prv_key_pwd}&warehouse=PFE_COMMON_WH_XS_01&db=COMETL_SFDC_X_REGION_DEV_DB&schema=COMETL_SFDC_PUBLISH" \
                              --changeLogFile=unused.xml \
                                execute-sql \
                              --sql="SELECT CURRENT_USER();" 
                    """
                    // Run the liquibase command
                    sh liquibaseCommand
                        }
                }
        }




    }
}
