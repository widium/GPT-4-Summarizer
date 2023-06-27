# *************************************************************************** #
#                                                                              #
#    file.py                                                                   #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/16 14:56:09 by Widium                                    #
#    Updated: 2023/06/16 14:56:09 by Widium                                    #
#                                                                              #
# **************************************************************************** #

from typing import List 
from pathlib import Path

def read_content(filepath : str)->str:
    """
    Reads the content of a text file at the specified file path.

    1. Converts the provided file path to a Path object.
    2. Checks if the file exists at the given path.
       - If the file doesn't exist, it raises a FileExistsError with a descriptive message.
    3. Reads the content of the file using the `read_text` method from the `Path` class.
    4. Returns the content of the file.

    Args:
        filepath (str): The file path of the text file.

    Returns:
        str: The content of the text file.

    Raises:
        FileExistsError: If the file doesn't exist at the given file path.
    """
    path = Path(filepath)
    
    if not path.exists():
        raise FileExistsError(f"{path} doesn't exist...")
    
    content = path.read_text()
    
    return (content)

def renplace_token(prompt : str, token : str, value : str):
    prompt = prompt.replace(token, value)
    return (prompt)

def verify_file_path(filepaths : List[Path]):
   
    for path in filepaths:
        if not path.exists():
            raise FileNotFoundError(f"{path} doesn't already exist...")
        else:
            print(f"[INFO] : {path} already exist")

    