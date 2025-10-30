pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo "Pulling code from GitHub"
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image"
                sh 'docker build -t devops-app .'
            }
        }

        stage('Run Container') {
            steps {
                echo "Running Docker Container"
                sh 'docker run -d -p 5000:5000 --name devops-container devops-app'
            }
        }
    }

    post {
        always {
            echo "Cleaning up"
            sh 'docker stop devops-container || true'
            sh 'docker rm devops-container || true'
        }
    }
}
