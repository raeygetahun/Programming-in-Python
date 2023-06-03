import matplotlib.pyplot as plt

with open("data.dat", "w") as file:
    for x in range(-20, 21):
        file.write(f"{x} {x**3}\n")

x_values = []
y_values = []
with open("data.dat", "r") as file:
    for line in file:
        x, y = line.strip().split()
        x_values.append(int(x))
        y_values.append(int(y))

plt.plot(x_values, y_values)
plt.xlabel("x")
plt.ylabel("x^3")
plt.title("x and x^3")
plt.grid(True)
plt.savefig("output.pdf")
plt.show()
