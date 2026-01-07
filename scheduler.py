from collections import deque

def fcfs(processes):
    time = 0
    completed = []

    for p in sorted(processes, key=lambda x: x.arrival_time):
        if time < p.arrival_time:
            time = p.arrival_time
        p.start_time = time
        time += p.burst_time
        p.completion_time = time
        completed.append(p)

    return completed


def sjf(processes):
    time = 0
    completed = []
    ready = processes.copy()

    while ready:
        available = [p for p in ready if p.arrival_time <= time]
        if not available:
            time += 1
            continue

        p = min(available, key=lambda x: x.burst_time)
        p.start_time = time
        time += p.burst_time
        p.completion_time = time
        completed.append(p)
        ready.remove(p)

    return completed


def round_robin(processes, quantum):
    time = 0
    queue = deque(processes)
    completed = []

    while queue:
        p = queue.popleft()

        if p.start_time is None:
            p.start_time = max(time, p.arrival_time)

        exec_time = min(quantum, p.remaining_time)
        time += exec_time
        p.remaining_time -= exec_time

        if p.remaining_time == 0:
            p.completion_time = time
            completed.append(p)
        else:
            queue.append(p)

    return completed
