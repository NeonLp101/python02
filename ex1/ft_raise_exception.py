def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        print(f"Success temp is now {temp}°C")
        return temp


def test_temperature() -> None:
    for data in ["25", "100", "-1", "0", "50", "abc"]:
        print(f"Input data is '{data}'")
        try:
            input_temperature(data)
        except ValueError as e:
            print(f"Caught error with input_temperature: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
