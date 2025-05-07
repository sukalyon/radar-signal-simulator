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
    
    if delay_samples == 0:
        print("Warning: Delay is zero, no echo shift applied.")
        return echo  # Boş dönüş yap
    
    if delay_samples >= len(pulse):
        print(f"Warning: Delay ({delay_samples}) exceeds pulse length ({len(pulse)}). Clipping to max length.")
        delay_samples = len(pulse) - 1
    
    echo[delay_samples:] = pulse[:-delay_samples]
    return echo

if __name__ == "__main__":
    t, pulse = generate_pulse()

    # Simulate echoes from multiple targets
    targets = [50, 150, 300]  # Target distances in meters
    sampling_rate = 1e9
    time_per_sample = 1 / sampling_rate

    # Calculate the delay in samples for each target
    delays = [round((2 * d) / (3e8 * time_per_sample)) for d in targets]
    
    # Log delay values
    for i, d in enumerate(targets):
        print(f"Target at {d}m -> Delay Samples: {delays[i]}")

    # Generate echoes for each target
    echoes = [simulate_echo(pulse, d) for d in delays]

    # Visualize the transmitted pulse and echoes
    plt.plot(t, pulse, label="Transmitted Pulse")
    for i, echo in enumerate(echoes):
        plt.plot(t, echo, label=f"Echo from {targets[i]} m")

    plt.legend()
    plt.title("Multiple Target Echoes")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()
