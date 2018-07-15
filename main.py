from PIL import Image, ImageFilter
#Read image
im = Image.open( 'image.jpg' )
#Display image
im.show()

#Applying a filter to the image
im_sharp = im.filter( ImageFilter.SHARPEN )
im_sharp.save( 'image_sharpened.jpg', 'JPEG' )
im_sharp.show()

im_blur = im.filter( ImageFilter.BLUR )
im_blur.save( 'image_blur.jpg', 'JPEG' )
im_blur.show()

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
r,g,b = im_sharp.split()

#Viewing EXIF data embedded in image
exif_data = im._getexif()
exif_data