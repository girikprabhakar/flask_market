pipeline{
    agent any
    stages
    {
        stage("Checkout Code")
        {
            steps
            {
                echo "Checkout Code"
            }
        }
        stage("Docker Compose up")
        {
            steps
            {
                echo "Docker Compose up"
                script
                {
                    sh 'docker-compose up -d'
                }
            }
            
        }
        stage("Tests")
        {
            steps
            {
                echo "Executing Tests"
            }
        }
        stage("Pushing Web Image")
        {
            steps
            {
                script 
                {
                    sh 'docker image tag flask_market:latest 8285/flask_market:latest'
                    withCredentials([string(credentialsId: 'dockerhub', variable: 'dockerhub')]) 
                    {                        
                        sh 'docker login -u 8285 -p ${dockerhub}'
                        sh 'docker push 8285/flask_market'
                    }
                }
            }
        }
        stage("Clean Up")
        {
            steps
            {
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "./cleanup.sh"
            }
        }
    }
    
}
