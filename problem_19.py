# Problem 19: Calculate power of a number
# Find and fix the error

def power(base, exponent):
    result = 1
    if exponent >=0:
     for i in range(exponent):
        result *= base
    else:
       for i in range(-exponent):
          result *= base
    return result

print(f"2^8 = {power(2, 8)}")
