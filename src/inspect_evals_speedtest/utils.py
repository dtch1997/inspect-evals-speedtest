import time
import functools
from typing import Callable, Any
from loguru import logger


def time_execution(func: Callable) -> Callable:
    """
    Decorator to time the execution of a function.
    
    Args:
        func: The function to be timed
        
    Returns:
        Wrapped function that prints execution time
        
    Example:
        @time_execution
        def my_function():
            time.sleep(1)
            return "done"
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            logger.info(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
    
    return wrapper


if __name__ == "__main__":
    # Sanity check for the timing decorator
    import time
    
    @time_execution
    def quick_function():
        """A quick function for testing."""
        time.sleep(0.1)
        return "Quick function completed"
    
    @time_execution
    def slow_function():
        """A slower function for testing."""
        time.sleep(0.5)
        return "Slow function completed"
    
    @time_execution
    def function_with_args(x, y, z=10):
        """A function with arguments for testing."""
        time.sleep(0.2)
        return f"Result: {x + y + z}"
    
    print("Testing timing decorator...")
    print()
    
    # Test basic functionality
    result1 = quick_function()
    print(f"Returned: {result1}")
    print()
    
    # Test with different timing
    result2 = slow_function()
    print(f"Returned: {result2}")
    print()
    
    # Test with arguments
    result3 = function_with_args(5, 3, z=2)
    print(f"Returned: {result3}")
    print()
    
    print("All tests completed successfully!")
