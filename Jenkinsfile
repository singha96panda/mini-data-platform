pipeline {
    agent any

    environment {
        PYSPARK_PYTHON = 'python'
        PYSPARK_DRIVER_PYTHON = 'python'
    }

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }
    }
}
