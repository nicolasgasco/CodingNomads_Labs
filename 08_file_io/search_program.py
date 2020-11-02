"""
Write a script that searches a folder you specify (as well as all its subfolders) on your computer and compiles a list of all .jpg files. The list should contain the complete path of each .jpg file.

If you are feeling bold, create a list containing each type of file extension you find in the folder.

Start with a small folder to make it easy to check whether your program is working correctly. Then switch that small folder name with a bigger folder.

This program should work for any specified folder on your computer.
"""
import os

dir_path = "/home/nicolasg/Pictures"
new_list = []

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.png'):
            # jpg_file = root + '/' + str(file)
            new_list.append(f"{root}/{str(file)}")

print(new_list)
