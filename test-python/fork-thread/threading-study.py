import time
import threading
import os


def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)


if __name__ == "__main__":
    # for i in range(5):
    #     t = threading.Thread(target=saySorry)
    #     t.start()
    p = os.fork()
    saySorry()
