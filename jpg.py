#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image,ImageFilter
import optparse
import os

os.system("sysvbanner only jpg")

def imageShow(image):

	with Image.open(image) as image1:

		image1.show()

def imageInfo(image):

	os.system("exiftool {}".format(image))
	os.system("exiftool {} > info.txt".format(image))

def imageRotation(image , value):

	with Image.open(image) as image1:

		image1.rotate(value).save("rotation.jpg")
		with Image.open("rotation.jpg") as image2:
			image2.show()

def blur(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.BLUR)
		filteredImage.save("blur.jpg")
		with Image.open("blur.jpg") as image2:
			image2.show()
def contour(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.CONTOUR)
		filteredImage.save("contour.jpg")
		with Image.open("contour.jpg") as image2:
			image2.show()

def detail(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.DETAIL)
		filteredImage.save("detail.jpg")
		with Image.open("detail.jpg") as image2:
			image2.show()

def edgeEnhance(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.EDGE_ENHANCE)
		filteredImage.save("edgeEnhance.jpg")
		with Image.open("edgeEnhance.jpg") as image2:
			image2.show()

def edgeEnhanceMore(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.EDGE_ENHANCE_MORE)
		filteredImage.save("edgeEnhanceMore.jpg")
		with Image.open("edgeEnhanceMore.jpg") as image2:
			image2.show()

def emboss(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.EMBOSS)
		filteredImage.save("emboss.jpg")
		with Image.open("emboss.jpg") as image2:
			image2.show()

def findEdges(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.FIND_EDGES)
		filteredImage.save("findEdges.jpg")
		with Image.open("findEdges.jpg") as image2:
			image2.show()

def smooth(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.SMOOTH)
		filteredImage.save("smooth.jpg")
		with Image.open("smooth.jpg") as image2:
			image2.show()

def smoothMore(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.SMOOTH_MORE)
		filteredImage.save("smoothMore.jpg")
		with Image.open("smoothMore.jpg") as image2:
			image2.show()

def sharpen(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.SHARPEN)
		filteredImage.save("sharpen.jpg")
		with Image.open("sharpen.jpg") as image2:
			image2.show()

image = input("enter jpg file name : ")



while True:


	print("""

		[1] Show image

		[2] Image info

		[3] Image rotation

		[4] BLUR_FILTER

		[5] CONTOUR_FILTER

		[6] DETAIL_FILTER

		[7] EDGE_ENHANCE_FILTER
			
		[8] EDGE_ENHANCE_MORE_FILTER

		[9] EMBOSS_FILTER

		[10] FIND_EDGES_FILTER

		[11] SMOOTH_FILTER

		[12] SMOOTH_MORE_FILTER

		[13] SHARPEN_FILTER

		[Q] Exit



		""")

	choice2 = input("enter your choice : ")


	if choice2 == "1":

		imageShow(image)
		os.system("clear")



	elif choice2 == "2":

		imageInfo(image)
		


	elif choice2 == "3":

			
		try:
			value = int(input("enter the rotation value of the image : "))
			imageRotation(image , value)

		except ValueError:

			value = int(input("please enter only integer numbers : "))
			imageRotation(image , value)
		os.system("clear")


	elif choice2 == "4":

		blur(image)
		os.system("clear")

	elif choice2 == "5":

		contour(image)
		os.system("clear")

	elif choice2 == "6":

		detail(image)
		os.system("clear")

	elif choice2 == "7":

		edgeEnhance(image)
		os.system("clear")

	elif choice2 == "8":

		edgeEnhanceMore(image)
		os.system("clear")

	elif choice2 == "9":

		emboss(image)
		os.system("clear")

	elif choice2 == "10":

		findEdges(image)
		os.system("clear")

	elif choice2 == "11":

		smooth(image)
		os.system("clear")

	elif choice2 == "12":

		smoothMore(image)
		os.system("clear")

	elif choice2 == "13":

		sharpen(image)
		os.system("clear")


	elif choice2 == "q" or choice == "Q":

		os.system("clear")
		break

	else:

		print("wrong value")
		os.system("clear")


