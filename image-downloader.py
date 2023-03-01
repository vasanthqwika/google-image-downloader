from pygoogle_image import image as gi
import os
import shutil

# read image names with file
def read_image_names(fileName=None):
	fileNames = []

	if fileName is not None:
		# check path is exist or not 
		if os.path.exists(fileName):
			with open(fileName) as file:
				fileNames = file.read().split('\n')
		else:
			print("File is not found !")

	return fileNames
		
# download image with filenames
def download_images(fileNames):
	for fileName in fileNames:
		gi.download(fileName, limit=4)

# move images in image folder
def move_images(dirNames, newImagePath):
	# check new Image path find not create folder other wise create folder
	if not os.path.exists(newImagePath):
		os.mkdir(newImagePath);

	for dirName in dirNames:
		
		# check path is exists
		_dirName = dirName.replace(' ', '_') 
		if os.path.exists("images/" + _dirName):
			
			# scan directory
			for imageFile in os.scandir("images/" + _dirName):
				dummy = int(imageFile.name.split('_')[1].split('.')[0])

				if 2 < dummy: 
					_imageFile = f"images/{_dirName}/{imageFile.name}"
					shutil.move(_imageFile, newImagePath)



def main():
	# file name
	FILE_NAME = "image_names.txt"
	NEW_IMAGE_PATH = "filter_images"

	fileNames = read_image_names(FILE_NAME)
	download_images(fileNames)
	move_images(fileNames, NEW_IMAGE_PATH)

if __name__ == '__main__':
	main()

# pi.download("Mango Senthoora",limit=5)
# pi.download("Apple Royal Gala",limit=5)
# pi.download("Banana Karpooravalli",limit=5)
# pi.download("Banana Poovan",limit=5)