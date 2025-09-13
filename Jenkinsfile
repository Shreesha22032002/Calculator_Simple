pipeline {
    agent any

    stages {
        stage('Run Calculator / Tests') {
            steps {
                // Run main.py in Jenkins
                sh '''
                python3 main.py > result.log 2>&1 || true
                '''
            }
        }

        stage('Publish Test Results') {
            steps {
                // Convert unittest results to JUnit XML for Jenkins
                sh '''
                python3 -m pip install junit-xml
                python3 -c "
import unittest
from junit_xml import TestSuite, TestCase
import main

loader = unittest.TestLoader()
suite = loader.loadTestsFromTestCase(main.TestCalculator)
junit_suite = TestSuite('CalculatorTests', suite)
with open('junit_report.xml', 'w') as f:
    TestSuite.to_file(f, [junit_suite], prettyprint=True)
                "
                '''
                junit 'junit_report.xml'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
                archiveArtifacts artifacts: 'result.log', fingerprint: true
            }
        }
    }
}
