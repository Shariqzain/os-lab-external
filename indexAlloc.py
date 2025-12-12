import random

memory = [0] * 50

def allocate_indexed(index_block, file_blocks):
    if memory[index_block] == 1:
        print("Index block already used!")
        return

    memory[index_block] = 1
    allocated = []

    for _ in range(file_blocks):
        block = random.randint(0, 49)
        while memory[block] == 1:
            block = random.randint(0, 49)

        memory[block] = 1
        allocated.append(block)

    print(f"File allocated with index block {index_block} -> {allocated}")

if __name__ == "__main__":
    allocate_indexed(2, 4)
    allocate_indexed(10, 3)
