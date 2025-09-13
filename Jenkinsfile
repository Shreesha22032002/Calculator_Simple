pipeline {
    agent any
    stages {
        stage('Setup Python') {
            steps {
                sh 'python --version'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Calculator') {
            steps {
                sh './venv/bin/python main.py'
            }
        }
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
            }
        }
    }
}
