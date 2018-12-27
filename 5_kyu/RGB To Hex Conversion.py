# Description:
# The rgb() method is incomplete.
# Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned.
# The valid decimal values for RGB are 0 - 255. Any (r,g,b)
# argument values that fall out of that range should be rounded to the closest valid value.


def dec_to_hex(color):
    letters = 'ABCDEF'
    hexa = []
    if color < 0:
        color = 0
    if color > 255:
        color = 255
    ratio = color % 16
    if ratio < 10:
        hexa.append(str(ratio))
    if 10 <= ratio <= 15:
        hexa.append(letters[ratio - 10])
    if color > 15:
        hexa.append(dec_to_hex(color // 16))
    return ''.join(hexa)


def rgb(a, b, c):
    buf = []
    for color in (a, b, c):
        hex_color = dec_to_hex(color)[::-1]
        if len(hex_color) == 1:
            hex_color = '0' + hex_color
        buf.append(hex_color)
    out = ''.join(buf)
    return out


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
