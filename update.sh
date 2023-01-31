PASSWORD=$1
# ##########UPDATE AND UPGRADE (1)###################
update_and_upgrade(){
    pass_show="**********"
    echo "UPDATING AND UPGRADING..."
    echo "UPDATE..."
    echo $PASSWORD | sudo -S -k apt-get -y update
    echo $pass_show
    echo "UPGRADE..."
    echo $PASSWORD | sudo -S -k apt-get -y upgrade
    echo $pass_show
    echo "UPDATE AND UPGRADE FINISH"
}
echo 'testing ...'
update_and_upgrade
# ##########UPDATE AND UPGRADE###################