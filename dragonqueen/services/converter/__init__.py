from os import listdir, mkdir

if "raw_files" not in listdir():
    mkdir("raw_files")

from dragonqueen.services.converter.converter import convert
