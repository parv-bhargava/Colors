
from matplotlib.colors import to_rgb, to_hex
from skimage.color import rgb2lab, lab2rgb
import numpy as np
import matplotlib.pyplot as plt

def hex_to_lab(hex_color):
    """Convert HEX to LAB color space."""
    rgb = np.array([to_rgb(hex_color)])
    lab = rgb2lab(rgb)
    return lab[0]

def lab_to_hex(lab_color):
    """Convert LAB to HEX color space."""
    rgb = lab2rgb([lab_color])
    return to_hex(rgb[0])

def interpolate_colors(color_start, color_end, num_colors):
    """Interpolate between two colors in LAB space and return HEX codes."""
    lab_start = hex_to_lab(color_start)
    lab_end = hex_to_lab(color_end)
    lab_colors = [lab_start + (lab_end - lab_start) * i / (num_colors - 1) for i in range(num_colors)]
    hex_colors = [lab_to_hex(color) for color in lab_colors]
    return hex_colors


def plot_color_scales(hex_scales, titles):
    """Plot color scales using matplotlib and annotate with HEX codes."""
    fig, axes = plt.subplots(1, len(hex_scales), figsize=(18, 3))
    if len(hex_scales) == 1:
        axes = [axes]
    for ax, scale, title in zip(axes, hex_scales, titles):
        colors = [to_rgb(color) for color in scale]
        ax.imshow([colors], aspect='auto')
        ax.set_title(title)

        # # Annotate each color with its HEX code
        # for i, hex_code in enumerate(scale):
        #     ax.text(i, 0, hex_code, fontsize=9, ha='center')
        #
        # ax.axis('off')
    plt.tight_layout()
    plt.show()

# Define base colors for the scales
base_colors = {
    'deep_teal': '#006D77',
    'vibrant_yellow': '#FFEA00',
    'light_blue': '#A2CFFE',
    'warm_orange': '#FF8C00',
    'burgundy': '#800020',
}

# Generate the qualitative scale
qualitative_scale_hex = [
    base_colors['deep_teal'],
    base_colors['vibrant_yellow'],
    base_colors['light_blue'],
    base_colors['warm_orange'],
    base_colors['burgundy'],
]


light_blue_to_deep_teal = interpolate_colors(base_colors['light_blue'], base_colors['deep_teal'], 5)
vibrant_yellow_to_warm_orange = interpolate_colors(base_colors['vibrant_yellow'], base_colors['warm_orange'], 5)

deep_teal_to_white = interpolate_colors(base_colors['deep_teal'], '#FFFFFF', 5)[:-1] # Exclude white
white_to_burgundy = interpolate_colors('#FFFFFF', base_colors['burgundy'], 5)
adjusted_diverging_scale = deep_teal_to_white + white_to_burgundy

plot_color_scales([qualitative_scale_hex], ['Qualitative Scale'])
plot_color_scales([light_blue_to_deep_teal], ['Light Blue to Deep Teal Sequential Scale'])
plot_color_scales([vibrant_yellow_to_warm_orange], ['Yellow to Warm Orange Sequential Scale'])
plot_color_scales([adjusted_diverging_scale], ['Diverging Scale'])

