import threading
import time

class myThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        print("running on number:%s" %self.num)
        time.sleep(3)
        print(self.num)

if __name__ == '__main__':
    t1=myThread(56)
    t2=myThread(78)
    t1.start()
    t2.start()
    print("ending...")

'''总结
子进程未结束，主进程不会结束
'''
