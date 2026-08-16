class GardenError(Exception):
    def __init__(
        self, message: str = "Unknown garden error", error_code: int = 1
    ) -> None:
        self.message = message
        super().__init__(self.message)
        self.error_code = error_code

    def __str__(self) -> str:
        return f"{self.message} (Error Code: {self.error_code})"


class PlantError(GardenError):
    def __init__(
        self, message: str = "Unknown plant error", error_code: int = 2
    ) -> None:
        super().__init__(message, error_code)


class WaterError(GardenError):
    def __init__(
        self, message: str = "Unknown water error", error_code: int = 3
    ) -> None:
        super().__init__(message, error_code)


def test_errors() -> None:
    TomatoHP = 3
    WaterLevel = 20
    print("=== Custom Garden Errors Demo ===")
    print("")
    print("Testing Custom Water Error")
    try:
        if WaterLevel > 50:
            return None
        else:
            raise WaterError("Water level is way too low!", 300)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
        print("")
    print("Testing Custom Plant Error")
    try:
        if TomatoHP > 10:
            return None
        else:
            raise PlantError("The Tomato is wilting!", 200)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("")
        print("Testing Custom Garden Error")
    try:
        if TomatoHP > 10:
            return None
        else:
            raise PlantError("The Tomato is wilting!", 200)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        if WaterLevel > 50:
            return None
        else:
            raise WaterError("Water level is way too low!", 300)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("")
    print("Program executed flawlessly")


if __name__ == "__main__":
    test_errors()
