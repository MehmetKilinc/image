#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image,ImageFilter
import optparse
import os

os.system("sysvbanner only png")

def imageShow(image):

	with Image.open(image) as image1:

		image1.show()

def imageInfo(image):

	os.system("exiftool {}".format(image))
	os.system("exiftool {} > info.txt".format(image))

def imageRotation(image , value):

	with Image.open(image) as image1:

		image1.rotate(value).save("rotation.png")
		with Image.open("rotation.png") as image2:
			image2.show()

def blur(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.BLUR)
		filteredImage.save("blur.png")
		with Image.open("blur.png") as image2:
			image2.show()
def contour(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.CONTOUR)
		filteredImage.save("contour.png")
		with Image.open("contour.png") as image2:
			image2.show()

def detail(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.DETAIL)
		filteredImage.save("detail.png")
		with Image.open("detail.png") as image2:
			image2.show()

def edgeEnhance(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.EDGE_ENHANCE)
		filteredImage.save("edgeEnhance.png")
		with Image.open("edgeEnhance.png") as image2:
			image2.show()

def edgeEnhanceMore(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.EDGE_ENHANCE_MORE)
		filteredImage.save("edgeEnhanceMore.png")
		with Image.open("edgeEnhanceMore.png") as image2:
			image2.show()

def emboss(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.EMBOSS)
		filteredImage.save("emboss.png")
		with Image.open("emboss.png") as image2:
			image2.show()

def findEdges(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.FIND_EDGES)
		filteredImage.save("findEdges.png")
		with Image.open("findEdges.png") as image2:
			image2.show()

def smooth(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.SMOOTH)
		filteredImage.save("smooth.png")
		with Image.open("smooth.png") as image2:
			image2.show()

def smoothMore(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.SMOOTH_MORE)
		filteredImage.save("smoothMore.png")
		with Image.open("smoothMore.png") as image2:
			image2.show()

def sharpen(image):

	with Image.open(image) as image1:

		filteredImage = image1.filter(ImageFilter.SHARPEN)
		filteredImage.save("sharpen.png")
		with Image.open("sharpen.png") as image2:
			image2.show()

image = input("enter png file name : ")



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


