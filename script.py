from PIL import Image
import pathlib

# image resizer
def resizeImage(file_name, extension, base_width):

	img = Image.open(file_name + extension)

	wpercent = (base_width / float(img.size[0]))

	hsize = int((float(img.size[1]) * float(wpercent)))

	img = img.resize((base_width, hsize), Image.ANTIALIAS)

	img.save(file_name + "-" + str(base_width) + "x" + str(hsize) + extension)

# It generate all thumbnails
def generateThumbnails(name_folder, sizes):
	for path in pathlib.Path(name_folder).iterdir():
		if path.is_file():
			for size in sizes:
				resizeImage(name_folder + "/" + path.stem, path.suffix, size)

generateThumbnails("images", [150, 300, 500, 600, 768, 800, 848, 1000, 1024, 1140])