import math

def calculate_volume_of_sphere(radius):
    return (4 / 3) * math.pi * (radius ** 3)

# Taking user input
radius = float(input("Enter the radius of the sphere: "))

# Calculating volume
volume = calculate_volume_of_sphere(radius)

# Displaying result
print(f"Volume of the sphere: {volume}")
#op
# Enter the radius of the sphere: 4
# Volume of the sphere: 268.082573106329