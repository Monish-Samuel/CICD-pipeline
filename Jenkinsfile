pipeline{
    agent any

    stages{
        stage('Compilation stage'){
            steps{
                bat 'python Alphabet.py'
            }

        }
        stage('Testing Stage'){
              steps{
                bat 'python test_Alphabet.py'
            }
        }
        stage('Deployment Stage'){
              steps{
               bat 'python output.py'
            }
        }
    }
}
