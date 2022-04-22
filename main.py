import random
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('colors_img.jpg', 6)
rgb_colors = [x.rgb for x in colors]
print(rgb_colors)
numbers = [n for n in range(101)]
print(numbers)

chosen = random.choice(numbers)
print(chosen)

num0_10 = numbers[0:11]
print(num0_10)
