# Python program to copy itself to another file

def copy_self():
    source_file = __file__  # Get the current script file name
    target_file = "copied_script.py"  # Name of the file to copy to

    try:
        with open(source_file, 'r') as src, open(target_file, 'w') as dest:
            dest.write(src.read())
        print(f"Script copied to '{target_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to copy the script
copy_self()
