# Suppose you want to build your own Deep Learning Framework(Hard+Soft-ware)
# from scratch: https://towardsdatascience.com/build-and-setup-your-own-deep-learning-server-from-scratch-e771dacaa252

## Assuming you have installed conda from here:
# Complete tutorial here: https://www.programcreek.com/2017/01/set-up-development-environment-for-deep-learning/
# https://docs.anaconda.com/anaconda/install/linux

# How to pick the right tool for deep learning:
# see https://www.programcreek.com/2017/01/how-to-select-the-right-tool-for-deep-learning/
#create your environment
conda create -n dlp3 python=3.7

#activate your env
source activate dlp3

# install recomended Machine Learning packages:
pip install numpy
pip install pandas
pip install scikit-learn
pip install seaborn

# install deep learning packages
pip install tensorflow
pip install keras

# deactivate your environment if no using again
source deactivate dlp3

# if a fan of pycharm:
# Download pycharm from here:
## https://www.jetbrains.com/pycharm/download/#section=linux
wget https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux&code=PCC
##copy it to /opt directory
sudo cp pycharm-community-2017.1.4.tar.gz /opt/
## Unzip the file:
cd /opt/
tar -xzvf pycharm-community-2017.1.4.tar.gz

# Run the script to start pycharm
. /opt/pycharm-community-2017.1.4/bin/pycharm.sh