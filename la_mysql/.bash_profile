alias mysql=/usr/local/mysql/bin/mysql
alias mysqladmin=/usr/local/mysql/bin/mysqladmin


# added by Anaconda3 2019.03 installer
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/Users/lucytodd/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/Users/lucytodd/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/lucytodd/anaconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/Users/lucytodd/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<

PYTHONPATH=/Users/lucytodd/Development/python/pymodules
PYTHONPATH=$PYTHONPATH:/Users/lucytodd/anaconda3/lib/python37.zip
PYTHONPATH=$PYTHONPATH:/Users/lucytodd/anaconda3/lib/python3.7
PYTHONPATH=$PYTHONPATH:/Users/lucytodd/anaconda3/lib/python3.7/lib-dynload PYTHONPATH=$PYTHONPATH:/Users/lucytodd/.local/lib/python3.7/site-packages PYTHONPATH=$PYTHONPATH:/Users$

export PYTHONPATH
