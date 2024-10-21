# 1. Exploring Python's OS Module
# Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

# Task 1: Directory Inspector:

# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.

import os

def list_directory_contents(path):
    if os.path.exists(path):
        print(f"Here is whats in the current directory: {os.listdir(path)}")
    else:
        print("This path is not valid!")

def main_menu():
    while True:
        print("""
                |====Directory Menu====|
                   1. Enter Directory
                   2. Exit Application
            """)
        choice = input("Enter your choice: ")

        if choice == "1":
            new_path = input("Enter the directory you wish to access: ")
            list_directory_contents(new_path)
        elif choice == "2":
            print("Application is shutting down!")
            break
        else:
            print("Invalid Option! Please enter a proper choice")

main_menu()