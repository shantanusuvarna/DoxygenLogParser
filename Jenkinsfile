pipeline {
    agent any
    stages {
        stage('Clone RepoA') {
            steps {
                git branch: 'main', url: 'https://github.com/shantanusuvarna/RepoA.git'
            }
        }
        stage('Modify Doxygen Config for Warnings') {
            steps {
                sh 'doxygen -g Doxyfile'
                sh "sed -i 's|INPUT.*|INPUT = src|' Doxyfile"
                sh "sed -i 's|GENERATE_HTML.*|GENERATE_HTML = YES|' Doxyfile"
                sh "sed -i 's|WARN_LOGFILE.*|WARN_LOGFILE = warnings.log|' Doxyfile"
            }
        }
        stage('Run Doxygen') {
            steps {
                sh 'doxygen Doxyfile'
            }
        }
        stage('Clone RepoC') {
            steps {
                git branch: 'main', url: 'https://github.com/shantanusuvarna/DoxygenLogParser'
            }
        }
        stage('Run Log Parser') {
            steps {
                sh 'python log_parser.py warnings.log parsed_warnings.csv'
                archiveArtifacts artifacts: 'parsed_warnings.csv', fingerprint: true
            }
        }
    }
}