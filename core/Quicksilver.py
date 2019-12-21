from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from core.requester import requester


def quicksliver(func,number_process):

    with ThreadPoolExecutor(max_workers = number_process) as executor:
        futures = [executor.submit(func) for count in range(number_process)]
        for future in as_completed(futures):
            future.result()
