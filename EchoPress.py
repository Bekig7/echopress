import os
import random
import string

def secure_delete(file_path, passes=3):
    """
    Securely delete a file by overwriting it with random data before deletion.
    
    :param file_path: The path to the file to be deleted.
    :param passes: The number of times the file is overwritten.
    """
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} is not a valid file.")
        return False

    # Get the size of the file
    file_size = os.path.getsize(file_path)

    try:
        with open(file_path, "ba+", buffering=0) as f:
            # Overwrite the file with random data
            for _ in range(passes):
                f.seek(0)
                random_data = os.urandom(file_size)
                f.write(random_data)
                f.flush()
                os.fsync(f.fileno())

        # Rename the file to a random name
        new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        os.rename(file_path, new_name)

        # Delete the file
        os.remove(new_name)

        print(f"Successfully deleted {file_path} securely.")
        return True

    except Exception as e:
        print(f"An error occurred while deleting {file_path}: {e}")
        return False

if __name__ == "__main__":
    file_to_delete = input("Enter the path of the file you want to securely delete: ")
    secure_delete(file_to_delete)