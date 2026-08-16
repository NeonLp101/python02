from io import TextIOWrapper


def garden_operations(
    operation_number: int
) -> None | int | str | TextIOWrapper:
    if operation_number == 0:
        return int(("abc"))
    elif operation_number == 1:
        2/0
        return None
    elif operation_number == 2:
        return (open("test.txt", "r"))
    elif operation_number == 3:
        return ("str" + 1 + "str")  # type: ignore
    else:
        return None


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("")
    print("Testing operation 0")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("")
    print("===Testing operation 1===")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print("")
    print("===Testing operation 2===")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print("")
    print("===Testing operation 3===")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    for i in range(0, 4):
        print("")
        print(f"===Testing operation {i}===")
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")


if __name__ == "__main__":
    test_error_types()
    print("")
    print("Programm is still running")
