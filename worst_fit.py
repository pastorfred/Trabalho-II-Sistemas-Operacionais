def worst_fit(filename, mem_size):
    mem = [0] * mem_size
    with open(filename, 'r') as file:
        for line in file:
            if line[0] == 'I':
                proc = line[3] # proc name (A, B, C, etc)
                size = int(''.join(filter(str.isdigit, line)))  # extract integer from line and convert to int
                # find biggest free space that fits the process
                worst = (0, 0)
                for i in range(mem_size):
                    aux = (0, 0)
                    if mem[i] == 0:
                        aux = (i, 1)
                        for j in range(i+1, mem_size):
                            if mem[j] == 0:
                                aux = (i, aux[1] + 1)
                            else:
                                break
                    if aux[1] > worst[1]:
                        worst = aux
                if worst[1] >= size:
                    for j in range(size):
                        mem[worst[0]+j] = proc
                else:
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
        