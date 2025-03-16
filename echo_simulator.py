import numpy as np
import matplotlib.pyplot as plt
from radar_simulator import generate_pulse

def simulate_echo(pulse, delay_samples):
    """
    Simulates the reflected echo signal by delaying the transmitted pulse.

    Parameters:
    - pulse: The original transmitted pulse (numpy array).
    - delay_samples: Number of samples to delay the echo.

    Returns:
    - Echo signal (numpy array).
    """
    echo = np.zeros_like(pulse)
    echo[delay_samples:] = pulse[:-delay_samples]
    return echo

if __name__ == "__main__":
    # Generate the radar pulse
    t, pulse = generate_pulse()

    # Simulate a reflected echo with a delay
    delay_samples = 100  # Delay in samples (equivalent to a target distance)
    echo = simulate_echo(pulse, delay_samples)

    # Plot the transmitted and reflected signals
    plt.plot(t, pulse, label="Transmitted Pulse")
    plt.plot(t, echo, label="Reflected Echo")
    plt.legend()
    plt.title("Radar Echo Simulation")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()
