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


def water_plant(plant_name: str) -> None:
    if plant_name.capitalize() == plant_name:
        print(f"Watering {plant_name} [OK]")
    else:
        raise PlantError(f"Invalid Plant name to water: '{plant_name}'", 101)


def test_watering_system() -> None:
    print("Testing Valid plants")
    print("Opening watering system")
    plants = ["Lettuce", "Tomato", "Cucumber", "Asparagus"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        return None
    finally:
        print("Closing watering system")
        print("Program part 1 concluded.")
        print("")

    plants = ["Lettuce", "tomato", "Cucumber", "asparagus"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        return None
    finally:
        print("Closing watering system")
        print("Program concluded even with error and returns to main.")


if __name__ == "__main__":
    test_watering_system()
