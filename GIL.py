import threading
import time

def cpu_task():
    print(f"Thread {threading.current_thread().name} starting")
    count = 0
    for _ in range(10**7):
        count += 1
    print(f"Thread {threading.current_thread().name} finished")

# Start time
start = time.time()

# Create 2 threads doing CPU-bound work
t1 = threading.Thread(target=cpu_task, name='A')
t2 = threading.Thread(target=cpu_task, name='B')

t1.start()
t2.start()

t1.join()
t2.join()

# End time
end = time.time()

print(f"Total time with threads: {end - start:.2f} seconds")