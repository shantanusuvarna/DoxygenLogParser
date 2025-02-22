pipeline {
    agent any
    stages {
        stage('Clone RepoA') {
            steps {
                git branch: 'master', url: 'https://github.com/shantanusuvarna/RepoA.git'
            }
        }
        stage('Modify Doxygen Config for Warnings') {
            steps {
                bat "doxygen -g Doxyfile"
                bat "powershell -Command \"(Get-Content Doxyfile) -replace 'INPUT.*', 'INPUT = src' | Set-Content Doxyfile\""
                bat "powershell -Command \"(Get-Content Doxyfile) -replace 'GENERATE_HTML.*', 'GENERATE_HTML = YES' | Set-Content Doxyfile\""
                bat "powershell -Command \"(Get-Content Doxyfile) -replace 'WARN_LOGFILE.*', 'WARN_LOGFILE = warnings.log' | Set-Content Doxyfile\""
            }
        }
        stage('Run Doxygen') {
            steps {
                bat "doxygen Doxyfile"
            }
        }
        stage('Clone RepoC') {
            steps {
                git branch: 'main', url: 'https://github.com/shantanusuvarna/DoxygenLogParser'
            }
        }
        stage('Run Log Parser') {
            steps {
                bat "python log_parser.py warnings.log parsed_warnings.csv"
                archiveArtifacts artifacts: 'parsed_warnings.csv', fingerprint: true
            }
        }
    }
}
