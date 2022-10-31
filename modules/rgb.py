import cv2 as cv
import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt
asoy = ''
asoy2 = ''

def getInputImage():
    global asoy, asoy2
    inputImage = input('Masukan nama gambar: ')
    pathImage = 'images/input/'+ inputImage
    image = skimage.io.imread(fname=pathImage)
    image2 = cv.imread(pathImage)
    asoy = image
    asoy2 = image2

def showRGBImage(skipped = True):
    plt.imshow(asoy)
    plt.show(block=skipped)

def histogramRGBImage(skipped = True):
    colors = ("red", "green", "blue")
    channel_ids = (0, 1, 2)
    plt.figure()
    plt.xlim([0, 256])
    for channel_id, c in zip(channel_ids, colors):
        histogram, bin_edges = np.histogram(
            asoy[:, :, channel_id], bins=256, range=(0, 256)
        )
        plt.plot(bin_edges[0:-1], histogram, color=c)
    plt.title("Color Histogram")
    plt.xlabel("Color value")
    plt.ylabel("Pixel count")
    plt.show(block=skipped)

def quantization(skipped=True):
    colors = ("red", "green", "blue")
    channel_ids = (0, 1, 2)
    plt.figure()
    plt.xlim([0, 256])
    for channel_id, c in zip(channel_ids, colors):
        histogram, bin_edges = np.histogram(
            asoy[:, :, channel_id], bins=256, range=(0, 256)
        )
        cdf = histogram.cumsum()
        cdf_normalized = cdf * float(histogram.max()) / cdf.max()
        plt.plot(bin_edges[0:-1], cdf_normalized, color=c)
    plt.title("Color Histogram")
    plt.xlabel("Color value")
    plt.ylabel("Pixel count")
    plt.show(block=skipped)

def showEqImage(skipped=True):
    img_hsv = cv.cvtColor(asoy2, cv.COLOR_BGR2HSV)
    img_hsv[:,:,0] = cv.equalizeHist(img_hsv[:,:,0])
    img_output = cv.cvtColor(img_hsv, cv.COLOR_HSV2BGR)
    plt.figure()
    plt.imshow(img_output)
    plt.show(block=skipped)

def rgb():
    getInputImage()
    showRGBImage(False)
    histogramRGBImage()

def eq():
    getInputImage()
    showRGBImage(False)
    histogramRGBImage(False)
    showEqImage(False)
    quantization()
