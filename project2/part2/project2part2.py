from PIL import Image


def copyImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)

    copyImageOutput.save("copy.png")



def main():
    # Change the path in Line 6 to the path of the image you want to use as input 
    # for Windows users the path specify the path as "c:\\users\\alark1\\Pictures\\usfca.png"
    inputImage = Image.open('usfca_logo.png')
    imageWidth, imageHeight = inputImage.size
    initialAnswer = 0
    while initialAnswer >= 0 and initialAnswer <=10:
        print(""" What would you like to do?
            1. Copy image
            2. Flip the image Vertically
            3. Flip the image Horizontally
            4. Brighten Image
            5. Darken Image
            6. Scroll Image Horizontally
            7. Scroll Image Vertically
            8. Grey Scale Image
            9. Rotate
            10. Swap Corners
            """)
        initialAnswer=int(input("Enter the corresponding number:"))
        if initialAnswer == 1:
            copyImage(inputImage, imageWidth, imageHeight)
            img = Image.open("copy.png")
            img.show()

        if initialAnswer ==2:
            img = Image.open('vflip.png')
            img.show()
        if initialAnswer == 3:
            img = Image.open('hflip.png')
            img.show()
        if initialAnswer== 4:
            amount = 0
            print("Enter a number between 0 and 1. Higher is brighter.")
            amount = float(input("Here:"))
            lighten(inputImage,imageWidth,imageHeight,amount)
            img = Image.open("light.png")
            img.show()
        if initialAnswer == 5:
            amount = 0
            print("Enter a number between 0 and 1. Higher is darker ")
            amount = float(input("Here:"))
            darken(inputImage,imageWidth,imageHeight,amount)
            img = Image.open("darken.png")
            img.show()
        if initialAnswer == 6:
            amount = 0
            print("Enter a number of pixels to scroll.")
            numpixels = int(input("Here:"))
            scrollHorizontal(inputImage,imageWidth,imageHeight,numpixels)
            img = Image.open("scrollhorizontal.png")
            img.show()
        if initialAnswer == 7:
            amount = 0
            numpixels = int(input("Here:"))
            scrollVertical(inputImage, imageWidth, imageHeight, numpixels)
            img = Image.open("scrollvertical.png")
            img.show()
        if initialAnswer == 8:

            greyscale(inputImage,imageWidth,imageHeight)
            img = Image.open("greyscale.png")
            img.show()
        if initialAnswer == 9:

            rotate(inputImage,imageWidth,imageHeight)
            img = Image.open("rotate.png")
            img.show()
        if initialAnswer == 10:

            swapCorners(inputImage,imageWidth,imageHeight)
            img = Image.open("swapcorners.png")
            img.show()



        else:

            print("""

                >>>>Enter a number 1 through 10<<<<

                """)
            main()


# Creates a copy of an image given the image variable, its width, and height
def copyImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)

    copyImageOutput.save("copy.png")

#Flips the image horizontally
def flipHorizontal(inputImage,imageWidth,imageHeight):
    flipHorizontalOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for j in range(imageHeight):
        for i in range(imageWidth):
            pixelcoordinate = inputImage.getpixel((i,j))
            flipHorizontalOutput.putpixel(((imageWidth-i)-1,j),pixelcoordinate)


    flipHorizontalOutput.save("hflip.png")


#Flips the image vertically
def flipVertical(inputImage,imageWidth,imageHeight):
    flipverticalOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for j in range(imageHeight):
        for i in range(imageWidth):
            pixelcoordinate = inputImage.getpixel((i,j))
            flipverticalOutput.putpixel((i,(imageHeight-j)-1),pixelcoordinate)


    flipverticalOutput.save("vflip.png")


#lightens the image
def lighten(inputImage,imageWidth,imageHeight,amount):
    lightenImageOutput = Image.new('RGB',(imageWidth,imageHeight),'white')
    for j in range(imageHeight):
        for i in range(imageWidth):
            pixel = inputImage.getpixel((i,j))
            red = pixel[0]
            green = pixel[1]
            blue= pixel[2]
            newred = (1-amount)* red + amount *255
            newgreen =(1-amount)* green + amount *255
            newblue= (1-amount)* blue + amount *255
            newpixel = (int(newred),int(newgreen), int(newblue))

            lightenImageOutput.putpixel((i,j), newpixel)

    lightenImageOutput.save("light.png")


def darken(inputImage, imageWidth, imageHeight, amount):
    darkenImageOutput= Image.new('RGB',(imageWidth,imageHeight),'white')
    for j in range(imageHeight):
        for i in range(imageWidth):
            pixel = inputImage.getpixel((i,j))
            red = pixel[0]
            green = pixel[1]
            blue= pixel[2]
            newred = (1-amount)* red
            newgreen =(1-amount)* green
            newblue= (1-amount)* blue
            newpixel = (int(newred),int(newgreen), int(newblue))

            darkenImageOutput.putpixel((i,j), newpixel)

    darkenImageOutput.save("darken.png")
            




def scrollHorizontal(inputImage, imageWidth, imageHeight, numpixels):
    scrollHOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

 
    #part B of the image
    for i in range(numpixels,imageWidth):
        for j in range(0,imageHeight):

            pixelColors = inputImage.getpixel((i, j))
            scrollHOutput.putpixel((i-numpixels, j), pixelColors)
    #part A of the image
    for i in range(0,numpixels):

        for j in range(0,imageHeight):

            pixelColors = inputImage.getpixel((i, j))
            scrollHOutput.putpixel((imageWidth-numpixels+i, j), pixelColors)



    scrollHOutput.save("scrollhorizontal.png")

def scrollVertical(inputImage, imageWidth, imageHeight, numpixels):
    scrollVOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

 
    #part B of the image
    for i in range(numpixels,imageHeight):
        for j in range(0,imageWidth):

            pixelColors = inputImage.getpixel((j,i))
            scrollVOutput.putpixel((j, i-numpixels), pixelColors)

    #part A of the image
    for i in range(0,numpixels):
        for j in range(0,imageWidth):

            pixelColors = inputImage.getpixel((j, i))
            scrollVOutput.putpixel((j,(i+(imageHeight-numpixels))), pixelColors)



    scrollVOutput.save("scrollvertical.png")


def greyscale(inputImage, imageWidth, imageHeight):
    greyscaleOutput= Image.new('RGB',(imageWidth,imageHeight),'white')
    for j in range(imageHeight):
        for i in range(imageWidth):
            pixel = inputImage.getpixel((i,j))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            newred = red *.3
            newgreen = green * .59
            newblue =  blue* .11
            greypixel = (int(newred)+int(newgreen)+int(newblue))
            newpixel = (int(greypixel),int(greypixel),int(greypixel))
            
            greyscaleOutput.putpixel((i,j),newpixel)

    greyscaleOutput.save("greyscale.png")


def swapCorners(inputImage,imageWidth,imageHeight):
    swapCornersOutput= Image.new('RGB',(imageWidth,imageHeight),'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors= inputImage.getpixel((i,j))

            cut_height = imageHeight//2
            cut_width = imageWidth//2

            if j< cut_height:
                new_height = j + cut_height
            if j >= cut_height:
                new_height = j - cut_height
            if i < cut_width: 
                new_width = i+ cut_width
            elif i>= cut_width:
                new_width = i - cut_width

            swapCornersOutput.putpixel((new_width,new_height), pixelColors)

    

    swapCornersOutput.save("swapcorners.png")


def rotate(inputImage, imageWidth, imageHeight):
    newWidth = imageHeight
    newHeight= imageWidth

    rotateOutput = Image.new('RGB',(imageHeight,imageWidth),'white')

    for i in range(newWidth):
        for j in range(newHeight):
            pixelColors = inputImage.getpixel((j,i))
            rotateOutput.putpixel((i,newHeight -1 -j), pixelColors)

    rotateOutput.save("rotate.png")
main()












