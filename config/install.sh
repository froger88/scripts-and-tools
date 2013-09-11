#!/bin/bash

# mkdir for basic scripts
mkdir -p $HOME/.scripts_by_froger88

#copy .bash_profile
cp .bash_profile $HOME/

#copy .tmux.conf
cp .tmux.conf $HOME/


# copy .gitconfig
## print existing .gitconfig
echo "existing .gitconfig:"
cat $HOME/.gitconfig

echo "diff:"
diff .gitconfig $HOME/.gitconfig

echo "copying new .gitconfig"
cp .gitconfig $HOME/
echo "Please set up name and email in .gitconifg"
read -p "press [Enter] to continue"
nano $HOME/.gitconfig


# run source on .bash_profile
source $HOME/.bash_profile


# copy list_cores.sh script and give run privilages
#cp list_cores.sh $HOME/.scripts_by_froger88 -R
#chmod +x $HOME/.scripts_by_froger88/list_cores.sh
