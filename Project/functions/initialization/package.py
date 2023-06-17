# *************************************************************************** #
#                                                                              #
#    package.py                                                                #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/05/30 14:35:28 by Widium                                    #
#    Updated: 2023/05/30 14:35:28 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import subprocess
import shutil
from pathlib import Path
from urllib.parse import urlparse

def extract_folder(parent_folder : str, target_folder_name : str, destination : str):
    """
    Extract Folder and his content to other location and remove the parent folder

    Args:
        `parent_folder` (str): parent folder of target folder
        `target_folder_name` (str): target folder we want to extract
        `destination` (str): destination of target folder extracted
    
    Return :
        new path of target folder
    """
    parent_folder = Path(parent_folder)
    destination = Path(destination)
    
    folders = [
        item.name 
        for item in parent_folder.iterdir() 
        if item.is_dir()
    ]
    
    for name in folders:
        
        if name == target_folder_name:
            target_folder_path = parent_folder / name
            shutil.move(src=str(target_folder_path), dst=str(destination))
            print(f"[INFO] : Moove [{target_folder_path}] to [{destination / target_folder_name}]")
    
    shutil.rmtree(str(parent_folder))
    print(f"[INFO] : Remove [{parent_folder}]")
    
    return (str(destination / target_folder_name))



def clone_repository(
    repository_url : str,
    destination_folder: str = "Project/src/",
):
    """
    Clone git repository inside a destination folder

    Args:
        repository_url (str): https url of the repository
        destination_folder (str, optional): destination folder. Defaults to "Project/src/".

    Raises:
        FileNotFoundError: if the destination folder doesn't exist
        FileExistsError: if the repository already exist in destination

    Returns:
        Path: path of cloned repository
    """
    destination_folder = Path(destination_folder)
    url_path = urlparse(repository_url).path
    repository_name = Path(url_path).stem
    
    if not destination_folder.exists():
        raise FileNotFoundError(f"destination_folder doesn't exist : [{destination_folder}]")

    repository_dest_path = destination_folder / repository_name

    # Check if the new folder is empty
    if repository_dest_path.exists():
        raise FileExistsError(f"{repository_dest_path} already exists. Please remove it or choose a different location.")

    # Clone the repository into the new folder
    subprocess.run(["git", "clone", repository_url, str(repository_dest_path)])
    
    return (repository_dest_path)


def import_package(destination_folder : str = "Project/src/"):
    
    repository = {
        # "repository url" : "package name"
        "https://github.com/widium/Pytorch-Model-Archiver.git" : "archive",
        "https://github.com/widium/Pytorch-Training-Toolkit.git" : "training",
        "https://github.com/widium/Pytorch_Experiment_Framework.git" : "saver",
    }
    
    for repos_url, package_name in repository.items():
        
        repos_path = clone_repository(
            repository_url=repos_url,
            destination_folder=destination_folder,
        )
        
        # extract package inside repos and remove repository folder 
        extract_folder(
            parent_folder=repos_path,
            target_folder_name=package_name,
            destination=destination_folder,
        )