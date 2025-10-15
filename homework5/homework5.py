##---3.1 VOCABULARY REVIEW---
"""
1. Git is the software installed locally on the computer, while GitHub is a a cloud service, that hosts Git repositories for collaboration and backup (remote)
2. Command line is the text-based user interference for executing commands. The terminal is the program that launches and hosts theCommand live encvironment
3. A Local Repository is the complete copy of the project's codebase and history stored on your computer; a Remote Repository is the copy hosted on an external server (like GitHub) used for backup and team collaboration.
4. Version Control is a system that records changes to a file or set of files over time so you can recall specific versions later, allowing developers to track and merge contributions efficiently.
5. Staging area is an intermediate area (or index) in Git where you prepare and group changes before committing them; it allows you to select exactly which changes will be part of the next commit.
6. git add: command that moves changes from the working directory to the Staging Area, marking them to be included in the next commit.
7. git commit: command that permanently records the staged changes into the local repository's history, usually along with a descriptive message
8. git push: command that uploads your local repository's committed history and branches to the designated Remote Repository
9. git status: command that displays the state of the working directory and the staging area, showing which files are tracked, modified, staged, or untracked.
10. git pull: command that fetches changes from the Remote Repository and immediately merges them into your current local branch
11. pwd: command (Print Working Directory) that displays the full path of the current directory you are in within the file system.
12. ls: command (List Segments/Contents) that lists the files and directories inside the current directory.
13 cd: command (Change Directory) that is used to navigate to a different directory in the file system.
14. nano: command that launches a simple, easy-to-use, command-line text editor to create or modify files.
15. touch: command that creates a new, empty file; if the file already exists, it updates the file's access and modification timestamps.
16. mv: command (Move) that is used to move a file or directory from one location to another, or to rename a file or directory.
17. rm: command (Remove) that is used to delete files or directories from the file system.
18. cat: command (Concatenate) that reads file contents and outputs them to the terminal screen, commonly used to quickly view the contents of a file.

"""

## --3.2 Directory Tree--
"""
1.pwd
2. ls
3.cd ..
  cd brianna_repo
  git pull
4. mv homework.py ../judy_decal/homework/
5. cd ~/python_decal/brianna_repo
   cd ~/python_decal/judy_decal/homework/
6. cat homework.py
7. git add .
   git commit -m "Finished week's homework"
   git push
8. What it means: Judy failed to ensure her local repository was up-to-date with the remote before trying to push her own changes. This prevents her work from overwriting the remote changes.
   Commands to resolve: You must integrate the remote changes first using git pull, and then try the git push again.
9. cd ~/Recent/
"""

##--- DATA TYPES---
#4.1
def check_data_type(value):
    return{type(value)}

print(check_data_type(3.14))
print(check_data_type(True))

#4.2 Conditionals
def even_or_odd(num):
    if num% 2==0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(7))
print(even_or_odd(10))

##---LOOPS---
def sum_with_loop(numbers):
    total =0
    for num in numbers:
        total = total + num
    return total

numbers=[1, 2, 3,4, 5]
print(sum_with_loop(numbers))

##---HOMEWORK 4 REVIEW---
#--6.1 Lists--
def duplicate(lst):
    new_list=[]
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list

duplicatelist=["a", "b", "c"]

print(duplicate(duplicatelist))

#--6.2 Debugging--
def square(num):
    return num**2
print(square(5))



##7 IN YOUR VS CODE TERMINAL

#Fav problem:
def even_or_odd(num):
    if num% 2==0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(49))
