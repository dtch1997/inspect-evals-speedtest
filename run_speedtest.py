from inspect_ai import eval
from inspect_evals_speedtest.gpqa import gpqa_diamond
from inspect_evals_speedtest.config import env_vars # noqa: F401
from inspect_evals_speedtest.utils import time_execution

@time_execution
def run_speedtest():
    eval(
        [gpqa_diamond()],
        model="openai/gpt-4o",
        max_retries=5,
        max_connections=1000,
        timeout=120,
    )
    
if __name__ == "__main__":
    run_speedtest()