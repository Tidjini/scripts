#!/bin/bash
PASSWORD=$1
USER=$2
USER_PASSWORD=$3
PROJECT=$4
LOG_FOLDER='/home/project_name/.logs'
ERROR_TMP='errtmp'

# DELETE
# echo $password | sudo -S -k userdel username
# echo $password | sudo -S -k rm -r /home/username
create_user(){
    # at this point user adduser in place instead of useradd (still some issue in this command)
    echo "USER CREATION / $USER"
    password_encripted=$(perl -e 'print crypt($ARGV[0], "password")' $USER_PASSWORD)
    echo $PASSWORD | sudo -S -k useradd -p $password_encripted $USER
    echo '***********'
    echo "GRANT $USER with sudo"
    echo $PASSWORD | sudo -S -k adduser $USER sudo
    echo '***********'
    # echo $PASSWORD | sudo -S -k -i   #to get root privileges
    echo $PASSWORD | sudo -S -k mkdir /home/$USER  #to create the directory   
    echo '***********'
    echo $PASSWORD | sudo -S -k cp -rT /etc/skel /home/$USER  #to populate with default files and folders      
    echo '***********'      
    echo $PASSWORD | sudo -S -k chown -R $USER:$USER /home/$USER #to change the owner of DIR to user 
    echo '***********'
    echo $PASSWORD | sudo -S -k touch /home/$USER/.hushlogin
    echo '***********'
    echo "User creation done"
}

echo 'testing ...'
create_user