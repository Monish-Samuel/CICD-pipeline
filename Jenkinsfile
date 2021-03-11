pipeline{
    agent any

    stages{
        stage('Compile stage'){
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
               echo 'successfully deployed'
            }
        }
    }
}
