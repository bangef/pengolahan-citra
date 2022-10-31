import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt
asoy = ''

def getInputImage():
    global asoy
    inputImage = input('Masukan nama gambar: ')
    pathImage = 'images/'+ inputImage
    image = skimage.io.imread(fname=pathImage, as_gray=True)
    asoy = image

def showGrayscaleImage():
    fig, ax = plt.subplots()
    plt.imshow(asoy, cmap='gray')
    plt.show(block=False)

def histogramGrayscaleImage():
    histogram, bin_edges = np.histogram(asoy, bins=256, range=(0, 1))
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixel count")
    plt.xlim([0.0, 1.0])  # <- named arguments do not work here

    plt.plot(bin_edges[0:-1], histogram)  # <- or here
    plt.show()

def grayscale():
    getInputImage()
    showGrayscaleImage()
    histogramGrayscaleImage()