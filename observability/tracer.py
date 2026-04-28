import time


def trace(agent_name):

    start = time.time()

    print(f"\nRunning agent: {agent_name}")

    return start


def end_trace(start):

    duration = time.time() - start

    print(f"Completed in {duration:.2f} seconds")