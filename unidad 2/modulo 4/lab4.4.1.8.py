'''
nombre:Monserat Orduña Basaldua
descripcion:lab 4.4.1.8
Fecha:08/11/2023
'''
import os

def find(path, dir_name):
    for foldername, subfolders, filenames in os.walk(path):
        if dir_name in subfolders:
            dir_path = os.path.join(foldername, dir_name)
            print(os.path.abspath(dir_path))

path = "./tree"
dir_name = "python"
find(path, dir_name)
