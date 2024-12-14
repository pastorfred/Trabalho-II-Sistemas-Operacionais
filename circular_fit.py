def circular_fit(filename, mem_size):
    mem = [0] * mem_size
    last_position = 0 
    with open(filename, 'r') as file:
        for line in file:
            if line[0] == 'I':
                proc = line[3]
                size = int(''.join(filter(str.isdigit, line)))
                found = False
                for i in range(mem_size):
                    pos = (last_position + i) % mem_size
                    if mem[pos] == 0:
                        if all(mem[(pos + j) % mem_size] == 0 for j in range(size)):
                            for j in range(size):
                                mem[(pos + j) % mem_size] = proc
                            last_position = (pos + size) % mem_size
                            found = True
                            break
                if not found:
                    print("Not enough memory for process " + proc)
            elif line[0] == 'O':
                proc = line[4]
                while proc in mem:
                    mem[mem.index(proc)] = 0
            else:
                raise ValueError("Invalid input file")
            
            # Visualização do estado atual da memória
            string = line.strip() + " -> " + str(mem)
            print(string)
    return 0
