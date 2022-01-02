import os

os.system("figlet image")


extension = input("what is the extension of your file : ")

if extension == "jpg":
	os.system("clear")
	import jpg
	jpg()

elif extension == "png":
	os.system("clear")
	import png
	png()

else:

	print("unsupported extension")