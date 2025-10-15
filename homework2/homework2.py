# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# Git --> is the software that runs on the local computer to track changes in your files, allowing us to save different versions, revert to previous states, and collaborate with others
# GitHub --> is a web-based hosting sevice for Git repositories, it stores the git projects in the cloud
# Git Bash --> provides a command line interference to use Git. Bash shell environement similar to those in Mac and Linux


# 2) What’s the difference between the terminal and the command line?
# Command line is the textbased interference where you type commands, while the terminal is the program that provides the graphical window and teh environmentin which one can use the command line

# 3) How does Windows PowerShell differ from Git Bash?
# Windows PowerShell is a built-in command line shell and scripting language for Windows, specifically designed to manage Windows systems
# Git Bash is a Bash shell emulator for Windows, its primary purpose is to provide is to provide a Unix-like environment on Windows, making it easier to run Git commands.

# 4) What’s the difference between Anaconda, conda, and Python?
# Python: is a general-purpose programming language
# Anaconda: is a distributionof Python and R. It includes Python, the conda package manager, and a large collection of pre-installed scientific computing libraries
# conda: is a package environment manager, its a command line tool that comes with Anaconda. Used to install packages and libraries, so different projects can have different versions of Python and libraries without interfering

# 5) What is VS Code? 
# VS Code (Visual Studio Code) is a free, open-source code editor created by Microsoft. It's a lightweight but powerful tool for writing and debugging code, with support for a vast number of programming languages, extensions, and features like integrated terminal and Git control.

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# A Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. It's great for exploratory data analysis and sharing results.
# Jupyter Lab is the next-generation user interface for Project Jupyter. While a Jupyter Notebook is a single document within your web browser, JupyterLab provides a more powerful and flexible "IDE-like" environment. It allows you to open multiple notebooks, terminals, text editors, and other files in a single, tabbed interface.

# 7) What does ~/ mean?
# it is a shortcut that represents your home directory

# 8) What’s the difference between an absolute path and a relative path?
# Absolute path:  is the full address of a file or directory, starting from the root of the file system. It's like giving a complete mailing address.
# A relative path: the address of a file or directory relative to your current location. It's a shortcut that depends on where you are.

#9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# Relative Path: course_assignments/homework2
# Absoulte Path: ~/OneDrive/escritorio/python_decal_fa25/course_assignments/homework2

#10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# cd ..

# 11) What would rm ./ do in your current directory? (Don’t try it!)
# The rm is used to remove files. The ./ specifies the current directory

# 12) What do the following commands do?
# git add: This command stages changes for the next commit. It tells Git which new or modified files you want to include in the next snapshot.
# git commit: This command saves the staged changes to the local repository. It creates a new "snapshot" or version of your project and typically includes a message describing the changes.
# git push: This command uploads your local commits to a remote repository (like on GitHub). It synchronizes your local changes with the remote version of the project.

# 13) What's the difference between "git add ." and "git add <file>"?
# git add . : The command stages all new and modified flies in your current directory and its subdirectories
# git add <files>: the command stages a single, specific file

# 14) What do "git status" and "git log -1" do?
# git status: This command shows you the state of your working directory and staging area. It tells you which files are untracked, modified, and staged for the next commit.
# git log -1: This command shows you the last (most recent) commit in the repository's history. It's a quick way to see the details of the latest snapshot, including the author, date, and commit message.

# 15) What’s the difference between cloning a repository and pulling from it?
# cloning (git clone): is for getting a repository for the first time. It downloads a complete copy of a remote repository from a server (like GitHub) to your local machine.
# pulling (git pull):  is for updating an existing local repository. It fetches the latest changes from the remote repository and merges them into your current local branch.

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# I would say that at first finding the python_decal_fa25 in my OneDrive and finding and switching repositories.

# 17) What’s a question you still have? What’s something you’re confused about?
# I think I still need more practice using GitHub, such as pushing files

# 18) Tell me a fun fact!
# cows have accents :)

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)

print(18//4) #it returns the integer part of the quotient