#!/usr/bin/env sh

#This script will copy the last artifact build and remotely execute the deployment script.

# Jenkins server url is http://yourjenkins:8080
# details of the last successful build viewed at http://yourjenkins:8080/job/appjob/lastSuccessfulBuild/
wget -q -O- http://http://localhost:8080/job/PythonPipeline/lastSuccessfulBuild/api/xml?tree=artifacts[relativePath] | xpath '//relativePath/text()' 2>&1 | sed -re 's/-- NODE --//g' | tail -n+3\
| while read fileName;\
do \
   wget "${url}artifact/${fileName}";\
done

#copy to the server
scp -i <HOME_DIR>/.ssh/id_dsa /jobs/PythonPipeline/

#connect to the server and execute the deployment script
ssh -i <HOME_DIR>/.ssh/id_dsa  





