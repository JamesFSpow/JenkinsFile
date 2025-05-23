pipeline{
    agent any

    stages{

        stage('Build')
        {
            steps
            {
                echo 'Stage 1: Build'
                echo 'Tool: Maven - Used to compile and package the code.'
            }
        }

        stage('Unit and Integration Tests')
        {
            steps
            {
                echo 'Stage 2: Unit and Integration Tests'
                echo 'Tools: JUnit (for unit tests), TestNG (for integration tests)'
            }
        }

        stage('Code Analysis')
        {
            steps
            {
                echo 'Stage 3: Code Analysis'
                echo 'Tool: SonarQube - Used for static code analysis'
            }
        }

        stage('Security Scan')
        {
            steps
            {
                echo 'Stage 4: Security Scan'
                echo 'Tool: OWASP - To scan dependencies for known vulnerabilites'
            }
        }

        stage('Deploy to Staging')
        {
            echo 'Stage 5: Deploy to Staging'
            echo 'Tool: AWS CLI - To deploy the application to a staging environment'
        }

        stage('Integration Tests on Staging')
        {
            echo 'Stage 6: Integration Tests on Staging'
            echo 'Tool: Selenium - Used for end-to-end integration on the staging environment'
        }

        stage('Deploy to Production')
        {
            echo 'Stage 7: Deploy to Production'
            echo 'Tool: AWS EC2 - Used to deploy application to a production environmentsS'
        }
    }


}