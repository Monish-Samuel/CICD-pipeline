pipeline {
    agent any

    stages {        
        stage('Compiling Stage'){
            steps{
                bat 'python src/Alphabet.py'
            }
        }
        stage('Testing Stage'){
            steps{
                bat 'python src/test_Alphabet.py'
            }
        }
        stage('Output'){
            steps{
                bat 'python src/output.py'
            }
        }
    }
}
