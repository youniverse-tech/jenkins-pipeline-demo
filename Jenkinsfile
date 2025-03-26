pipeline {
    agent any

    environment {
        PYTHONUTF8 = '1'
        PYTHON_PATH = 'C:\\Users\\aaron\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
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
                bat '"%PYTHON_PATH%" --version'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                    if not exist venv (
                        "%PYTHON_PATH%" -m venv venv
                    )
                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                    venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Build') {
            steps {
                script {
                    echo '🔨 Running Build step...'
                    def result = bat(script: 'venv\\Scripts\\python.exe -m pip install -r requirements.txt', returnStatus: true)
                    if (result != 0) {
                        error '❌ Build step failed!'
                    } else {
                        echo '✅ Build completed successfully!'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying the application...'
            }
        }

        stage('Post-Build Log Filtering') {
            steps {
                script {
                    echo '🛠 Running log filtering...'
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
                    def result = bat(script: 'venv\\Scripts\\python.exe scripts/anomaly_detection.py', returnStatus: true)
                    if (result != 0) {
                        error '❌ AI anomaly detection failed!'
                    } else {
                        echo '⚠️ Anomalies detected and saved in anomalies.txt'
                    }
                }
            }
        }
    } // Closes 'stages' block

    post {
        success {
            bat """
            curl -X POST -H "Content-type: application/json" --data "{\\"text\\": \\"✅ Jenkins Build SUCCESS! 🚀 Check: ${BUILD_URL}\\"}" https://hooks.slack.com/services/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
            """
        }
        failure {
            bat """
            curl -X POST -H "Content-type: application/json" --data "{\\"text\\": \\"❌ Jenkins Build FAILED! 🔴 Check: ${BUILD_URL}\\"}" https://hooks.slack.com/services/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
            """
        }
    }
}
