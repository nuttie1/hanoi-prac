import time

move_count = 0


def move(n, source, target):
    global move_count
    move_count += 1

    print(f"Move disk {n} from {source} to {target}")
    print(f"")


def hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        hanoi(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")
        target.append(source.pop())
        move(n, source, target)

        # Move the n - 1 disks that we left on auxiliary to target
        hanoi(n - 1, auxiliary, target, source)


# Driver code
n = 3
source = [i for i in range(n, 0, -1)]
target = []
auxiliary = []

start_time = time.time()
hanoi(n, source, target, auxiliary)
end_time = time.time()

print(f"\nExecution time: {end_time - start_time} seconds")
print(f"Total moves: {move_count}")
