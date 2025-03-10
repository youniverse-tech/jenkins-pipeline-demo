pipeline {
    agent any 
    stages {
        stage('Clone Repository') { // Renamed to avoid duplicate name
            steps {
                git branch: 'main', url: 'https://github.com/youniverse-tech/jenkins-pipeline-demo.git'
            }
        }
        stage('Hello') {
            steps {
                echo 'Hello, Jenkins!'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building the project..."'
            }
        }
    }
}
