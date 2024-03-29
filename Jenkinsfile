timestamps {
    node () {
        stage ('tsarenko_td tortik2 - Checkout') {
            checkout([$class: 'GitSCM', branches: [[name: 'main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/imnecytortik/tortik-ais-2']]]) 
        }
        stage ('tsarenko_td tortik2 - Build') {
            sh """ 
pip3 install -r req.txt 
            """
            sh """ 
python3 -m pytest test.py 
            """ 
        }
    }
}