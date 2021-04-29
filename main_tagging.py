#!/usr/bin/python

import sys
import pandas as pd
import os
import pathlib

def main():
    argumentos = sys.argv
    images_dir = ''
    if len(argumentos) <= 1:
	    images_dir = input("Ingrese el directorio en donde están sus imágenes: ")
	    while(not os.path.isdir(images_dir)):
		    images_dir = input("Ingrese el directorio en donde están sus imágenes: ")
    else:
        images_dir = argumentos[1]
    read_dir(images_dir)

def read_dir(paren_dir):
    datos = [[],[],[]]
    directorio = pathlib.Path(paren_dir)
    carpetas = [fichero for fichero in directorio.iterdir() if fichero.is_dir()]
    for carpeta in carpetas:
        imagenes = [file for file in carpeta.absolute().iterdir() if file.is_file() and file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))]
        for imagen in imagenes:
            datos[0].append(imagen.relative_to(directorio.parent.absolute()))
            datos[1].append(imagen.absolute())
            datos[2].append(carpeta.name)
    df = pd.DataFrame({'r_path':datos[0] ,'a_path':datos[1],'tag':datos[2]})
    df.to_csv('output.csv', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()


