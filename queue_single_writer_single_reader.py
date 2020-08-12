import queue
import random
import threading
import time

import pandas as pd

NUMBER_OF_EVENTS = 100000
BATCH_SIZE_TO_USE_IN_TPS_CALCULATION = 10000


def event_producer(number_of_events):
    event_counter = 0
    while True:
        event_data = {"time": time.time(), "obs_id": random.randint(1, 30), "throughput": random.randint(1, 5000)}
        event_counter = event_counter + 1
        event_queue.put(event_data)
        if event_counter == number_of_events:
            event_queue.task_done()
            break


def event_taker(tps_calculation_batch_size, number_of_events):
    start_time = time.time();
    event_batch_count = 0
    total_event_count = 0
    tps_values = {}
    sum_time = 0
    while True:
        item = event_queue.get()
        event_batch_count = event_batch_count + 1
        total_event_count = total_event_count + 1
        if event_batch_count == tps_calculation_batch_size:
            end_time = time.time();
            sum_time = (end_time - start_time + sum_time)
            tps_values[round((sum_time * 1000), 2)] = round(get_tps(tps_calculation_batch_size, end_time, start_time),2)
            start_time = end_time
            event_batch_count = 0
        if total_event_count == number_of_events:
            tps_data_frame = pd.DataFrame(tps_values.items(), columns=['Time (ms)', 'TPS (requests/second)'])
            tps_data_frame.to_csv("single-queue-single-reader.csv", encoding='utf-8', index=False)
            print(tps_data_frame)
            break


def get_tps(tps_calculation_batch_size, end_time, start_time):
    return tps_calculation_batch_size / (end_time - start_time)


event_queue = queue.Queue()
threading.Thread(target=event_taker, args=(BATCH_SIZE_TO_USE_IN_TPS_CALCULATION, NUMBER_OF_EVENTS,),
                 daemon=True).start()

threading.Thread(target=event_producer, args=(NUMBER_OF_EVENTS,), daemon=True).start()


event_queue.join()
