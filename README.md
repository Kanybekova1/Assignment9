# 3D Shape Abstraction in Python

This project demonstrates the concept of **abstraction** and **polymorphism** in Python using an abstract base class `Shape3D` for 3D shapes.

## Features

- Abstract base class with abstract `surface_area()`  and `volume()` methods.
- Implemented subclasses:
  - `Sphere`
  - `Cylinder`
  - `Cube`
- Random generation of 3D shapes and dimensions.
- Calculation and display of surface area and volume for each shape.

The abstract base class `Shape3D` defines a blueprint for all 3D shapes. It enforces that any subclass must implement:

`surface_area()`

`volume()`

This ensures consistency: no matter what shape we're working with—`Sphere`, `Cylinder`, or `Cube`we know it will have these two methods.


## Usage Example 
### Output Examples
``` 
Shape 1: <cylinder.Cylinder object at 0x000002359808B590>
  Surface Area: 263.89
  Volume: 311.02

Shape 2: <cylinder.Cylinder object at 0x0000023598088200>
  Surface Area: 119.38
  Volume: 56.55

Shape 3: <cube.Cube object at 0x0000023598088230>
  Surface Area: 486.00
  Volume: 729.00

Shape 4: <cylinder.Cylinder object at 0x000002359808AAB0>
  Surface Area: 955.04
  Volume: 2211.68

Shape 5: <cube.Cube object at 0x000002359809DB50>
  Surface Area: 486.00
  Volume: 729.00

Shape 6: <cylinder.Cylinder object at 0x000002359809DBE0>
  Surface Area: 942.48
  Volume: 2148.85

Shape 7: <cylinder.Cylinder object at 0x000002359809DC40>
  Surface Area: 1130.97
  Volume: 2513.27

Shape 8: <sphere.Sphere object at 0x000002359809E3F0>
  Surface Area: 1017.88
  Volume: 3053.63

Shape 9: <sphere.Sphere object at 0x000002359809E450>
  Surface Area: 615.75
  Volume: 1436.76

Shape 10: <cube.Cube object at 0x000002359809E480>
  Surface Area: 150.00
  Volume: 125.00 ```
