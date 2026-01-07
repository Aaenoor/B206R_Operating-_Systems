import matplotlib.pyplot as plt

algorithms = ['FCFS', 'SJF', 'Round Robin']
avg_waiting = [3.33, 3.33, 6.00]
avg_turnaround = [8.67, 8.67, 11.33]

plt.figure()
plt.bar(algorithms, avg_waiting)
plt.xlabel("Scheduling Algorithm")
plt.ylabel("Average Waiting Time")
plt.title("Average Waiting Time Comparison")
plt.show()

plt.figure()
plt.bar(algorithms, avg_turnaround)
plt.xlabel("Scheduling Algorithm")
plt.ylabel("Average Turnaround Time")
plt.title("Average Turnaround Time Comparison")
plt.show()
