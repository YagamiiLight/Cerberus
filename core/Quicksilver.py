from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed



def quicksliver(func,number_process):
    """fixed a big bug on 12.24 Merry Christmas"""

    with ThreadPoolExecutor(max_workers = number_process) as executor:
        futures = [executor.submit(func) for count in range(number_process)]

