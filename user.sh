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


# default logs path /home/project_name/.logs
# USER -> BLOCANTE -> REPORT AND STOP PROCESSING
# check if the user exist
# otherwise create the user with password and grant the user with sudo

# CREATE LOG FOLDER (DIR) oherwise use /home/.logs/project_name/ 
# echo $password | sudo -S -k mkdir /home/$user/.logs/project_name/ 

# remember to log issues in file [errors] and logs
# function to store errors (stderr):
#   - for each commande add in the end  2>tmperr to capture stderr
#   - get error with cat tmperr to var stderr
#   - if error is empty then : return and continue
#   - if error exist :
#       - log to errors log echo > filename (append to stderr file the real output with formated one )
#       - if error is none blocant > continue to next commande notify in both cases
#       - else stop process and send notification to administrators or (set notification service (mail/socket), and restarer service from previous point)
# -S : PUT PASSWORD (echo value)
# -k : clear cache of sudo (repeat entering pass for visual perpose)


# handle_err(){
#     errors=$(cat $tmperr)
#     stop_next_process=$2
#     if [$errors = ''];then
#         # ok to go to next step
#         return true
#     fi

#     now=$(date)
#     # append error to /home/user/.logs/project_name/errors




#     if [$stop_next_process];then
#         echo 'stop processing...'
#         return false
#     else
#         echo 'continue exectution, the exception will be handle later'
#         return true
#     fi


# }


# hostname="home-dev"


# ########## SWITCH TO ROOT (TEST) not neceserly ##############
# #echo $password | sudo -S su
# ########## SWITCH TO ROOT ##############


# ##########UPDATE AND UPGRADE (1)###################
# # echo "UPDATING AND UPGRADING..."
# # echo "UPDATE..."
# # echo $password | sudo -S -k apt-get -y update 2>tmperr
# # execute error function
# # echo $pass_show
# # echo "UPGRADE..."
# # echo $password | sudo -S -k apt-get -y upgrade
# # echo $pass_show
# # echo "UPDATE AND UPGRADE FINISH"
# ##########UPDATE AND UPGRADE###################

# ##########SET A HOSTNAME###################
# # echo "SET HOSTNAME..."
# # echo $password | sudo -S -k hostnamectl set-hostname $hostname
# # echo $pass_show
# # sys_hostname=$(hostname)
# # if [ $sys_hostname != $hostname ]; then
# #      # echo and log in file this exeption to errors -> to set in pipline to restart from this point
# #       hostname=sys_hostname
# #       echo "set-hostname not work"        
# # fi
# # 
# ##########SET A HOSTNAME###################

# ########    SET HOSTNAME AND IP ADDRESS IN sudo nano /etc/hosts how to##### 

# sed -i '8i This is Line 8' FILE


# echo "ADD $user as USER"
# echo $password | sudo -S useradd -p $encripted $user
# echo "**********"
# echo "GRANT $user with sudo"
# echo $password | sudo adduser $user sudo




# # echo "enter your name :$1"
# # read name
# # user=$(whoami)
# # directory=$(pwd)
# # list=$(ls /)
# # echo "$list"
# # echo "Hi $name from $user in dir : $directory"
# # sleep 1
# # echo "It's good today ($name)"
# # sleep 1
# # echo 'Go Out, $name'
