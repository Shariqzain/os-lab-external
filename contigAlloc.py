memory = [0] * 50

def allocate_contiguous(start, length):
    if any(memory[start:start + length]):
        print("Memory block not free!")
        return False

    for i in range(start, start + length):
        memory[i] = 1

    print(f"File allocated from block {start} to {start + length - 1}")
    return True

def display_memory():
    print("Memory blocks:", ''.join(map(str, memory)))

if __name__ == "__main__":
    allocate_contiguous(5, 5)
    allocate_contiguous(15, 10)
    display_memory()
