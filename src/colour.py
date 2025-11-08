"""Module for handling colour gradients and mapping noise values to colours."""

from math import floor, ceil
from rich.console import Console
from generic import get_int

console = Console()

def determine_gradient_points(num_points: int):
    """Determine key gradient colours for noise mapping."""
    gradient_points = []
    # Loop to get RGB values for each gradient point
    for i in range(num_points):
        r = get_int(f"Enter red value (0-255) of point {i+1}/{num_points}: ", 255)
        g = get_int(f"Enter green value (0-255) of point {i+1}/{num_points}: ", 255)
        b = get_int(f"Enter blue value (0-255) of point {i+1}/{num_points}: ", 255)
        console.print(f"Gradient point {i + 1} set.", style=f"rgb({r},{g},{b})")
        gradient_points.append([r, g, b])
    return gradient_points

def new_colourise_value(value: float, gradient: list) -> str:
    """Convert a noise value to a colored string for terminal output."""
    # Clamp value between -1 and 1
    clamped_value = max(-1, min(1, value))
    # Map value to a range encompassing all gradient points
    mapped_value = (len(gradient)*(clamped_value + 1)) / 2
    # Interpolate colour from custom values
    lower_colour = gradient[floor(mapped_value)-1] #127, 255, 0
    upper_colour = gradient[ceil(mapped_value)-1] #255, 0, 0

    modulo_value = mapped_value % 1
    r = int(lower_colour[0] + (upper_colour[0] - lower_colour[0]) * modulo_value)
    g = int(lower_colour[1] + (upper_colour[1] - lower_colour[1]) * modulo_value)
    b = int(lower_colour[2] + (upper_colour[2] - lower_colour[2]) * modulo_value)
    return f"rgb({r},{g},{b})"
