pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }

        stage('Verify Repository') {
            steps {
                sh '''
                    echo "Checking repository structure"

                    test -f user-service/app.py
                    test -f user-service/requirements.txt

                    test -f product-service/app.py
                    test -f product-service/requirements.txt

                    test -f order-service/app.py
                    test -f order-service/requirements.txt

                    echo "Repository structure verified"
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    set -e

                    for service in user-service product-service order-service
                    do
                        echo "Installing dependencies for $service"

                        cd "$WORKSPACE/$service"

                        python3 -m venv .venv

                        .venv/bin/python -m pip install --upgrade pip

                        .venv/bin/python -m pip install -r requirements.txt

                        cd "$WORKSPACE"
                    done
                '''
            }
        }

        stage('Validate Python Code') {
            steps {
                sh '''
                    set -e

                    for service in user-service product-service order-service
                    do
                        echo "Validating $service"

                        python3 -m py_compile "$service/app.py"
                    done

                    echo "All Python files passed validation"
                '''
            }
        }

        stage('Build Summary') {
            steps {
                echo 'All three microservices passed pipeline validation.'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Microservices pipeline completed.'
        }

        failure {
            echo 'FAILURE: Please check Jenkins Console Output.'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
