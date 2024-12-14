def first_fit(filename, mem_size):
    mem = [0] * mem_size
    with open(filename, 'r') as file:
        for line in file:
            if line[0] == 'I':
                proc = line[3] # proc name (A, B, C, etc)
                size = int(''.join(filter(str.isdigit, line)))  # extract integer from line and convert to int
                # find first free space that fits the process
                done = False
                counter = 0
                i = 0
                while i < mem_size and done == False:
                    if mem[i] == 0:
                        i += 1
                        counter += 1
                    else:
                        i += 1
                        counter = 0
                    if counter == size:
                        for j in range(i - counter, i):
                            mem[j] = proc
                        done = True
                if counter < size:
                    print("Not enough memory for process " + proc)
            elif line[0] == 'O':
                proc = line[4]
                while proc in mem:
                    mem[mem.index(proc)] = 0
            else:
                raise ValueError("Invalid input file")
            
            string = line.strip() + " -> " + str(mem)
            print(string)
            string = "Free Memory Blocks -> "
            count = 0
            for i in range(mem_size):
                if mem[i] == 0:
                    count += 1
                else:
                    if count > 0:
                        string += "| " + str(count) + " | "
                    count = 0
            if count > 0:
                string += "| " + str(count) + " | "
            print(string)
            print("Press any key to continue...")
            input()
    return 0
        