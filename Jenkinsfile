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

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip

                    if [ -f user-service/requirements.txt ]; then
                        python3 -m pip install -r user-service/requirements.txt
                    fi

                    if [ -f product-service/requirements.txt ]; then
                        python3 -m pip install -r product-service/requirements.txt
                    fi

                    if [ -f order-service/requirements.txt ]; then
                        python3 -m pip install -r order-service/requirements.txt
                    fi
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
