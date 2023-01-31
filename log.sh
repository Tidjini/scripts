# CREATE LOG FOLDER (DIR) oherwise use /home/.logs/project_name/ 
# echo $password | sudo -S -k mkdir /home/$user/.logs/project_name/ 

PASSWORD=$1
PROJECT=$2

create_project_logger(){
    echo "LOG FOLDER CREATION"
    echo $PASSWORD | sudo -S -k mkdir /var/log/$PROJECT
}

echo 'testing ...'
create_project_logger