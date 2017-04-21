#!/bin/bash
# Usage: compress all images in the imagenes folder
shopt -s nullglob

for f in imagenes/*/*.jpg
do
	mogrify -compress JPEG -define jpeg:extent=100kb $f
	echo $f
done
