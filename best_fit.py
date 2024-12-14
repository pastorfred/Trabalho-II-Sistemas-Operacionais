def best_fit(filename, mem_size):
    mem = [0] * mem_size
    with open(filename, 'r') as file:
        for line in file:
            if line[0] == 'I':
                proc = line[3] # proc name (A, B, C, etc)
                size = int(''.join(filter(str.isdigit, line)))  # extract integer from line and convert to int
                # find smallest free space that fits the process
                best = (0, mem_size)
                i = 0
                flag = 0
                while i < mem_size:
                    if mem[i] == 0:
                        count = 1
                        while i < mem_size and mem[i] == 0:
                            i += 1
                            count += 1
                        if count-1 >= size and count-1 < best[1]:
                            best = (i - count + 1, count - 1)
                    else:
                        flag += 1
                        i += 1
                if size > best[1]:
                    print("Not enough memory for process " + proc)
                elif flag > 1 and best[1] == mem_size:
                    print("Not enough memory for process " + proc)
                else:
                    for j in range(best[0], best[0] + size):
                        mem[j] = proc
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
        