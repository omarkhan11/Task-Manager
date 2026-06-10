pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm 
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building environment and installing Python dependencies...'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running test suite with pytest...'
                sh 'python3 -m pytest test_app.py -v' 
            }
        }
        
        stage('Simulate Deploy') {
            steps {
                echo 'All tests passed! Deploying application.'
            }
        }
    }
}
