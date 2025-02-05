def MidpointLine(x0, y0, x1, y1, value):
    def WritePixel(x, y, value):
        # This function should plot the pixel at (x, y) with the given value
        # Implementation depends on the specific graphics library you're using
        print(f"Plotting pixel at ({x}, {y}) with value {value}")

    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)
    x = x0
    y = y0
    WritePixel(x, y, value)
    
    while x < x1:
        if d <= 0:
            # choose E
            d = d + incrE
            x = x + 1
        else:
            # choose NE
            d = d + incrNE
            x = x + 1
            y = y + 1
        WritePixel(x, y, value)

# Example usage:
MidpointLine(0, 0, 10, 5, 1)

#Took from chatgpt
