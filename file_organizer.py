import os.path
from datetime import date, datetime, timedelta


def get_cretion_date(file: str) -> date:
    """
    Get the creation date of a file.

    Args:
        file (str): The path to the file.

    Returns:
        datetime.date: The creation date of the file.
    """
    creation_time = datetime.fromtimestamp(int(os.path.getmtime(file)))
    creation_date = creation_time.date()
    return creation_date


def get_last_modification_date(file: str) -> date:
    """
    Returns the last modification date of a file.

    Args:
        file (str): The path to the file.

    Returns:
        date: The last modification date of the file.
    """
    last_modification_time = datetime.fromtimestamp(int(os.path.getctime(file)))
    last_modification_date = last_modification_time.date()
    return last_modification_date


def get_file_extension(file: str) -> str:
    """
    Returns the file extension of a file.

    Args:
        file (str): The path to the file.

    Returns:
        str: The file extension of the file.
    """
    file_extension = os.path.splitext(file)[1]
    return file_extension


def create_folder(folder_name: str) -> None:
    """
    Creates a folder if it does not exist.

    Args:
        folder_name (str): The name of the folder to create.

    Returns:
        None
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print("Folder created successfully!")


def move_file(path: str, file: str, folder_name: str) -> None:
    """
    Moves a file to a folder.

    Args:
        path (str): The path to the directory containing the file.
        file (str): The name of the file to move.
        folder_name (str): The name of the folder to move the file to.

    Returns:
        None
    """
    file_path = os.path.join(path, file)
    folder_path = os.path.join(path, folder_name)
    os.rename(file_path, os.path.join(folder_path, file))


def check_file_extension(file: str, file_extension_list: list) -> bool:
    """
    Checks if a file has an image extension.

    Args:
        file (str): The path to the file.

    Returns:
        bool: True if the file has an image extension, False otherwise.
    """
    file_extension = get_file_extension(file)
    if file_extension.lower() in file_extension_list:
        return True
    else:
        return False


who_am_i = os.path.expanduser("~")
downloads_path = os.path.join(who_am_i, "Downloads")

today = date.today()
today_folder_name = today.strftime("%Y-%m-%d")

# which folders to create
folders = [
    "Images",
    "Sounds",
    "Videos",
    "Documents",
    "Others",
    "Code",
    "Data",
    "Installation",
    "Zips",
    "Torrents",
    "Folders",
]
# define the file extensions
images = [".jpg", ".png", ".jpeg", ".gif", ".webp", ".svg", ".heic"]
sounds = [".mp3"]
videos = [".mp4", ".mov"]
documents = [".pdf", ".txt", ".docx", ".doc", ".xls", ".xlsx", ".pptx", ".ppt"]
code = [".py", ".ipynb", ".html", ".js"]
data = [".csv", ".json", ".xml"]
installation = [".dmg", ".exe", ".pkg"]
zips = [".zip", ".rar", ".tar"]
torrents = [".torrent"]

# create folders
for folder in folders:
    create_folder(downloads_path + "/" + folder)

# return all files as a list
for file in os.listdir(downloads_path):
    file_to_move = os.path.join(downloads_path, file)
    if today - get_cretion_date(file_to_move) > timedelta(days=30):
        # check the files which are end with specific extension
        # and move them to the corresponding folder
        if os.path.isfile(file_to_move):
            print(" :File moved successfully!: ", file)
            if check_file_extension(file, images):
                move_file(downloads_path, file, "Images")
            elif check_file_extension(file, sounds):
                move_file(downloads_path, file, "Sounds")
            elif check_file_extension(file, videos):
                move_file(downloads_path, file, "Videos")
            elif check_file_extension(file, documents):
                move_file(downloads_path, file, "Documents")
            elif check_file_extension(file, code):
                move_file(downloads_path, file, "Code")
            elif check_file_extension(file, data):
                move_file(downloads_path, file, "Data")
            elif check_file_extension(file, installation):
                move_file(downloads_path, file, "Installation")
            elif check_file_extension(file, zips):
                move_file(downloads_path, file, "Zips")
            elif check_file_extension(file, torrents):
                move_file(downloads_path, file, "Torrents")
            else:
                move_file(downloads_path, file, "Others")
        elif os.path.isdir(file_to_move):
            move_file(downloads_path, file, "Folders")
