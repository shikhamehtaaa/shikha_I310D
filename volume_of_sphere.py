def calculate_volume_of_sphere(radius):
	pi = 3.14
	volume = pi * radius * radius * radius * 4/3
	return volume

radius1 = 30
volume1 = calculate_volume_of_sphere(radius1)
print(f"The volume of the sphere with radius {radius1} is: {volume1}")

radius2 = 40
volume2 = calculate_volume_of_sphere(radius2)
print(f"The volume of the sphere with radius {radius2} is: {volume2}")
