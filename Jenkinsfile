pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh '/home/moshe/envs/django_tests_fe/bin/python /home/moshe/projects/django_tests_fe/integration_tests_fe/manage.py test'
            }
        }
    }
}
