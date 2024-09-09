# Test preparation procedure
## 1. Install Jenkins and start up
#### $ cd ~/webpage_ws
#### $ ./start_jenkins.sh
#### $ jenkins_address (To monitor jenkins job, copy the link and past to the browser and select ros1_ci_pipeline job)
#### # echo "$(jenkins_address)github-webhook/" (update webhook address at https://github.com/invokelee/ros1_ci/settings/hooks)

## 2. Create ssh key
#### $ cd ~/webpage_ws
#### $ ./setup_ssh_git.sh
#### $ cat ~/.ssh/id_rsa.pub && echo '' && cat ~/.ssh/id_rsa

## 3. Install docker
#### $ cd ~/catkin_ws/src/ros1_ci_docker
#### $ ./start_docker_v2.sh
#### $ newgrp docker

## 4. Establish the authenticity of host 'github.com'
#### $ git ls-remote -h -- git@github.com:invokelee/ros1_ci.git HEAD (Enter 'yes')

### Proceed evaluation steps
