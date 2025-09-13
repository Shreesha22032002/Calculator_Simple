pipeline {
    agent any

    stages {
        stage('Run Calculator / Tests') {
            steps {
                // Run main.py; GUI is skipped in Jenkins, tests run automatically
                sh 'python3 main.py'
            }
        }

        stage('Archive Artifacts') {
            steps {
                // Archive all Python files and log output if needed
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
            }
        }
    }
}
