def ansi_coloring(text, color):
    if color == 'red':
        return f"\033[91m{text}\033[00m"
    elif color == 'green':
        return f"\033[92m{text}\033[00m"
    elif color == 'yellow':
        return f"\033[93m{text}\033[00m"
    elif color == 'blue':
        return f"\033[94m{text}\033[00m"
    elif color == 'magenta':
        return f"\033[95m{text}\033[00m"
    elif color == 'cyan':
        return f"\033[96m{text}\033[00m"
    elif color == 'white':
        return f"\033[97m{text}\033[00m"
    elif color == 'black':
        return f"\033[98m{text}\033[00m"
    else:
        return text


def ansi_coloring_hex_colour(text, colour):
    colour = [int(colour[1:3], 16), int(colour[3:5], 16), int(colour[5:7], 16)]
    return f"\033[38;2;{colour[0]};{colour[1]};{colour[2]}m{text}\033[00m"
