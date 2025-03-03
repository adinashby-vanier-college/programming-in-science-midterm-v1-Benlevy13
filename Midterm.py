import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = round(math.pi * (radius ** 2), 2)
    return area


# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""
    if n >= 4:
        result += "*\n"
        for i in range(0, n - 2):
            result += "*" + " " * i + "*"
            result += "\n"
        result += "*" * n
    else:
        result += "The triangle height should be at least 4."
    return result

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    return ""

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()