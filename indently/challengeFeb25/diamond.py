def create_diamond(width: int) -> None:
    """
    Prints a diamond shape using star characters based on the given width.
    :param
        width (int): The width of the diamond, must be greater than 2.
    :return
        None
    """
    linestring = ""
    even = width % 2 == 0
    if width <= 2:
        raise ValueError("width must be greater than 2")
    if even:
        start = 2
    else:
        start = 1
    for i in range(start, width + 1, 2):
        linestring = "*" * i
        print(linestring.center(width))
    for i in range(width - 2, start - 1, -2):
        linestring = "*" * i
        print(linestring.center(width))
