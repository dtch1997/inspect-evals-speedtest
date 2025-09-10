import itertools
import pandas as pd

from inspect_ai import eval
from inspect_evals_speedtest.gpqa import gpqa_diamond
from inspect_evals_speedtest.config import env_vars # noqa: F401
from inspect_evals_speedtest.utils import time_execution

def run_speedtest(
    max_retries: int = 5,
    max_connections: int = 1000,
    timeout: int = 120,
):
    wrapped_eval = time_execution(eval)
    _, execution_time = wrapped_eval(
        [gpqa_diamond()],
        model="openai/gpt-4o",
        max_retries=max_retries,
        max_connections=max_connections,
        timeout=timeout,
    )
    return execution_time
    
if __name__ == "__main__":
    
    connections_values = [
        100, 1000, 10000
    ]
    retries = [5]
    timeout = [120]

    data = []
    for (retries, connections, timeout) in itertools.product(retries, connections_values, timeout):
        execution_time = run_speedtest(max_retries=retries, max_connections=connections, timeout=timeout)
        data.append({
            "retries": retries,
            "connections": connections,
            "timeout": timeout,
            "execution_time": execution_time,
        })
    
    df = pd.DataFrame(data)
    df.to_csv("speedtest_data.csv", index=False)