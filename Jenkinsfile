pipeline {
    agent any 
    stages {
        stage('Checkout SCM') {
            steps {
                git 'https://github.com/youniverse-tech/jenkins-pipeline-demo'
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
