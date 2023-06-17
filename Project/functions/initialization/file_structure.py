# *************************************************************************** #
#                                                                              #
#    file_structure.py                                                         #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/05/30 14:38:21 by Widium                                    #
#    Updated: 2023/05/30 14:38:21 by Widium                                    #
#                                                                              #
# **************************************************************************** #

from pathlib import Path 

def create_project_structure(root_name : str = "Project")-> None:
    """Create Structure of Folder and file for Pytorch Project

    Args:
        root_name (str): root name of project folder
    """
    readme = Path("README.md")
    readme.touch()
    
    ROOT_PATH = Path(f"{root_name}/")
    
    
    structure = {
        "web_app" : ["demo", "web_page"],
        "data" : ["raw", "processed", "dataset", "dataloader"],
        "models" : ["architecture", "saved"],
        "experiments" : [],
        "notebooks" : ["theorical", "eda", "preprocessing", "modeling", "training", "evaluation"],
        "functions" : ["utils", "dataset", "prediction", "visualization", "evaluation"],
        "tests" : [],    
        "docs" : [],
    }
    
    for parent_folder, child_folder in structure.items():
        
        parent_path = ROOT_PATH / parent_folder
        parent_path.mkdir(exist_ok=True, parents=True)
        
        for child_name in child_folder:
          
          child_path = parent_path / child_name
          child_path.mkdir(exist_ok=True, parents=True)
        
          
    return (ROOT_PATH)