import threading
import time
from queue import Queue

q = Queue()

def create_objects():
    for i in range(5):
        obj = f"Object-{i}"
        print("[Creator] Created:", obj)
        q.put(obj)
        time.sleep(1)
    q.put(None)

def process_objects():
    while True:
        obj = q.get()
        if obj is None:
            break
        print("[Processor] Processing:", obj)
        time.sleep(2)

t1 = threading.Thread(target=create_objects)
t2 = threading.Thread(target=process_objects)

t1.start()
t2.start()

t1.join()
t2.join()

print("Finished!")
