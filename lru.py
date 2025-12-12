def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    recent_use = {}

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                lru_page = min(memory, key=lambda x: recent_use[x])
                memory.remove(lru_page)
                memory.append(page)
            page_faults += 1

        recent_use[page] = i
        print(f"Page: {page} -> Memory: {memory}")

    print(f"\nTotal Page Faults (LRU): {page_faults}")