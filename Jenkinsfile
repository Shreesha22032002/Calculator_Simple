pipeline {
    agent any
    stages {
        stage('Install Python') {
            steps {
                sh '''
                apt-get update && apt-get install -y python3 python3-venv python3-pip
                '''
            }
        }
        stage('Setup Python') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
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
