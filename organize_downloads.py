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
        print("Folder created successfully!: ", folder_name)


def move_file(path1: str, path2: str, file: str, folder_name: str) -> None:
    """
    Moves a file to a folder.

    Args:
        path1 (str): The path to the directory to move the file from.
        path2 (str): The path to the directory to move the file to.
        file (str): The name of the file to move.
        folder_name (str): The name of the folder to move the file to.

    Returns:
        None
    """
    file_path = os.path.join(path1, file)
    folder_path = os.path.join(path2, folder_name)
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
moving_path = os.path.join(who_am_i, "Desktop/downloadsArchive")
print(moving_path)

today = date.today()
today_folder_name = today.strftime("%Y-%m-%d")

# mapping of file extensions to folders
extensions_mapping = {
    "Images": [".jpg", ".png", ".jpeg", ".gif", ".webp", ".svg", ".heic"],
    "Sounds": [".mp3"],
    "Videos": [".mp4", ".mov"],
    "Documents": [".pdf", ".txt", ".docx", ".doc", ".xls", ".xlsx", ".pptx", ".ppt"],
    "Code": [".py", ".ipynb", ".html", ".js"],
    "Data": [".csv", ".json", ".xml"],
    "Installation": [".dmg", ".exe", ".pkg"],
    "Zips": [".zip", ".rar", ".tar"],
    "Torrents": [".torrent"],
}

# create folders
for folder_name in extensions_mapping.keys() | {"Others", "Folders"}:
    create_folder(os.path.join(moving_path, folder_name))

for file in os.listdir(downloads_path):
    file_to_move = os.path.join(downloads_path, file)
    if today - get_cretion_date(file_to_move) > timedelta(days=30):
        if os.path.isfile(file_to_move):
            file_extension = get_file_extension(file)
            folder_name = next(
                (
                    folder
                    for folder, ext_list in extensions_mapping.items()
                    if file_extension.lower() in ext_list
                ),
                "Others",
            )
            move_file(downloads_path, moving_path, file, folder_name)
            print(" :File moved successfully!: ", file)
        elif os.path.isdir(file_to_move):
            move_file(downloads_path, moving_path, file, "Folders")
            print(" :Folder moved successfully!: ", file)
