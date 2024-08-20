def main():
    ms = int(input("Enter the total memory available (in Bytes) -- "))
    temp = ms
    mp = []
    n = 0

    while True:
        memory_required = int(input(f"Enter memory required for process {n + 1} (in Bytes) -- "))
        if memory_required <= temp:
            print(f"\nMemory is allocated for Process {n + 1}")
            mp.append(memory_required)
            temp -= memory_required
            n += 1
        else:
            print("\nMemory is Full")
            break

        ch = input("\nDo you want to continue (y/n) -- ").strip().lower()
        if ch != 'y':
            break

    print(f"\n\nTotal Memory Available -- {ms}")
    print("\n\tPROCESS\t\tMEMORY ALLOCATED")
    for i in range(n):
        print(f"\t{i + 1}\t\t{mp[i]}")

    total_allocated = ms - temp
    print(f"\n\nTotal Memory Allocated is {total_allocated}")
    print(f"Total External Fragmentation is {temp}")

if __name__ == "__main__":
    main()
