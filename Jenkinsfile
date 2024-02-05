pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from your version control system (e.g., Git)
                script {
                    git 'https://github.com/athlour/webapp.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies using a virtual environment
                script {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run your unit tests
                script {
                    sh 'source venv/bin/activate && pytest'
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                // Build and deploy your Flask application
                script {
                    sh 'source venv/bin/activate && python your_flask_app.py &'
                    // Add additional deployment steps as needed
                }
            }
        }
    }

    post {
        always {
            // Clean up after the build
            script {
                sh 'killall -9 python'
                sh 'rm -rf venv'
            }
        }
    }
}
