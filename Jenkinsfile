pipeline{
    agent any

    stages{
        stage('enable all scripts to be executable'){
            steps{
                sh 'chmod +x ./script/*'
            }
        }
        stage('Get the enviroment ready') {
            steps{
                sh './script/before_installation.sh'
                sh './script/installation.sh'                        
            }
        }     
        stage('Run app') {
            steps{
                sh 'sudo systemctl restart flask.service'
            }
        }
    }
}    
    

