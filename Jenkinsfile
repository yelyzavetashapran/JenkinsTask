pipeline {
  agent any
  stages {
    stage("Deploying and testing from release branch") {
      steps {
        withPythonEnv('python') {
          sh 'pip install -r requirements.txt'
          sh 'python ./apply_scripts.py'
          sh 'pytest ./tests/main.py'
        }
      }
    }
    
    stage ('Merging release and develop'){
			steps{
            withCredentials([sshUserPrivateKey(credentialsId: 'd6f99c76-3df6-4fd1-bc50-c1061d77a903', keyFileVariable: 'SSH_KEY')]) {
                sh 'git checkout main'
                sh 'git pull'
                sh 'git merge origin/dev'
                sh 'GIT_SSH_COMMAND="ssh -i $SSH_KEY" git push git@github.com:yelyzavetashapran/JenkinsTask.git'
            }
        }
	}
	}
}


