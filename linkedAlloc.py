import random

disk = [-1] * 10

def allocate_linked(file_name, n_blocks):
    free_blocks = [i for i, v in enumerate(disk) if v == -1]

    if len(free_blocks) < n_blocks:
        print(f"Not enough space for {file_name}.")
        return

    allocated = random.sample(free_blocks, n_blocks)

    for i in range(n_blocks - 1):
        disk[allocated[i]] = allocated[i + 1]

    disk[allocated[-1]] = -1

    print(f"{file_name} allocated blocks:", ' -> '.join(map(str, allocated)))

if __name__ == "__main__":
    allocate_linked("File1", 4)
    allocate_linked("File2", 3)
    print("Disk pointers:", disk)
