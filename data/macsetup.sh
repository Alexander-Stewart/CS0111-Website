if [ ! $(which python3.7) ]; then
    echo "You have to install python3.7 before running this script";
    echo "If you did install python3.7, email the TAs";
    exit 1;
fi

mkdir -p $HOME/bin # make a bin directory if it doesn't exist yet

# add bin to path if it's not there yet
[[ $PATH != *"$HOME/bin:"* ]] && echo 'export PATH="$HOME/bin:$PATH"' >> $HOME/.bash_profile

[ ! -f $HOME/bin/python ] && ln -s $(which python3.7) $HOME/bin/python # add Python to bin
[ ! -f $HOME/bin/pip ] && ln -s $(which pip3.7) $HOME/bin/pip # add pip to bin

# update pip to stop getting annoying error messages
$HOME/bin/pip install --upgrade pip 

# install ipython
$HOME/bin/pip install -q ipython
# add ipython to path
[ ! -f $HOME/bin/ipython ] && ln -s $(which ipython3) $HOME/bin/ipython 

