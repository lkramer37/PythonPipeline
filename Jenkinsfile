pipeline {
    agent none
    stages {

        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile sources/tictactoe.py'
		stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_tictactoe.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }

        stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python2'
                }
            }
            steps {
                sh 'pyinstaller --onefile sources/tictactoe.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/TicTacToe'
                }
            }
        }
    }
}
