pipeline {
    agent any
    stages {
        stage('Run Calculator') {
            steps {
                sh 'python3 main.py'
            }
        }
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
            }
        }
    }
}
