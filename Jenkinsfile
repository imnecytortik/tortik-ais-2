// Powered by Infostretch 

timestamps {

node () {

	stage ('tsarenko_td tortik1 - Checkout') {
 	 checkout([$class: 'GitSCM', branches: [[name: 'main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/imnecytortik/tortik-ais-1']]]) 
	}
	stage ('tsarenko_td tortik1 - Build') {
 			// Shell build step
sh """ 
pip3 install -r req.txt 
 """		// Shell build step
sh """ 
python3 -m pytest test.py 
 """ 
	}
}
}