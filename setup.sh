#!/bin/bash

bold='\033[1m'
red='\e[31m'
green='\e[32m'
light_green='\e[92m'
yel='\e[33m'
blu='\e[34m'
mag='\e[35m'
cyn='\e[36m'
end='\e[0m'

crossmark="${red}\u2718${end}"
checkmark="${green}\u2714${end}"


print_pink(){
  msg=$1
  echo -e "${bold}${cyn}${msg}${end}"
}

print_bold(){
  msg=$1
  echo -e "${bold}${msg}${end}"
}

print_info(){
  msg=$1
  echo -e "${green}${msg}${end}"
}

failure(){
	msg=$1
  echo -e "${crossmark} ${red}${msg}${end}"
  exit -1
}

success(){
  msg=$1
  echo -e "${checkmark} ${light_green}${msg}${end}"
}

success_bold(){
  msg=$1
  echo -e "${bold}${green}${msg}${end}"
}

check_exit_code(){
  exit_code=$?
  err_msg=$1
  success_msg=$2
  if [[ $exit_code -ne 0 ]]; then
    failure "$err_msg"
  elif [[ ! -z $success_msg ]]; then
    success "$success_msg"
  fi
}

check_root(){
  if [[ $EUID -ne 0 ]]; then
      		failure "This script must be run as root"
	fi
}

check_linux(){
	os=$(uname -s)
	if [ $os != "Linux" ]; then 
		failure "This script can run only on Linux system"
	fi 	
}

host_info(){
  host_info=$(hostnamectl)
  print_bold "-------------------    Host Info    ------------------------"
  print_pink "$host_info"
  print_bold "------------------------------------------------------------"
  print_bold "Starting Installation..."
}

check_connection(){
	curl -s  http://google.com > /dev/null
	check_exit_code "Connection to network failed. Check connection..." "Connected to Network"
}

install_yum_packages(){
  print_info "Updating yum.."
  yum update -y > /dev/null
  check_exit_code "yum update failed" "yum update finished successfully"
  print_info "Install yum packages"
  yum -y groupinstall "Development Tools" > /dev/null
  yum -y install openssl-devel bzip2-devel libffi-devel sqlite-devel wget > /dev/null
  check_exit_code "yum packages failed to install" "yum packages installed successfully"
}

install_python3(){
  print_info "Installing Python3.8"
  python3 --version > /dev/null 2>&1
  if [[ $? -eq 0 ]]; then
    success "python + pip already installed"
  else
    print_bold " - Downloading python"
    sudo -u $USER mkdir downloads
    wget https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz -P downloads > /dev/null 2>&1
    tar xvf downloads/Python-3.8.7.tgz -C downloads > /dev/null
    pushd downloads/Python-3.8.7 > /dev/null
    print_bold " - Configure + Make"
    ./configure --enable-optimizations > /dev/null 2>&1
    make altinstall > /dev/null 2>&1
    popd > /dev/null
    ln -s /usr/local/bin/python3.8 /usr/local/bin/python3
    ln -s /usr/local/bin/pip3.8 /usr/local/bin/pip3
    sed -i -e '/secure_path/ s[=.*[&:/usr/local/bin[' /etc/sudoers
    export PATH="$PATH:/usr/local/bin"
    python3 --version > /dev/null
    check_exit_code "python3 failed to install" "python3 installed successfully"
    pip3 --version > /dev/null
    check_exit_code "pip3 failed to install" "pip3 installed successfully"
  fi
  pip3 install virtualenv > /dev/null 2>&1
  check_exit_code "virtualenv failed to install" "virtualenv installed successfully"
}

create_virtualenv(){
  print_info "Creating virtualenv"
  sudo -u $USER python3 -m virtualenv venv > /dev/null 2>&1
  . venv/bin/activate
  check_exit_code "virtualenv failed to create" "virtualenv created successfully"
  print_info "Installing dependencies"
  print_bold "$(cat requirements.txt)"
  pip3 install --no-index --find-links=downloaded_packages -r requirements.txt > /dev/null
  check_exit_code "dependencies failed to install" "dependencies installed successfully"
  deactivate
}

start_service(){
  print_info "starting afk-ui Service"
  cp afk-ui.service /etc/systemd/system/
  systemctl daemon-reload
  systemctl start afk-ui
  systemctl is-active --quiet afk-ui
  if [[ $? -ne 0 ]]; then
    failure "afk-ui Service failed to run. Run 'sudo journalctl -xe' to see the reason"
  else
    success_bold "------------------------------------------"
    success_bold "afk-ui Service Started to run Successfully"
    success_bold "------------------------------------------"
  fi
}


main(){
  check_root
  check_linux
  host_info
  check_connection
  install_yum_packages
  install_python3
  create_virtualenv
  start_service
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
