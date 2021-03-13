# afk_ui
Untill we solve pip install from pypi - setup.sh will install from local folder - '*downloaded_pakages*'.

Steps to add package from outside:

* Add package to pip_freeze.txt:  
```
. venv/bin/activate
pip install [PACKAGE]
pip freeze > pip_freeze.txt
```
- download package with all its dependencies.  
 
from linux machine:
```
pip3 download [PACKAGE] -d downloaded_packages
```
from from MacOS: 
```
pip3 download -r requirements.txt -d downloaded_packages_macos
```
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