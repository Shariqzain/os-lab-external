def sjf_non_preemptive(processes, burst_time, arrival_time):
    n = len(processes)
    completed = [False] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    gantt_chart = []
    timeline = []

    t = 0
    completed_count = 0

    while completed_count < n:
        idx = -1
        minm = float('inf')
        for i in range(n):
            if arrival_time[i] <= t and not completed[i]:
                if burst_time[i] < minm:
                    minm = burst_time[i]
                    idx = i

        if idx == -1:
            t += 1
            continue

        gantt_chart.append(processes[idx])
        timeline.append(t)

        t += burst_time[idx]
        completed[idx] = True
        completed_count += 1

        turnaround_time[idx] = t - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]

    timeline.append(t)

    print("\nNon-Preemptive SJF Scheduling:")
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
burst_time = [6, 8, 7, 3]
arrival_time = [0, 1, 2, 3]
sjf_non_preemptive(processes, burst_time, arrival_time)
