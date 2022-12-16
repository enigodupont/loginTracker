
pipeline {
  agent {
    kubernetes {
        yaml '''
            apiVersion: v1
            kind: Pod
            metadata:
                name: build
            spec:
                volumes:
                - name: kaniko-config
                  secret:
                    secretName: kaniko-config
                containers:
                    - name: kaniko
                      image: gcr.io/kaniko-project/executor:debug
                      imagePullPolicy: "IfNotPresent"
                      command:
                        - /busybox/cat
                      tty: true
                      volumeMounts:
                        - mountPath: "/kaniko/.docker/config.json"
                          subPath: "config.json"
                          readOnly: true
                          name: kaniko-config
                    - name: sonarscan
                      image: sonarsource/sonar-scanner-cli
                      imagePullPolicy: "IfNotPresent"
                      command:
                        - cat
                      tty: true
                    - name: git
                      image: alpine/git:v2.34.2
                      imagePullPolicy: "IfNotPresent"
                      command:
                        - cat
                      tty: true
        '''
    }
  }
  
  stages {
    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv('Eniworks') {
          container('sonarscan') {
              sh "sonar-scanner -Dsonar.projectKey=LOGINTRACKER -Dsonar.sources=loginTrackerServer"
          }
        }
      }
    }
    stage('Build/Push Docker Image') {
      steps {
        container('kaniko') {
            sh "/kaniko/executor --context . --cache --destination=enigodupont/logintracker:default_tag_change_me --destination=enigodupont/logintracker:$BUILD_NUMBER"
        }
      }
    }
    stage('Update argo image') {
      steps {
        withCredentials(bindings: [sshUserPrivateKey(credentialsId: '8fe21223-8d56-49ea-8eb5-6dc0171c102f', keyFileVariable: 'GIT_SSH_KEY', passphraseVariable: '', usernameVariable: '')]) {
          container('git') {
            sh "mkdir -p /root/.ssh"
            // This method hides the variable
            sh('mv $GIT_SSH_KEY /root/.ssh/id_rsa')
            sh '''
              cd /tmp
              chmod 0600 /root/.ssh/id_rsa
              ssh-keyscan -t rsa github.com >> /root/.ssh/known_hosts
              git config --global user.name 'Jenkins Automation'
              git config --global user.email 'juramir@protonmail.com'
              git clone git@github.com:enigodupont/loginTracker.git
              cd loginTracker
              git checkout -B argo_cd
              sed s/default_tag_change_me/$BUILD_NUMBER/g ./argo/deployment.yaml -i
              git add .
              git commit -m 'ArgoCD build update commit'
              git push -f --set-upstream origin argo_cd
            '''
          }
        }
      }
    }
  }
}
