import numpy as np
import matplotlib.pyplot as plt

from distance_calculator import calculate_distance

def generate_pulse(frequency=1e6, duration=1e-6, sampling_rate=1e9):
    t = np.arange(0, duration, 1 / sampling_rate)
    pulse = np.sin(2 * np.pi * frequency * t)
    return t, pulse

t, pulse = generate_pulse()
plt.plot(t, pulse)
plt.title("Radar Pulse Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

#calculate the distance
time_delay = 2e-6  
distance = calculate_distance(time_delay)
print(f"Target Distance: {distance:.2f} m")