import time

from observability.logger import log_event, create_trace


def trace(agent_name):

    start = time.time()

    trace_data = create_trace(agent_name)

    print(f"\nRunning agent: {agent_name}")

    return start, trace_data


def end_trace(start, trace_data):

    duration = time.time() - start

    trace_data["latency"] = round(duration, 2)

    log_event(trace_data)

    print(f"Completed in {duration:.2f} seconds")