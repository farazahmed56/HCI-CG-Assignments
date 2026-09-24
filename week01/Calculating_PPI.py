import math 

diagonal = float(input("Enter screen size (inches): "))
width = int(input("Enter horizontal resolution: "))
height = int(input("Enter vertical resolution: "))

diagonal_pixels = math.sqrt(width**2 + height**2)
ppi = diagonal_pixels / diagonal 

print(f"Diagonal Pixel Count: {diagonal_pixels:.2f} pixels")
print(f"PPI: {ppi:.2f}")