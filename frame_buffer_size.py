width = int(input("Enter width (pixels): "))
height = int(input("Enter height (pixels): "))
color_bits = int(input("Enter color depth (bits): "))

pixels = width * height

#converting bits to bytes
bytes_per_pixel = color_bits / 8

total_bytes = pixels * bytes_per_pixel

#convertig bytes to Mb
total_mb = total_bytes / (1024**2)

print("\nTotal Pixels: ", pixels)
print("Bytes per Pixel: ", bytes_per_pixel)
print("Total Memory:", total_bytes, "bytes")
print(f"Frame Buffer Size:{total_mb:.2f}MB")
