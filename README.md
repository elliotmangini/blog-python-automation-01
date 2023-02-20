## Python Program to Generate Notes File for Each Subdirectory

I recently watched a [one-hour Python class](https://youtu.be/hMCJDycsHks) offered by [StudySession](https://www.youtube.com/channel/UCaFHlSOg83nCUIHlFMlUhPw) to learn the basics of Python syntax. The class covered topics such as variables, data types, conditionals, loops, functions, classes and all the basics I would need to get started because I wanted to try writing my first automation stuff. The following is...
&nbsp;

## My First Automation Script!

<strong>This script is a Python program that generates a notes file for each subdirectory in the current working directory.</strong>

<p>The problem I'm solving is that I have 600+ songs and I want to make a place to take notes on them as I work on them, and I wanna do it quickly.</p>
&nbsp;

## What I want to end up with:

![Notes Files for All Songs](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ylhqp85ob5h8rv4ditcg.png)
<figcaption>
Notes Files for All Songs
</figcaption>
&nbsp;

<p>I have another simple automation project I'll post about soon, and then more as I've found when you are managing a project with a discography of several hundred songs it is difficult to do even the simplest things without automation!!</p>
&nbsp;

# The actual script:

```py
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
```

It starts by importing the `os` module to retrieve the current working directory path as a string. Then it uses the `pathlib` module to convert the string path to a path object. After that, it lists all the paths inside the current working directory using the `.iterdir()` method.

The program then initializes three variables: `folder_count`, `existing_count`, and `new_count`, all with an initial value of 0. The program then enters a `for` loop that iterates over each item (i.e., file or directory) inside the current working directory. If the item is a directory (i.e., a subdirectory), the program increments the `folder_count` variable and proceeds to create a notes file for that directory.

<em>Quick aside-- if you're coming from JS this is how string interpolation/template literals work in python:</em>

in JS:

```js
wordOne = "Hello"
wordTwo = "World"
console.log(`${wordOne} ${wordTwo}!`)  // => "Hello World!"
```

vs py:

```py
word_one = "Hello"
word_two = "World"
print(f"{word_one} {word_two}!")  # => "Hello World!"
```

<em>Backticks become double-quotes and we use curly braces without a $ before them</em>
&nbsp;

The name of the notes file is set to `{item}/{item.name}_Notes.txt`. The first `{item}` refers to the path of the directory, while `{item.name}` refers to the name of the directory. The `.txt` extension is added to denote that this is a text file.


![Screenshot of Created Files](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bpn4vl0cwquuluvv9udw.png)
<figcaption>
Screenshot of Created Files
</figcaption>
&nbsp;

If a notes file already exists in the subdirectory, the program increments the `existing_count` variable and prints the message "File Exists". Otherwise, the program increments the `new_count` variable, prints the message `"Creating File {folder_count}: {file_to_create}"` and proceeds to create a new file with the name and location specified in `file_to_create`.

![Notes File Boilerplate Example Screenshot](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yc8fomk4iwzf3emmibk9.png)
<figcaption>
Notes File Boilerplate Example
</figcaption>
&nbsp;

To create a new file, the program uses the `open()` function with the `x` mode. The `x` mode creates a new file and opens it for writing. It also populates a header for the text file using `f.write(f"{item.name} Notes:")`.


![File Setup Before Script Runs](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mb4336zt4apykxk1tp6y.png)
<figcaption>
File Setup Before Script Runs
</figcaption>
&nbsp;

To run it we just use `python3 <name_of_script_here.py>`.

Altogether here's what I have the console doing for me, accounting for all blocks of code being reached:

![Running Script & Showing Terminal Output](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/aosn0yel24rcy06w85fe.png)
<figcaption>
Running Script & Showing Terminal Output
</figcaption>
&nbsp;

The program prints a summary of the number of subdirectories found, the number of existing notes files, and the number of new notes files created. The message includes the `folder_count`, `existing_count`, and `new_count` variables.

# We end with:

![All Notes Created In Correct Places](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kown7hqwn9h5d01w5nt0.png)
<figcaption>
All Notes Created In Correct Places
</figcaption>
&nbsp;

You can check it out and try the script for yourself on my [GitHub](https://github.com/elliotmangini/blog-python-automation-01).


![Preview of my second simple python automation project screenshot.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6o8g0vsizl130js9d74w.png)
<figcaption>
Preview of my second simple python automation project.
</figcaption>
&nbsp;

Next post will be about how to take all of these folders containing multiple bounces of songs (as they have progressed) ie version 1, version 2, etc. And creating a folder where every song is represented by one file-- whichever is most recent. Smash that follow button to see how I did it. And let me know if there's any way I can make my blogs easier to follow or more useful for those finding them!

Thanks,
-Elliot/Big Sis
