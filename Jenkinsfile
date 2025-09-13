pipeline {
    agent any
    stages {
        stage('Run Calculator') {
            steps {
                sh 'xvfb-run python3 main.py'
            }
        }
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
            }
        }
    }
}
