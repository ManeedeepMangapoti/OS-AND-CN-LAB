def round_robin(n, burst_time, time_slice):
    # Initialize waiting time, turnaround time, remaining burst time, and completion time
    wait_time = [0] * n
    turnaround_time = [0] * n
    remaining_time = burst_time[:]
    time = 0
    complete = [False] * n

    print("Initial Values:")
    print("Burst Time:", burst_time)
    print("Time Slice:", time_slice)
    print("Remaining Time:", remaining_time)
    print()

    while not all(complete):
        for i in range(n):
            if remaining_time[i] > 0:
                if remaining_time[i] > time_slice:
                    # Process the current time slice
                    remaining_time[i] -= time_slice
                    time += time_slice
                else:
                    # Process the remaining time
                    time += remaining_time[i]
                    wait_time[i] = time - burst_time[i]
                    remaining_time[i] = 0
                    complete[i] = True
                
                print(f"Time: {time}, Process {i+1}, Remaining Time: {remaining_time}")

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = burst_time[i] + wait_time[i]

    # Calculate average waiting time and turnaround time
    avg_wait_time = sum(wait_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Print the results
    print("\nThe Average Turnaround time is -- {:.2f}".format(avg_turnaround_time))
    print("The Average Waiting time is -- {:.2f}".format(avg_wait_time))
    print("\n\tPROCESS\t BURST TIME \t WAITING TIME\tTURNAROUND TIME")
    for i in range(n):
        print("\t{}\t {}\t\t {}\t\t {}".format(i+1, burst_time[i], wait_time[i], turnaround_time[i]))

#example output
n=1
burst_time=[2]
time_slice=1
round_robin(n,burst_time,time_slice)
