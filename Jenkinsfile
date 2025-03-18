pipeline {
    agent any
    environment {
        PYTHONUTF8 = '1'  // Set UTF-8 encoding to avoid UnicodeEncodeError
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', credentialsId: 'bbd4faff-f5c7-47df-9351-76ab8d014fca', url: 'https://github.com/youniverse-tech/jenkins-pipeline-demo.git'
            }
        }

        stage('Check Python Path') {
            steps {
                bat 'where python'
                bat 'python --version'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip && venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Python projects usually do not have a build step. Skipping...'
            }
        }

        stage('Test') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
            }
        }

        stage('Post-Build Log Filtering') {
            steps {
                script {
                    echo '🚀 Running log filtering...'
                    def result = bat(script: 'venv\\Scripts\\python.exe scripts/filter_logs.py', returnStatus: true)
                    if (result != 0) {
                        error '❌ Log filtering script failed!'
                    } else {
                        echo '✅ Filtered logs saved successfully in filtered_logs.txt'
                    }
                }
            }
        }

        stage('Post-Build AI Anomaly Detection') {
            steps {
                script {
                    echo '🤖 Running AI-based anomaly detection...'
                    def result = bat(script: 'venv\\Scripts\\python.exe scripts/filter_logs.py', returnStatus: true)
                    if (result != 0) {
                        error '❌ AI anomaly detection failed!'
                    } else {
                        echo '⚠️ Anomalies detected and saved in anomalies.txt'
                    }
                }
            }
        }
    }
}
