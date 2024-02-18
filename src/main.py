import concurrent.futures
import random


def execute_microtask(task_id, microtask_input):
    # Simulate microtask work, returning task_id for aggregation

    # Generate a workload between 100,000 and 100,000,000
    workload = max(100000, round(random.random() * 100000000))

    print("Task #{} started with workload {}".format(task_id, workload))

    # Simulate the workload
    for _ in range(workload):
        pass

    print("Task #{} completed".format(task_id))

    # Return the task ID and the result of the microtask
    return task_id, microtask_input * 2


def map_reduce(tasks):
    # Flatten tasks list to a list of (task_id, microtask_input) tuples
    microtasks = [
        (task_id, microtask) for task_id, task in enumerate(tasks) for microtask in task
    ]

    # Initialize a dictionary to collect results for each task
    task_results = {}
    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        # Submit all microtasks for execution
        future_to_microtask = {
            executor.submit(execute_microtask, task_id, mt): (task_id, mt)
            for task_id, mt in microtasks
        }

        for future in concurrent.futures.as_completed(future_to_microtask):
            task_id, result = future.result()
            # Aggregate results by task_id
            if task_id not in task_results:
                task_results[task_id] = []
            task_results[task_id].append(result)

    # Reduce microtask results within each task and combine for final result
    final_result = sum(
        reduce_microtasks_results(results) for results in task_results.values()
    )
    return final_result


def reduce_microtasks_results(microtask_results):
    # Reduce microtask results for a single task
    return sum(microtask_results)


if __name__ == "__main__":
    tasks = [
        [1, 2, 3, 4],  # Task with 4 microtasks
        [5, 6],  # Task with 2 microtasks
        [7, 8, 9],  # Task with 3 microtasks
    ] * 25  # Simulate 100 tasks

    final_result = map_reduce(tasks)
    print("Final Result:", final_result)
