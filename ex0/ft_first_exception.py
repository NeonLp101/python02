def input_temperature(temp_str: str) -> int | None:
    try:
        return int(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return None


def test_temperature() -> None:
    input_temperature("abc")
    print("Program still running")
    input_temperature("20")
    print(f"Temperature is {input_temperature('36')}°C")
    print("Program still running")


if __name__ == "__main__":
    test_temperature()
