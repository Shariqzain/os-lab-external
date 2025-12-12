def fcfs(processes, burst_time, arrival_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    gantt_chart = []
    timeline = []

    order = sorted(range(n), key=lambda i: arrival_time[i])

    t = 0
    for idx in order:
        if t < arrival_time[idx]:
            t = arrival_time[idx]

        gantt_chart.append(processes[idx])
        timeline.append(t)

        waiting_time[idx] = t - arrival_time[idx]
        t += burst_time[idx]
        turnaround_time[idx] = t - arrival_time[idx]

    timeline.append(t)

    print("\nFCFS Scheduling:")
    for i in range(n):
        print(f"{processes[i]}: Waiting={waiting_time[i]}, Turnaround={turnaround_time[i]}")

    print("\nGantt Chart:")
    for p in gantt_chart:
        print(f"| {p} ", end="")
    print("|")

    for time in timeline:
        print(f"{time:>3}", end=" ")
    print()

processes = ["P1", "P2", "P3", "P4"]
burst_time = [5, 3, 8, 6]
arrival_time = [0, 1, 2, 3]
fcfs(processes, burst_time, arrival_time)
