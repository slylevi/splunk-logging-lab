pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'git@github.com:slylevi/splunk-logging-lab.git'
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                echo 'Running Ansible Playbook...'
                sh 'ansible-playbook ./log-generator/deploy.yml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}

