import errno
import logging
import os
import random
import string
import subprocess
import sys
from collections import OrderedDict


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

def genID(str_len):
    """
    Generate a random alphanumeric string of length `str_len`.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(str_len))

def dict_all_over(obj):
    """
    Specifically for output of `xmltodict` package's `parse` method.

    Usage:
    from xmltodict import parse
    
    xml = '<aldkj asld="asldk" alsdfj="100.2"></aldkj>'
    xml = '<aldkj asld="asldk" alsdfj="100.2">laskdjf<alsdkfj>aaldkj</alsdkfj><alsdkfj>aaldaldskfjkj</alsdkfj></aldkj>'
    xml = '<asfd><alsdkfj>aaldkj</alsdkfj><alsdkfj>aaldaldskfjkj</alsdkfj></asfd>'

    dict_all_over(parse(xml))
    """
    if type(obj) == OrderedDict:
        for key, value in obj.iteritems():
            if key[0] != '@' and key != '#text':
                obj[key] = dict_all_over(value)
        return obj
    elif type(obj) == list:
        for i in xrange(len(obj)):
            obj[i] = dict_all_over(obj[i])
        return obj
    else:
        a = OrderedDict()
        a["#text"] = obj
        return a

