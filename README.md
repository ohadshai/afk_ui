# afk_ui

 before running setup.sh - need to **disable SELinux** (Securit-Enhanced Linux):  
 ```
sudo vi /etc/selinux/config
```
inside file change to:
```
SELINUX=disabled
```
reboot:
```
sudo shutdown -r now
```