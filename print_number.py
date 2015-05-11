#input a numpy array
def print_number (pic1):
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    import numpy as np

    plt.imshow(pic1, cmap = cm.Greys_r, interpolation= 'none')
    plt.show()

    return




