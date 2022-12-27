import colorgram

rgb_colors = []
colors = colorgram.extract("image.jpg", 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

color_list = rgb_colors
