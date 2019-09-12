import foreground
import background
import style

def color(style, foreground_color, background_color):
    return "\033[{style};{foreground_color};{background_color}m".format(
        style = style,
        foreground_color = foreground_color,
        background_color = background_color
    )

RESET = "\033[0m"