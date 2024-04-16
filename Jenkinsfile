pipeline { 
        environment { 
                registry = "harunisiaho/getip" 
                registryCredential = 'dockerhub_id'
                dockerImage = '' 
        }

        agent kubernetes {
            yaml 'kaniko-pod.yaml'
        } 

        stages { 
                stage('Cloning our Git') { 
                        steps { 
                                git branch: 'main', url: 'https://github.com/harunisiaho/getip.git' 
                        }
                } 

                stage('Building our image') { 
                        steps { 
                                script { 
                                        dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                                }
                        } 
                }

                stage('Deploy our image') { 
                        steps { 
                                script { 
                                        docker.withRegistry( '', registryCredential ) { 
                                                dockerImage.push() 
                                        }
                                } 
                        }
                } 
                stage('Cleaning up') { 
                        steps { 
                                sh "docker rmi $registry:$BUILD_NUMBER" 
                        }
                } 
        }
}