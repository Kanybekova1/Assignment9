from shape3d import Shape3D
from sphere import Sphere
from cylinder import Cylinder
from cube import Cube
import random

shapes = []
for _ in range(10):
    shape_type = random.choice(["Sphere", "Cylinder", "Cube"])
    if shape_type == "Sphere":
        r = random.randint(1, 10)
        shapes.append(Sphere(r))
    elif shape_type == "Cylinder":
        r = random.randint(1, 10)
        h = random.randint(5, 20)
        shapes.append(Cylinder(r, h))
    else:
        a = random.randint(1, 10)
        shapes.append(Cube(a))

for i, shape in enumerate(shapes, start=1):
    print(f"Shape {i}: {shape}")
    print(f"  Surface Area: {shape.surface_area():.2f}")
    print(f"  Volume: {shape.volume():.2f}\n")

