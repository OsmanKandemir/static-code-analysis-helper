from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    LOG = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.GOOD = ''
        self.LOG = ''
        self.ENDC = ''

class log:
    info = "[INF]"


def time():
    return datetime.utcnow().strftime("%B %d %Y - %H:%M:%S")

def worktime():
    return datetime.utcnow().strftime('%Y%m%d%H%M%S%f')

def msg(m):
    ti = " , "
    # n = 55
    print(f"{bcolors.OKBLUE}{log.info}{bcolors.ENDC}{m}")