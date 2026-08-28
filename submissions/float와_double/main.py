import struct
PI = 3.14159265359
r = 5.0
f = struct.unpack('f', struct.pack('f', struct.unpack('f', struct.pack('f', r))[0] * struct.unpack('f', struct.pack('f', r))[0] * struct.unpack('f', struct.pack('f', PI))[0]))[0]
d = r * r * PI
print(f"원의 면적 (float): {f:.7f}")
print(f"원의 면적 (double): {d:.12f}")