# Python Async Functions

Practice with `async`, `await`, and Python's `asyncio` module.

## Exercises

[0-basic_async_syntax.py](0-basic_async_syntax.py): `wait_random` waits for a
random delay between zero and `max_delay` seconds, then returns the delay.
The default maximum is 10 seconds.

[1-concurrent_coroutines.py](1-concurrent_coroutines.py): `wait_n` runs `n`
random waits concurrently. It collects the delays as they finish, so they arrive
in ascending order without sorting.

[2-measure_runtime.py](2-measure_runtime.py): `measure_time` times a call to
`wait_n` with `time.perf_counter()` and returns the total time divided by `n`.

[3-tasks.py](3-tasks.py): `task_wait_random` creates a task from `wait_random`
and returns it for the caller to await.

[4-tasks.py](4-tasks.py): `task_wait_n` runs multiple random waits and collects
their results with `asyncio.as_completed()`.

`measure_time` is a regular function that starts an event loop with
`asyncio.run()`. Call it outside an already running event loop and use a positive
`n`, since the result is divided by `n`.

`task_wait_random` is also a regular function, but it must be called while an
event loop is running because `asyncio.create_task()` schedules work on that loop.

## Run the examples

Requires Python 3.7 or later. There are no extra packages to install.

Run this from the project directory:

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

