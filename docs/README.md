
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# General Description of the Solution
## `calculate.py`
### `def calc(fig, func, size)`:
- This file calculates the value of a function based on the choice of shape (square or circle), the operation to be calculated (perimeter or area), and its size.
- Example: Input: `calc("square", "area", [4])`; Output: 16 (the area of a square with a side length of 4).
  
## `circle.py`
### `def area(r)`:
- This function calculates the area of a circle with a user-specified radius.
- Example: Input: `area(5)`; Output: 78.53975 (the area of a circle with a radius of 5).
### `def perimeter(r)`:
- This function calculates the perimeter (circumference) of a circle with a user-specified radius.
- Example: Input: `perimeter(5)`; Output: 31.4159 (the perimeter of a circle with a radius of 5)..

## `square.py`
### `def area(a)`:
- This function calculates the area of a square based on a user-specified side
- Example: Input: `area(4)`; Output: 16 (the area of a square with a side length of 4).
### `def perimeter(a)`:
- This function calculates the perimeter of a square based on a user-specified side.
- Example: Input: `perimeter(4)`; Output: 16 (the perimeter of a square with a side length of 4).

## `triangle.py`
### `def area(a, b, c)`:
- This function calculates the area of a triangle based on user-specified sides.
- Example: Input: `area(3, 4, 5)`; Output: 6 (the area of a triangle with sides 3, 4, and 5).
### `def perimeter(a, b, c)`:
- This function calculates the perimeter of a triangle based on user-specified sides.
- Example: Input: `perimeter(3, 4, 5)`; Output: 12 (the perimeter of a triangle with sides 3, 4, and 5).

# Project change history with commit hashes
1. Triangle added
   ```commit d080c7888b81955bad2ed78d58ad910526b5132a```
2. Doc updated for triangle
   ```commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3```
3. Add calculate.py
   ```commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71```
4. Update docs for calculate.py
   ```commit b5b0fae727ca72c317c383b39c0af73d6adcd81c```
5. Update circle.py
   ```commit 9aa716e2295cafba1ec7f2d03019a5755dac180b```
6. Update square.py 
   ```commit af0fde5f5d3ec76484885ad88d40fbd74d8d24c0```
7. Update triangle.py
   ```commit d6b47a4477fa0ecfb10b8d668d236b5df974466d```
8. Update calculate.py
   ```commit dc1fc2e3dd73d52e1b537df056ba6a2bf6b0abe7```
