pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-u root' // run as root to install packages if needed
        }
    }
    stages {
        stage('Setup Python') {
            steps {
                sh 'python --version'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
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
