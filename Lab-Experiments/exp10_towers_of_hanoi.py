def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move container 1 from {source} to {destination}")
        return
    towers_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move container {n} from {source} to {destination}")
    towers_of_hanoi(n - 1, auxiliary, source, destination)

num_containers = 3
print(f"Optimal Moves for {num_containers} Containers:")
towers_of_hanoi(num_containers, 'RodA', 'RodB', 'RodC')
