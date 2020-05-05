#!/usr/bin/env sh

# Jenkins server url is http://yourjenkins:8080

# details of the last successful build viewed at http://yourjenkins:8080/job/appjob/lastSuccessfulBuild/
wget -q -O- http://http://localhost:8080/job/PythonPipeline/lastSuccessfulBuild/api/xml?tree=artifacts[relativePath] | xpath '//relativePath/text()' 2>&1 | sed -re 's/-- NODE --//g' | tail -n+3\
| while read fileName;\
do \
   wget "${url}artifact/${fileName}";\
done







#This script will copy the last artifact build by the job "MyApp" to test.myserver.com
#and remotely execute the deployment script.

#copy the war to the server
#(the job "MyApp" is using maven, that's why the war can be found at this location)
#scp -i <HOME_DIR>/.ssh/id_dsa $HUDSON_HOME/jobs/MyApp_Build/workspace/myapp/target/myapp.war     deployeruser@test.myserver.com:/tmp/

#connect to the server and execute the deployment script
#ssh -i <HOME_DIR>/.ssh/id_dsa deployeruser@test.myserver.com 

#The following is just an example of what a deployment script can be.
#of course you must adapt it to your needs and environment
#"cd <TOMCAT_DIR>;

#first copy the current war to a backup directory (additionaly, I have a cron task deleting old undeployed apps)
#cp -rf myapp-apps/myapp* undeployed/myapp-apps/; 

#execute a script (stored on the server) to properly stop the app
#sh bin/myapp.sh stop; 

#delete current app
#rm -rf myapp-apps/myapp; 
#rm -rf myapp-apps/myapp.war;

#copy the uploaded war in tomcat app directory 
#cp /tmp/myapp.war myapp-apps/; 

#execute a script (stored on the server) to start the app
#sh bin/myapp.sh start"



