from multiprocessing import Process, Pipe

def child_process(conn):
    msg = conn.recv()  # Receive data from parent
    print(f"Child received: {msg}")
    conn.send("Hello Parent, Message Received!")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=child_process, args=(child_conn,))
    p.start()
    parent_conn.send("Hello Child, from Parent!")  # Send data to child
    print(f"Parent received: {parent_conn.recv()}")
    p.join()