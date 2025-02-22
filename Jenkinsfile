pipeline {
    agent any
    
    stages {
        stage('Clone RepoA') {
            steps {
                git branch: 'master', url: 'https://github.com/shantanusuvarna/RepoA.git'
            }
        }
        stage('Generate Doxygen Config') {
            steps {
                bat 'doxygen -g Doxyfile'
                bat 'powershell -Command "Set-ExecutionPolicy Unrestricted -Scope Process -Force"'
                bat """powershell -Command "(Get-Content Doxyfile) -replace 'INPUT\\s*=.*', 'INPUT = src' | Set-Content Doxyfile" """
                bat """powershell -Command "(Get-Content Doxyfile) -replace 'GENERATE_HTML\\s*=.*', 'GENERATE_HTML = YES' | Set-Content Doxyfile" """
                bat 'type Doxyfile'  // Print modified file for debugging
            }
        }
        stage('Run Doxygen') {
            steps {
                bat 'doxygen Doxyfile'  // Run doxygen with the modified config
            }
        }
        stage('Check Documentation Output') {
            steps {
                bat 'if not exist html echo "Doxygen output not found!" && exit /b 1'
            }
        }
        stage('Archive Documentation') {
            steps {
                bat 'powershell Compress-Archive -Path html -DestinationPath doc.zip'
                archiveArtifacts artifacts: 'doc.zip', fingerprint: true
            }
        }
    }
}
