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
                echo "starting docker compose"
                docker-compose build
                docker-compose up -d
                sh"python3 Tests.py"
            }
        stage('publish image'){
            steps{
                echo 'Going to push the images to G Container Registry'
            }
        }

        }
    }
}