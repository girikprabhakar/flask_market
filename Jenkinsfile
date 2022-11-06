pipeline{
    agent
    {
        label "docker-build server"
    }
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
                    sh 'docker image tag 8285/flask_market:latest flask_market:latest '
                    withCredentials([string(credentialsId: 'dockerhub', variable: 'dockerhub')]) 
                    {                        
                        sh 'docker login -u 8285 -p ${dockerhub}'
                        sh 'docker push 8285/flask_market'
                    }
                }
            }
        }
    }
    
}