import perlin
import matplotlib.pyplot as plt

noise=perlin.Perlin()

time=[i*0.01 for i in range(600)]
values=[noise.valueAt(i) for i in time]

plt.title("Perlin Noise")
plt.xlabel("Time")
plt.ylabel("Value")
plt.plot(time, values)
plt.show()

noise.discard(2.2)
values = [noise.valueAt(i) if noise.valueAt(i) else 0 for i in time]
plt.title("Perlin Noise - Discard")
plt.xlabel("Time")
plt.ylabel("Value")
plt.plot(time, values)
plt.show()
