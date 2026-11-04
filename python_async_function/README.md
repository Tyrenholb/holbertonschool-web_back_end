# Python Async Functions

This project uses Python's `asyncio` module to run coroutines concurrently,
measure runtime, and create tasks. It also covers `async` and `await`,
non-blocking waits, and type annotations.

## Exercises

[0-basic_async_syntax.py](0-basic_async_syntax.py) defines
`wait_random(max_delay=10)`. It waits for a random delay between zero and
`max_delay` seconds and returns the delay as a float.

[1-concurrent_coroutines.py](1-concurrent_coroutines.py) defines
`wait_n(n, max_delay)`. It runs `n` random waits concurrently and collects their
delays in completion order, giving ascending results without sorting.

[2-measure_runtime.py](2-measure_runtime.py) defines
`measure_time(n, max_delay)`. It measures how long `wait_n` takes to run using
`time.perf_counter()` and returns the elapsed time divided by `n`.

[3-tasks.py](3-tasks.py) defines `task_wait_random(max_delay)`. It schedules
`wait_random` with `asyncio.create_task()` and returns the task for the caller
to await.

[4-tasks.py](4-tasks.py) defines `task_wait_n(n, max_delay)`. It runs multiple
random waits concurrently using `asyncio.as_completed()` and returns the delays
in completion order.

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

