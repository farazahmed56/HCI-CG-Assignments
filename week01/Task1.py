import math

Wpx = int(input("Enter horizontal resolution (Pixels): "))
Hpx = int(input("Enter vertical resolution (Pixels): "))
Dinches = float(input("Enter physical diagonal size (inches): "))

total_pixels = Wpx * Hpx

gcd = math.gcd(Wpx, Hpx)
aspect_width = Wpx // gcd 
aspect_height = Hpx // gcd

diagonal_pixels = math.sqrt(Wpx**2 + Hpx**2)

dpi = diagonal_pixels / Dinches 

if dpi < 100:
    density = "Low Density (Standard Monitor)"
elif dpi <= 200: 
    density = "Medium Density (HD Display)"
else: 
    density = "High Density (Retina / Mobile)"

print("\n---DISPLAY METRICS ANALYSIS---")
print(f"Total Pixel Count : {total_pixels:,} pixels")
print(f"Aspect Ratio : {aspect_width}:{aspect_height}")
print(f"Calculated DPI : {dpi:.2f} DPI")
print(f"Density Category : {density}")