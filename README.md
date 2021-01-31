# afk_ui
* Untill we solve pip install from pypi - setup.sh will install from local folder - downloaded_pakages
I downloaded all needed packages using the command: ```pip3 download -r requirements.txt -d downloaded_packages```

## Setup Process ##
1.before running setup.sh - need to **disable SELinux** (Security-Enhanced Linux):  
 ```
sudo vi /etc/selinux/config
```
inside file change to:
```
SELINUX=disabled
```
then, reboot:
```
sudo shutdown -r now
```

2.  
```
sudo setup.sh
```