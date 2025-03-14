def calculate_distance(time_delay, speed_of_light=3e8):
    """
    Calculates the target distance based on the time delay.

    Parameters:
    - time_delay: Round-trip time delay of the reflected signal (in seconds).
    - speed_of_light: Speed of light (default: ~3x10^8 m/s).

    Returns:
    - Target distance (in meters).

    """
    return (speed_of_light * time_delay) / 2

if __name__ == "__main__":
    time_delay = 2e-6  # Example: 2 microseconds delay
    distance = calculate_distance(time_delay)
    print(f"Target Distance: {distance:.2f} m")
