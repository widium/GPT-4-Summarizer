# *************************************************************************** #
#                                                                              #
#    evaluator.py                                                              #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/21 17:15:53 by Widium                                    #
#    Updated: 2023/06/21 17:15:53 by Widium                                    #
#                                                                              #
# **************************************************************************** #
import sys
sys.path.append("/home/widium/Programming/AI/GPT4-Summarizer/Project")

from typing import Any
from functions.utils.file import read_content
from functions.utils.file import renplace_token

class ToughtEvaluator:
    
    def __init__(self, prompt_file_path : str) -> None:
        
        self.prompt = read_content(filepath=prompt_file_path)
        
    def __call__(self, toughts : str, task : str) -> Any:
        
        self.prompt = renplace_token(
            prompt=self.prompt,
            token="<TASK>",
            value=task,
        )
        
        self.prompt = renplace_token(
            prompt=self.prompt,
            token="<SOLUTIONS>",
            value=toughts,
        )
        
        self.message = {"role" : "user", "content" : self.prompt}
        
        return (self.message)