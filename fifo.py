from collections import deque

def fifo_page_replacement(pages, capacity):
    page_faults = 0
    memory = deque()          # main memory (queue)
    in_memory = set()         # helper set for quick lookup

    for page in pages:
        if page not in in_memory:       # page not found → page fault
            page_faults += 1

            if len(memory) == capacity:  # memory is full → remove oldest page
                removed = memory.popleft()
                in_memory.remove(removed)

            memory.append(page)          # add new page to memory
            in_memory.add(page)          # mark it as loaded

    return page_faults

# Example:
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
capacity = 3
print("FIFO Page Faults:", fifo_page_replacement(pages, capacity))