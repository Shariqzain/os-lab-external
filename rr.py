def round_robin(processes, burst_time, arrival_time, quantum):
    n = len(processes)
    rem_bt = burst_time[:]
    t = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n

    gantt_chart = []
    timeline = []

    while True:
        done = True

        for i in range(n):
            if rem_bt[i] > 0 and arrival_time[i] <= t:
                gantt_chart.append(processes[i])
                timeline.append(t)

                done = False

                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    waiting_time[i] = t - burst_time[i] - arrival_time[i]
                    rem_bt[i] = 0

        if done:
            break

    timeline.append(t)

    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    print("\nRound Robin Scheduling:")
    for i in range(n):
        print(f"{processes[i]}: Waiting={waiting_time[i]}, Turnaround={turnaround_time[i]}")

    print("\nGantt Chart:")
    for p in gantt_chart:
        print(f"| {p} ", end="")
    print("|")

    for time in timeline:
        print(f"{time:>3}", end=" ")
    print()


processes = ["P1", "P2", "P3"]
burst_time = [5, 4, 2]
arrival_time = [0, 1, 2]
quantum = 2
round_robin(processes, burst_time, arrival_time, quantum)
