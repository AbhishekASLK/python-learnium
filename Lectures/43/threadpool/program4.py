import concurrent.futures

def work():
    for _ in range(10000):
        print('work')

pool = concurrent.futures.ThreadPoolExecutor(20)
pool.submit(work)
pool.shutdown(wait=False)

print('Main Thread')