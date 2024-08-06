def priority_scheduling(n, burst_time, priority):
    # Create a list of processes with their burst times and priorities
    processes = list(range(n))
    
    # Sort processes by priority using built-in sort (lower value means higher priority)
    processes.sort(key=lambda x: priority[x])
    sorted_burst_time = [burst_time[i] for i in processes]
    sorted_priority = [priority[i] for i in processes]

    # Initialize waiting time and turnaround time arrays
    wait_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time and turnaround time
    for i in range(1, n):
        wait_time[i] = wait_time[i - 1] + sorted_burst_time[i - 1]
        turnaround_time[i] = wait_time[i] + sorted_burst_time[i]

    # Calculate turnaround time for the first process
    turnaround_time[0] = sorted_burst_time[0]

    # Calculate average waiting time and turnaround time
    avg_wait_time = sum(wait_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Print the results
    print("\nPROCESS\tPRIORITY\tBURST TIME\tWAITING TIME\tTURNAROUND TIME")
    for i in range(n):
        print(f"{processes[i]+1}\t{sorted_priority[i]}\t{sorted_burst_time[i]}\t{wait_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time is --- {avg_wait_time:.2f}")
    print(f"Average Turnaround Time is --- {avg_turnaround_time:.2f}")

# Example usage
n = 3
burst_time = [5, 1, 8]
priority = [3,1,2]
priority_scheduling(n, burst_time, priority)
