import syslog
import os
import sys
import signal

pid = os.getpid()
aid = sys.argv[1:2]

class Flag:
    def __init__(self):
        self.should_stop = False

    def stop(self):
        self.should_stop = True

flag = Flag()

def signal_handler(signum, _frame):
    print("received signal %s", signum)
    flag.stop()

signal.signal(signal.SIGTERM, signal_handler)


iteration=0
while not flag.should_stop:
    iteration += 1
    message = "aid: %s, pid: %s, iteration: %s" % (aid, pid, iteration)
    syslog.syslog(message)
    print("start of long operation")
    # long operation that is not interrupted by signals like time.sleep()
    for i in range(0, 1000000):
        with open('/dev/null') as fp:
            fp.read()
    print("end of long operation")

print("gracefully stopping")
