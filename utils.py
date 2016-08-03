import errno
import logging
import os
import subprocess
import sys

def get_git_commit_hash(filename):
    """Gets the latest git commit hash for the given absolute file path.

    Assumes git command works.
    git repository is cloned and updated in local.
    filename is absolute path of that filename.

    Parameters
    ----------
    filename : str
        absolute path of the file we want to get commit hash for.

    Returns
    -------
    str
        Hash value of the latest git commit, the file is part of.

    """
    if not os.path.isabs(filename):
        logging.error(filename + " :should be an absolute path.")
        raise Exception(filename + " :should be an absolute path.")

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    logging.info(subprocess.check_output('pwd', shell=True).strip())

    command = 'git log -n 1 --format="%%H" -- %s' % filename
    logging.info(command)

    return subprocess.check_output(command, shell=True).strip().decode('utf-8')

def mkdir_p(dir_name):
    """Imitates mkdir_p functionality.

    Reference: http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python

    Parameters
    ----------
    dir_name : str
        The directory path that is to be created with 
        all the internal directories, if it does not exist.

    Exceptions
    ----------
    Propagates the OSError from os.makedirs if 
    it's not about the directory already being present.

    """
    try:
        os.makedirs(dir_name)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(dir_name):
            pass
        else:
            raise

