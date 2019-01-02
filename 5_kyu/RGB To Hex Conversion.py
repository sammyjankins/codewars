# Description:
# The rgb() method is incomplete.
# Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned.
# The valid decimal values for RGB are 0 - 255. Any (r,g,b)
# argument values that fall out of that range should be rounded to the closest valid value.


def rgb(r, g, b):
    return ''.join(['{:02X}'.format(x) for x in [max(0, min(y, 255)) for y in (r, g, b)]])


color_1 = (255, 255, 255)
color_2 = (254, 253, 252)
color_3 = (0, 0, 0)
color_4 = (1, 2, 3)
color_5 = (-20, 275, 125)
print(rgb(*color_1))
print(rgb(*color_2))
print(rgb(*color_3))
print(rgb(*color_4))
print(rgb(*color_5))
