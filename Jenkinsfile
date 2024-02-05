pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from your version control system (e.g., Git)
                script {
                    bat 'git clone https://github.com/athlour/webapp.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies using a virtual environment
                script {
                    bat 'python -m venv venv'
                    bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run your unit tests
                script {
                    bat '.\\venv\\Scripts\\activate && pytest test_app.py'
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                // Build and deploy your Flask application
                script {

                    bat 'start /B .\\venv\\Scripts\\activate && python app.py'

                    // Add additional deployment steps as needed
                }
            }
        }
    }

    post {
        always {
            // Clean up after the build
            script {
                bat 'taskkill /F /IM python.exe'
                bat 'rmdir /s /q venv'
            }
        }
    }
}
