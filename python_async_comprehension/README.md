# Python Async Comprehension

Practice with async generators, async list comprehensions, and runtime measurement.

## Exercises

[0-async_generator.py](0-async_generator.py): `async_generator` yields 10 random
floats between 0 and 10. It waits one second before each value.

[1-async_comprehension.py](1-async_comprehension.py): `async_comprehension`
collects those 10 values using an async list comprehension and returns the list.

[2-measure_runtime.py](2-measure_runtime.py): `measure_runtime` runs four
comprehensions concurrently with `asyncio.gather()`. It uses `time.time()` to
measure the total runtime in seconds.

Each comprehension takes about 10 seconds. Running four concurrently also takes
about 10 seconds because their waits overlap. The waits within each generator
still happen one after another.

## Run an example

Written for Python 3.8. There are no extra packages to install.
Run this from the project directory:

```bash
python3 - <<'PY'
import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime
print(asyncio.run(measure_runtime()))
PY
```

This prints a runtime of roughly 10 seconds.

Use `__import__()` for the numbered filenames, leaving off `.py`.
