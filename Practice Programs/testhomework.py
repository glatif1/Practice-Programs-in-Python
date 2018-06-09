
def main():
    # Change the path in Line 6 to the path of the image you want to use as input 
    # for Windows users the path specify the path as "c:\\users\\alark1\\Pictures\\usfca.png"
    inputImage = Image.open('usfca_logo.png')
    imageWidth, imageHeight = inputImage.size
    scrollHorizontal(inputImage, imageWidth, imageHeight, numpixels)
	def scrollHorizontal(inputImage, imageWidth, imageHeight, numpixels):
	    scrollHOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

	    numpixels = int(input("Enter number of pixels:"))

	    for i in range(numpixels,imageWidth):
	        for j in range(0,imageHeight):

	            pixelColors = inputImage.getpixel((i, j))
	            scrollHoutpututput.putpixel((i-numpixels, j), pixelColors)

	    scrollHOutput.save("copy.png")