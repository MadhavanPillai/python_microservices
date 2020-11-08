pipeline{
    agent any
    stages{
        stage('clone repository'){
            steps{
            checkout scm
            echo 'cloned repository'
            }
        }
        stage('build & test'){
            steps{
                sh '''
                echo "starting docker-compose"
                docker-compose build
                docker-compose up -d
                python3 Tests.py
                echo "Tests completed successfully")
                '''
            }

        }
    }
}