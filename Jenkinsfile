pipeline {
  agent any
  stages {
    stage("Deploying and testing from release branch") {
      steps {
        withPythonEnv('python3') {
          sh 'pip install -r requirements.txt'
          sh 'python3 ./apply_scripts.py'
          sh 'pytest ./tests/main.py'
        }
      }
    }
    
    stage ('Merging release and develop'){
			steps{
            withCredentials([sshUserPrivateKey(credentialsId: '29636bef-b4c4-4133-bfd1-dac8c51a64c2', keyFileVariable: 'SSH_KEY')]) {
                sh 'git checkout main'
                sh 'git pull'
                sh 'git merge origin/dev'
                sh 'GIT_SSH_COMMAND="ssh -i $SSH_KEY" git push git@github.com:yelyzavetashapran/JenkinsTask.git'
            }
        }
	}
	}
}


