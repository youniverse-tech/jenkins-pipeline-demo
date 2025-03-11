pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/youniverse-tech/jenkins-pipeline-demo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'   // Create a virtual environment
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'  // Install dependencies
            }
        }

        stage('Build') {
            steps {
                echo 'Python projects usually do not have a build step. Skipping...'
            }
        }

        stage('Test') {
            steps {
                bat 'venv\\Scripts\\activate && pytest tests/'  // Run tests with pytest
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
            }
        }
        
        stage('Checkout Code') {
            steps {
                git credentialsId: 'bbd4faff-f5c7-47df-9351-76ab8d014fca', 
                url: 'https://github.com/youniverse-tech/jenkins-pipeline-demo.git', 
                branch: 'main'
             }
        }

    }
}
