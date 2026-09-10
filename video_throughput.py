width = int(input("Enter Width: "))
height = int(input("Enter Height: "))
color_depth = int(input("Enter color depth (Bits): "))
fps = int(input("Enter FPS: "))

frame_size = width * height * color_depth 
bit_rate = frame_size * fps
throughput = bit_rate / 10**9

print(f"Frame Size {frame_size:,} bits/frame")
print(f"Bitrate {bit_rate:,} bits/sec")
print(f"Throughput {throughput:.2f} GBps")