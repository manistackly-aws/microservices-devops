
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate Repository') {
            steps {
                sh '''
                    test -f user-service/app.py
                    test -f product-service/app.py
                    test -f order-service/app.py
                '''
            }
        }

        stage('Python Syntax Check') {
            steps {
                sh '''
                    python3 -m py_compile user-service/app.py
                    python3 -m py_compile product-service/app.py
                    python3 -m py_compile order-service/app.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Build Successful!'
        }

        failure {
            echo 'Build Failed!'
        }
    }
}
