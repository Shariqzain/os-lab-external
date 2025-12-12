import threading
import time
import random
from queue import Queue

buffer = Queue(maxsize=5)

def producer():
    while True:
        item = random.randint(1, 100)
        buffer.put(item)
        print(f"Produced: {item}")
        time.sleep(random.uniform(0.5, 2))

def consumer():
    while True:
        item = buffer.get()
        print(f"Consumed: {item}")
        time.sleep(random.uniform(1, 3))

# Create threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()
