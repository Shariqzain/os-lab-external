def bankers_algorithm(n_processes, n_resources, allocation, maximum, available):
    need = []
    for i in range(n_processes):
        row = []
        for j in range(n_resources):
            row.append(maximum[i][j] - allocation[i][j])
        need.append(row)

    finish = [False] * n_processes
    safe_sequence = []
    work = []
    for r in available:
        work.append(r)

    print("\nNeed Matrix:")
    for i in range(n_processes):
        print(f"P{i}:", need[i])

    while len(safe_sequence) < n_processes:
        executed = False
        for i in range(n_processes):
            if not finish[i]:
                can_allocate = True
                for j in range(n_resources):
                    if need[i][j] > work[j]:
                        can_allocate = False
                        break

                if can_allocate:
                    for j in range(n_resources):
                        work[j] += allocation[i][j]

                    finish[i] = True
                    safe_sequence.append(i)
                    executed = True
                    break

        if not executed:
            print("\nSystem is in an UNSAFE state! Deadlock may occur.")
            return

    print("\nSystem is in a SAFE state.")
    print("Safe Sequence:", " → ".join(f"P{p}" for p in safe_sequence))


# Input Data
n_processes = 5
n_resources = 3

allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

available = [3, 3, 2]

# Run Banker’s Algorithm
bankers_algorithm(n_processes, n_resources, allocation, maximum, available)
