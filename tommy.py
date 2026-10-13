a=int(input("enter first side of triangle"))
b=int(input("enter second side of triangle"))
c=int(input("enter third side of triangle"))
def triangle_info(a, b, c):
    # Check validity
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid sides"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    # Type
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
         print("Isosceles")
    else:
         print = ("Scalene")
    # Right-angled?
    x, y, z = sorted([a, b, c])
    is_right = "Right-angled" if abs(x*x + y*y - z*z) < 1e-9 else "Not right-angled"
    return f"{ttype}, {is_right}"