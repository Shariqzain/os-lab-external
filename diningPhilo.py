import threading
import time
import random

# Number of philosophers
N = 5

# Create a semaphore for each fork
forks = [threading.Semaphore(1) for _ in range(N)]

def philosopher(i):
    while True:
        print(f"Philosopher {i} is thinking.")
        time.sleep(random.uniform(1, 3))  # Thinking time

        print(f"Philosopher {i} is hungry.")
        
        # Pick up left fork
        forks[i].acquire()
        print(f"Philosopher {i} picked up left fork.")

        # Pick up right fork
        forks[(i + 1) % N].acquire()
        print(f"Philosopher {i} picked up right fork.")

        print(f"Philosopher {i} is eating.")
        time.sleep(random.uniform(1, 2))  # Eating time

        # Put down right fork
        forks[(i + 1) % N].release()
        print(f"Philosopher {i} put down right fork.")

        # Put down left fork
        forks[i].release()
        print(f"Philosopher {i} put down left fork.")

# Create and start threads for each philosopher
philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]

for p in philosophers:
    p.start()
