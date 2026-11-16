# Program: Copy, Move and Delete Files using shutil

import shutil
import os

# Create a source file
source = "source2.txt"

with open(source, "w") as file:
    file.write("Helloooooo, Python!")

print("Source file created.")

# Copy the file
copy_file = "copy.txt"
shutil.copy(source, copy_file)
print("File copied successfully.")

# Move the copied file
move_file = "moved.txt"
shutil.move(copy_file, move_file)
print("File moved successfully.")

# Delete the moved file
if os.path.exists(move_file):
    os.remove(move_file)
    print("File deleted successfully.")
