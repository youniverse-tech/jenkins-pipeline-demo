pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/youniverse-tech/jenkins-pipeline-demo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Python projects usually do not have a build step. Skipping...'
            }
        }

        stage('Test') {
            steps {
                bat 'venv\\Scripts\\activate && pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
            }
        }
    }
}
