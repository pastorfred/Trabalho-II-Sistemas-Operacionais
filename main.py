from first_fit import first_fit
from best_fit import best_fit
from worst_fit import worst_fit
from circular_fit import circular_fit 

def main():
    filename = input("Enter the filename: ")
    mem_size = int(input("Enter the power of 2 for the memory size: "))
    mem_size = 2 ** mem_size
    choice = input("Enter the algorithm (first, best, worst, circular): ")
    if choice == "first":
        first_fit(filename, mem_size)
    elif choice == "best":
        best_fit(filename, mem_size)
    elif choice == "worst":
        worst_fit(filename, mem_size)
    elif choice == "circular":  # Adicionar opção para Circular-Fit
        circular_fit(filename, mem_size)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
