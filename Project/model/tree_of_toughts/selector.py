# *************************************************************************** #
#                                                                              #
#    selector.py                                                               #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/21 17:15:47 by Widium                                    #
#    Updated: 2023/06/21 17:15:47 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append("/home/widium/Programming/AI/GPT4-Summarizer/Project")

from typing import Any
from functions.utils.file import read_content
from functions.utils.file import renplace_token

class ToughtSelector:
    
    def __init__(self, prompt_file_path : str) -> None:
        self.prompt = read_content(filepath=prompt_file_path)
    
    def __call__(self, toughts : str) -> Any:
        
        prompt = renplace_token(
            prompt=self.prompt,
            token="<SOLUTIONS>",
            value=toughts,
        )
        
        self.message = {"role" : "assistant", "content" : prompt}
        
        return (self.message)