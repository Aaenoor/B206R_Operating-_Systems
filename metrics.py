def calculate_metrics(processes):
    total_waiting = 0
    total_turnaround = 0

    for p in processes:
        turnaround = p.completion_time - p.arrival_time
        waiting = turnaround - p.burst_time
        total_turnaround += turnaround
        total_waiting += waiting

    n = len(processes)
    return {
        "Average Waiting Time": total_waiting / n,
        "Average Turnaround Time": total_turnaround / n
    }
