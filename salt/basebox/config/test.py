import syslog
import os
import sys
import signal
import time

pid = os.getpid()
aid = sys.argv[1:2]

class Flag:
    def __init__(self):
        self.should_stop = False

    def stop(self):
        self.should_stop = True

flag = Flag()

def signal_handler(signum, _frame):
    syslog.syslog("received signal %s" % signum)
    flag.stop()

signal.signal(signal.SIGTERM, signal_handler)


iteration=0
while not flag.should_stop:
    iteration += 1
    message = "aid: %s, pid: %s, iteration: %s" % (aid, pid, iteration)
    syslog.syslog(message)
    syslog.syslog("start of long operation")
    # long operation that persists even if interrupted by signals in time.sleep()
    for i in range(0, 5):
        time.sleep(1)
    syslog.syslog("end of long operation")

syslog.syslog("gracefully stopping")
