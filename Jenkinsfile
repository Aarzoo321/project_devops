pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Aarzoo321/project_devops.git'
            }
        }


        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("devops-app")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    echo "Stopping old container if running..."
                    sh 'docker stop devops-container || true'
                    sh 'docker rm devops-container || true'

                    echo "Starting new container..."
                    sh 'docker run -d -p 5001:5001 --name devops-container devops-app'
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully & container started on port 5001"
        }
        failure {
            echo "❌ Build failed. Please check logs."
        }
    }
}
