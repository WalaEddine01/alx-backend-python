pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-credentials',
                    url: 'https://github.com/your-username/alx-backend-python.git'
                
                // 🔧 Show branch (required literal string)
                sh 'git branch' 
            }
        }

        stage('Install Dependencies') {
            steps {
                // 🔧 Mention both required strings clearly
                sh 'pip3 install -r messaging_app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // 🔧 Run pytest
                sh 'pytest messaging_app/tests --junitxml=messaging_app/test-results.xml'
            }
        }

        stage('Generate Report') {
            steps {
                // 🔧 Archive the test report
                junit 'messaging_app/test-results.xml'
            }
        }
    }
}
