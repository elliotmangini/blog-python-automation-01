import os
current_directory = os.getcwd()  # => this is a string for our current directory

import pathlib
cwd_as_obj = pathlib.Path(current_directory)  # => turn that string into a path object

items = list(cwd_as_obj.iterdir())  # => list the paths inside our cwd

folder_count = 0
existing_count = 0
new_count = 0

for item in items:
    if item.is_dir():  # if this is a folder
        folder_count = folder_count + 1  # count it
        file_to_create = f"{item}/{item.name}_Notes.txt"  # name a notes file to make (string)

        if os.path.exists(file_to_create):  # if a notes file already exists
            print("File Exists")
            existing_count = existing_count + 1  # count it
        else:  # otherwise
            print(f"Creating File {folder_count}: {file_to_create}")
            new_count = new_count + 1  # count it
            with open(file_to_create, "x") as f:  # make a new notes file
                f.write(f"{item.name} Notes:")  # populate it with a correct heading
                f.close()

print(f"{folder_count} Folders found in this directory.")
print(f"{existing_count} Notes Files found in subdirectories.")
print(f"{new_count} new Notes Files created.")