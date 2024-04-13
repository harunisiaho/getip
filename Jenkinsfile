pipeline {
    agent { docker { image 'python:3.12.1-slim-bullseye' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
