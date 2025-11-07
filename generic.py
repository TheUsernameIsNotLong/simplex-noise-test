"""Utility functions for getting user input with default values."""

def get_int(prompt: str, default: int) -> int:
    """Get an integer input from the user, with a default value."""
    value = input(prompt)
    if value.strip() == "":
        return default
    try:
        return int(value)
    except ValueError:
        print(f"Invalid input. Using default value of {default}.")
        return default

def get_float(prompt: str, default: float) -> float:
    """Get a float input from the user, with a default value."""
    value = input(prompt)
    if value.strip() == "":
        return default
    try:
        return float(value)
    except ValueError:
        print(f"Invalid input. Using default value of {default}.")
        return default
