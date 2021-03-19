pipeline{
    agent any

    stages{
        stage('Compilation stage'){
            steps{
                bat 'python src/Alphabet.py'
            }

        }
        stage('Testing Stage'){
              steps{
                bat 'python src/test_Alphabet.py'
            }
        }
        stage('Output Display'){
              steps{
               bat 'python src/output.py'
            }
        }
    }
}
