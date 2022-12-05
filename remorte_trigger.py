#!usr/bin/python3

import jenkins
from jenkinsapi.jenkins import Jenkins


server = jenkins.Jenkins('http://192.168.0.119:8080/', username='Ganesh', password="12345")
user = server.get_whoami()
version = server.get_version()
print(user['fullName'])
print("version : "+version)

def trigger_job(RunID,CustomerID,AssignedInstanceID,AssignedInstanceIP,ServiceSubscribed,SubCompsToRun):
    server.build_job('Final_Test', {"Run-ID":RunID,"Customer-ID":CustomerID,"Assigned-Instance-ID":AssignedInstanceID,"Assigned-Instance-IP":AssignedInstanceIP,"Service-Subscribed":ServiceSubscribed,"Sub-Comps-To-Run":SubCompsToRun})
    last_build_number = server.get_job_info('Final_Test')['lastCompletedBuild']['number']
    print("current_Job_no. : ",last_build_number+1)
    # build_info = server.get_build_info('test', last_build_number)

def get_params():
    with open("params.txt","r") as param_file:
        params = param_file.read().splitlines()
    return params

param_list = get_params()
trigger_job(param_list[0],param_list[1],param_list[2],param_list[3],param_list[4],param_list[5])#"1","2","3","4","5","6")