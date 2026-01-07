from process import Process
from scheduler import fcfs, sjf, round_robin
from memory import MemoryManager
from metrics import calculate_metrics


def main():
    processes = [
        Process(1, 0, 5, 100),
        Process(2, 1, 3, 120),
        Process(3, 2, 8, 80)
    ]

    memory = MemoryManager(total_memory=500)

    admitted = []
    for p in processes:
        if memory.first_fit(p):
            admitted.append(p)

    print("Select Scheduling Algorithm:")
    print("1. FCFS")
    print("2. SJF")
    print("3. Round Robin")

    choice = input("Enter choice: ")

    if choice == "1":
        completed = fcfs(admitted)
    elif choice == "2":
        completed = sjf(admitted)
    elif choice == "3":
        completed = round_robin(admitted, quantum=2)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        return
    metrics = calculate_metrics(completed)
    print("\nProcess Execution Order:")
    for p in completed:
        print(f"Process {p.pid}: Start={p.start_time}, Completion={p.completion_time}")

    print("\nSystem Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v:.2f}")

    print(f"Memory Utilization: {memory.utilization():.2f}%")

if __name__ == "__main__":
    main()