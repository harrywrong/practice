import os
import time
from multiprocessing import Process


# from os import fork as a

# 程序执行到os.fork()时，操作系统会创建一个新的进程（子进程），然后复制父进程的所有信息到子进程中
# 然后父进程和子进程都会从fork()函数中得到一个返回值，在子进程中这个值一定是0，而父进程中是子进程的 id号
# pid = os.fork()
# if pid ==0:
#     print("{}:{}".format(pid,"1"))
# else:
#     print("{}:{}".format(pid,"2"))


# 多进程中，每个进程中所有数据（包括全局变量）都各有拥有一份，互不影响
# x =  1
# pid = os.fork()
# if pid<0:
#     print("fork调用失败。")
# elif pid == 0:
#     x += 3
#     print("我是子进程（%s），我的父进程是（%s）,x的值为(%s)"%(os.getpid(),os.getppid(),x))
# else:
#     x += 2
#     print("我是父进程（%s），我的子进程是（%s）,x的值为(%s)"%(os.getpid(),pid,x))
#
#
# print("父子进程都可以执行这里的代码,,x的值为(%s)"%x)
# 多次fork的问题
# 父进程、子进程执行顺序没有规律，完全取决于操作系统的调度算法
# pid = os.fork()
# if pid == 0:
#     print('哈哈1')
# else:
#     print('哈哈2')
#
# pid = os.fork()
# if pid == 0:
#     print('哈哈3')
# else:
#     print('哈哈4')
#
# time.sleep(1)

# # 子进程要执行的代码
# def run_proc(name):
#     print('子进程运行中，name= %s ,pid=%d...' % (name, os.getpid()))

# 两个子进程将会调用的两个方法
def worker_1(interval):
    print("worker_1,父进程(%s),当前进程(%s)" % (os.getppid(), os.getpid()))
    t_start = time.time()
    time.sleep(interval)  # 程序将会被挂起interval秒
    t_end = time.time()
    print("worker_1,执行时间为'%0.2f'秒" % (t_end - t_start))


def worker_2(interval):
    print("worker_2,父进程(%s),当前进程(%s)" % (os.getppid(), os.getpid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("worker_2,执行时间为'%0.2f'秒" % (t_end - t_start))


if __name__ == '__main__':
    #     print('父进程 %d.' % os.getpid())
    #     p = Process(target=run_proc, args=('test',))
    #     print('子进程将要执行')
    #     p.start()
    #     p.join()#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    #     print('子进程已结束')

    # 输出当前程序的ID
    print("进程ID：%s" % os.getpid())

    # 创建两个进程对象，target指向这个进程对象要执行的对象名称，
    # args后面的元组中，是要传递给worker_1方法的参数，
    # 因为worker_1方法就一个interval参数，这里传递一个整数2给它，
    # 如果不指定name参数，默认的进程对象名称为Process-N，N为一个递增的整数
    p1 = Process(target=worker_1, args=(2,))
    p2 = Process(target=worker_2, name="dongGe", args=(1,))

    # 使用"进程对象名称.start()"来创建并执行一个子进程，
    # 这两个进程对象在start后，就会分别去执行worker_1和worker_2方法中的内容
    p1.start()
    p2.start()

    # 同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
    print("p2.is_alive=%s" % p2.is_alive())

    # 输出p1和p2进程的别名和pid
    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)

    # join括号中不携带参数，表示父进程在这个位置要等待p1进程执行完成后，
    # 再继续执行下面的语句，一般用于进程间的数据同步，如果不写这一句，
    # 下面的is_alive判断将会是True，在shell（cmd）里面调用这个程序时
    # 可以完整的看到这个过程，大家可以尝试着将下面的这条语句改成p1.join(1)，
    # 因为p2需要2秒以上才可能执行完成，父进程等待1秒很可能不能让p1完全执行完成，
    # 所以下面的print会输出True，即p1仍然在执行
    p1.join()
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
