from multiprocessing import Process, shared_memory
import numpy as np

def child_process(name):
    existing_shm = shared_memory.SharedMemory(name=name)
    shared_array = np.ndarray((5,), dtype=int, buffer=existing_shm.buf)
    print("Child reads data:", shared_array[:])
    shared_array[0] = 99
    existing_shm.close()

if __name__ == "__main__":
    data = np.array([1, 2, 3, 4, 5], dtype=int)
    shm = shared_memory.SharedMemory(create=True, size=data.nbytes)
    shared_array = np.ndarray(data.shape, dtype=data.dtype, buffer=shm.buf)
    shared_array[:] = data[:]
    print("Parent wrote data:", shared_array[:])

    p = Process(target=child_process, args=(shm.name,))
    p.start()
    p.join()

    print("Parent reads modified data:", shared_array[:])
    shm.close()
    shm.unlink()
