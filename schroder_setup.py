"""
Module: schroder_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Justin Schroder
"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
# TODO: Import additional modules as needed
import pathlib
import time

# Import local modules
import utils_schroder 

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.

    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    # Loop through each year in the range
    for year in range(start_year, end_year + 1):
        # Create the path for the year folder
        year_folder = data_path.joinpath(str(year))

        # Create the folder (if it doesn’t already exist)
        year_folder.mkdir(exist_ok=True)
        # Log the folder creation
        print(f"Created folder: {year_folder}")

#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase=False, remove_spaces=False) -> None:
    '''
    Create folders from a list of folder names, with optional transformations.

    Arguments:
    folder_list -- A list of folder names to create.
    to_lowercase -- Whether to convert the folder names to lowercase (default: False).
    remove_spaces -- Whether to remove spaces from the folder names (default: False).
    '''
    # Log the function call and its arguments
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}, to_lowercase={to_lowercase}, remove_spaces={remove_spaces}")

    # Loop through each folder name in the list
    for folder_name in folder_list:
        # Apply transformations if options are set
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "")

        # Create the path for the folder
        folder_path = data_path.joinpath(folder_name)

        # Create the folder (if it doesn’t already exist)
        folder_path.mkdir(exist_ok=True)
        # Log the folder creation
        print(f"Created folder: {folder_path}")

  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create folders by adding a prefix to each name in the folder list.

    Arguments:
    folder_list -- A list of folder names to transform and create.
    prefix -- The prefix to add to each folder name.
    '''
    # Log the function call and its arguments
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix='{prefix}'")

    # Use a list comprehension to create full folder names with the prefix
    prefixed_folders = [f"{prefix}{folder_name}" for folder_name in folder_list]

    # Loop through each prefixed folder name and create the folder
    for folder_name in prefixed_folders:
        # Create the path for the folder
        folder_path = data_path.joinpath(folder_name)

        # Create the folder (if it doesn’t already exist)
        folder_path.mkdir(exist_ok=True)
        # Log the folder creation
        print(f"Created folder: {folder_path}")

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders periodically by waiting for the specified duration between each folder creation.

    Arguments:
    duration_seconds -- The wait time in seconds between folder creation attempts.
    '''
    # Log the function call and its arguments
    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}")

    # Loop to create a folder every duration_seconds seconds
    for i in range(5):  # Create 5 folders as an example (you can adjust this)
        # Generate a folder name (e.g., folder1, folder2, etc.)
        folder_name = f"folder{i+1}"

        # Create the path for the folder
        folder_path = data_path.joinpath(folder_name)

        # Create the folder (if it doesn’t already exist)
        folder_path.mkdir(exist_ok=True)
        # Log the folder creation
        print(f"Created folder: {folder_path}")

        # Wait for the specified duration before creating the next folder
        time.sleep(duration_seconds)
   
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options to force lowercase and remove spaces
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    # Call the function to create folders with additional options
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.
