pipeline {
    agent any
    options {
     buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub1')
    }
    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
                sh 'ls *'
            }
        }
        stage('Build Image') {
            steps {
                //Aquí debes poner tu repositorio de dockerhub
		sh 'docker build -t aobrero/dockerhubejenkins . '
            }
        }
        stage('DockerHUB Login') {
            steps {
                
                sh 'docker login --username aobrero --password administrador'                
                }
            }
        stage('Docker Push') {
            steps {
		//Aquí debes poner tu DockerHub
                sh 'docker push aobrero/dockerhubejenkins'
                }
            }
        }
    post {
		always {
			sh 'docker logout'
		}
	 }
    }

