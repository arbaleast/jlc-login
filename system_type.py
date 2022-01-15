import os, re, platform

def system():
    plat = platform.system()
    match plat:
        case 'Windows':
            tmp = os.popen('where geckodriver')
            path = re.split(r'\n', tmp.read())[1]
            return path
        case 'Linux':
            path = os.popen('which geckodriver')
            return path.read()
        case _:
            print('other platform?')