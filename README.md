# python02

42 Heilbronn — Python module 02: exceptions.

Five exercises on error handling, themed around greenhouse temperature and
watering.

| | Topic |
|---|---|
| `ex0` | `try` / `except ValueError` — recovering from bad input without crashing |
| `ex1` | `raise` — enforcing a valid temperature range |
| `ex2` | Handling `ValueError`, `ZeroDivisionError`, `FileNotFoundError` and `TypeError` separately |
| `ex3` | A custom exception hierarchy — `GardenError` with `PlantError` and `WaterError` subclasses, each carrying an error code and a custom `__str__` |
| `ex4` | `finally` — cleanup that runs whether or not an exception fired |

## Running

```
python3 ex3/ft_custom_errors.py
```
