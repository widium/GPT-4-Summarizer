# *************************************************************************** #
#                                                                              #
#    core.py                                                                   #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/16 15:00:21 by Widium                                    #
#    Updated: 2023/06/16 15:00:21 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append("/home/widium/Programming/AI/GPT4-Summarizer/Project")

from typing import List, Dict
from openai import Completion
from openai import ChatCompletion

from functions.utils.file import read_content
from functions.utils.file import renplace_token

class TextSummarizerModel:
    
    def __init__(self, model_version : str, role_path : str):
        
        self.model = model_version
        self.role = read_content(filepath=role_path)
    
    def processing(self, content : str):
        
        prompt = renplace_token(
            prompt=self.role,
            token="<CONTENT>",
            value=content,
        )
        
        messages = [
            {"role" : "system", "content" : prompt},
        ]
        
        return (messages)
        
    def summarize(self, messages : List[Dict])->str:

        generations = ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=0
        )
        
        print(generations)

        summary = generations.choices[0]["message"]["content"]

        return (summary)