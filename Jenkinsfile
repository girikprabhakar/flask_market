pipeline
{
    agent
    {
        label "docker-build-server"
    }
    environment
        {
            IMAGE = "flask_market"
            IMAGE_NEW_NAME = "8285/flask_market"
            TAG = "latest"
            USERNAME = "8285"
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
        stage("Publishing Docker Image")
        {
            when
            {
                anyOf 
                {
                    branch "release*"
                    branch "main"
                    branch "master"
                }
            }
            steps
            {
                script 
                {
                    sh 'docker image tag $IMAGE:$TAG $IMAGE_NEW_NAME:$TAG'
                    withCredentials([string(credentialsId: 'dockerhub', variable: 'dockerhub')]) 
                    {                        
                        sh 'docker login -u $USERNAME -p ${dockerhub}'
                        sh 'docker push $IMAGE_NEW_NAME'
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
