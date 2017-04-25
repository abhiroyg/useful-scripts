import subprocess

def b(folder_path):
    try:
        a = subprocess.check_output('ls {}'.format(folder_path), shell=True)
    except:
        a = ''
    print filter(None, a.split())

b('/home/nineleaps/')
b('/home/nineleaps/Pictures/craigslist/')
