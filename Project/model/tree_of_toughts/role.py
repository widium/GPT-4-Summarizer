# *************************************************************************** #
#                                                                              #
#    role.py                                                                   #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/22 12:39:03 by Widium                                    #
#    Updated: 2023/06/22 12:39:03 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append("/home/widium/Programming/AI/GPT4-Summarizer/Project")

from typing import Any
from functions.utils.file import read_content
from functions.utils.file import renplace_token


class RoleCreator:
    
    def __init__(
        self, 
        main_role_path : str,
        speciality_path : str,
    ) -> None:
        
        role = read_content(filepath=main_role_path)
        speciality = read_content(filepath=speciality_path)
        
        self.role = renplace_token(
            prompt=role,
            token="<SPECIALITY>",
            value=speciality,
        )
    
    
    def __call__(self) -> Any:
        
        self.message = {"role" : "system", "content" : self.role}
        
        return (self.message)

