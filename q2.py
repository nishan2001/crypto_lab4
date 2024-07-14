# Python program to exhaust primary memory

# Function to allocate large chunks of memory
def exhaust_memory():
    try:
        memory_blocks = []
        while True:
            memory_blocks.append(' ' * (1024^2 * 1024^2))  # Allocating 1 MB at a time
    except MemoryError:
        print("Memory exhausted")

# Calling the function to exhaust memory
exhaust_memory()
