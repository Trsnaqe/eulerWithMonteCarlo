from hw import FindEuler, Timer
from threading import Thread
import os

if __name__ == "__main__":
    tt = Timer()
    tt.time1()
    n = 10000000
    euler_finders = []
    threads = []
    for i in range(os.cpu_count()):
        euler_finders.append(FindEuler())
        threads.append(Thread(target=euler_finders[i].generate_capsules, args=(n,)))
        print("Thread %d has been started" % i)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    exceededNums = 0
    generatedCaps = 0
    for euler_finder in euler_finders:
        exceededNums += euler_finder.sumOfI
        generatedCaps += euler_finder.run_amount
    euler = exceededNums / generatedCaps
    print("E=%.5f & SumOfI=%d & Run Amount=%d & Time Elapsed=%.5f second(s)"
          % (euler, exceededNums, generatedCaps, tt.time2()))
