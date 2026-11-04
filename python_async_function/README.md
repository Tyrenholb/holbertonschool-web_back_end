# Python Async Functions

This project explores Python's `asyncio` module: defining coroutines, running
multiple waits concurrently, measuring elapsed time, and scheduling tasks.

## Learning objectives

- Define coroutines with `async def` and retrieve their results with `await`.
- Use `asyncio.sleep()` to wait without blocking the event loop.
- Run coroutines concurrently and collect results with `asyncio.as_completed()`.
- Measure elapsed execution time with `time.perf_counter()`.
- Create scheduled tasks with `asyncio.create_task()`.
- Add type annotations to function parameters and return values.

## Exercises

| File | Function | Purpose |
| --- | --- | --- |
| [0-basic_async_syntax.py](0-basic_async_syntax.py) | `wait_random(max_delay=10)` | Wait for a random delay between zero and `max_delay` seconds, then return that delay as a float. |
| [1-concurrent_coroutines.py](1-concurrent_coroutines.py) | `wait_n(n, max_delay)` | Run `n` random waits concurrently and collect their delays in completion order, producing ascending delays without sorting. |
| [2-measure_runtime.py](2-measure_runtime.py) | `measure_time(n, max_delay)` | Measure the total elapsed time for `wait_n` and return that time divided by `n`. |
| [3-tasks.py](3-tasks.py) | `task_wait_random(max_delay)` | Schedule `wait_random` and return an `asyncio.Task` that the caller can await. |
| [4-tasks.py](4-tasks.py) | `task_wait_n(n, max_delay)` | Run multiple random waits concurrently using `asyncio.as_completed()` and return their delays in completion order. |

`measure_time` is a regular function that starts an event loop with
`asyncio.run()`. Call it outside an already running event loop and use a positive
`n`, since the result is divided by `n`.

`task_wait_random` is also a regular function, but it must be called while an
event loop is running because `asyncio.create_task()` schedules work on that loop.

## Run the examples

Python 3.7 or later is required. All imports use the Python standard library;
no additional packages are needed.

From this directory, run this standalone example in your terminal:

```bash
python3 - <<'PY'
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n
print(asyncio.run(wait_n(5, 2)))
PY
```

It prints five random delays in ascending order. The values change on each run.

The numbered filenames are loaded with `__import__()` because their names cannot
be used in a normal `import` statement. Omit the `.py` extension when importing.

