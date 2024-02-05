pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    bat 'git clone https://github.com/athlour/webapp.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    bat 'python -m venv venv'
                    bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat '.\\venv\\Scripts\\activate && pytest test_app.py'
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                script {
                    bat '.\\venv\\Scripts\\activate && python app.py'
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up after the build, if needed
            }
        }
    }
}
