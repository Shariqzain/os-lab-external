from multiprocessing import Process, Semaphore
import time, random

sem = Semaphore(1)  # Allow 1 process at a time

def task(name):
    print(f"{name} is waiting to enter the critical section...")
    sem.acquire()
    print(f"{name} entered the critical section.")
    time.sleep(random.randint(1, 3))
    print(f"{name} is leaving the critical section.")
    sem.release()

if __name__ == "__main__":
    p1 = Process(target=task, args=("Process-1",))
    p2 = Process(target=task, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()