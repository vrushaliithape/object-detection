pipeline { 
    agent any 
 
    stages { 
        stage('Install Dependencies') { 
            steps { 
                bat 'pip3 install -r requirements.txt' 
            } 
        } 
 
        stage('Run Tests') { 
            steps { 
                bat 'python -m unittest' 
            } 
        } 
    } 
}
