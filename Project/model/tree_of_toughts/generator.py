# *************************************************************************** #
#                                                                              #
#    generator.py                                                              #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/21 17:15:51 by Widium                                    #
#    Updated: 2023/06/21 17:15:51 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append("/home/widium/Programming/AI/GPT4-Summarizer/Project")

from typing import Any
from functions.utils.file import read_content
from functions.utils.file import renplace_token

class ToughtGenerator:
    def __init__(
        self, 
        init_prompt_path : str,
        generator_prompt_path : str, 
        nbr_to_generate : int = 3,
    ) -> None:
        
        self.nbr_to_generate = nbr_to_generate
         
        self.init_prompt = read_content(filepath=init_prompt_path)
        self.prompt = read_content(filepath=generator_prompt_path)
        
    def processing_init_prompt(self, prompt : str, nbr_to_generate : int):
        
        prompt = renplace_token(
            prompt=prompt,
            token="<NBR_TO_GENERATE>",
            value=str(nbr_to_generate),
        )
        
        return (prompt)
    
    def processing_prompt(self, prompt : str, previous_winner : str, nbr_to_generate : int):
        
        
        prompt = renplace_token(
            prompt=prompt,
            token="<NBR_TO_GENERATE>",
            value=str(nbr_to_generate - 1),
        )
        
        prompt = renplace_token(
            prompt=prompt,
            token="<PREVIOUS_WINNER>",
            value=previous_winner,
        )
        
        return (prompt)
        
    
    def __call__(self, task : str, previous_winner : str = None) -> Any:
        

        if (previous_winner == None):
            prompt = self.processing_init_prompt(
                prompt=self.init_prompt,
                nbr_to_generate=self.nbr_to_generate,
            )
        
        else :
            prompt = self.processing_prompt(
                prompt=self.prompt,
                previous_winner=previous_winner,
                nbr_to_generate=self.nbr_to_generate,
            )
        
        prompt = renplace_token(
            prompt=prompt,
            token="<TASK>",
            value=task,
        )
        
        self.messages = {"role" : "assistant", "content" : prompt}
        
        return (self.messages)