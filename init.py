import subprocess

#this is to help work around aws resources
import boto3
#dump database to home directory
subprocess.run('mysqldump --host=host -u username -ppassword databasename > ~/pythonscriptedb.sql',shell=True)
