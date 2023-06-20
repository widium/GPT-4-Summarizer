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

from .api import setup_api_key
from functions.utils.file import read_content

API_KEY = "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"

setup_api_key(key=API_KEY)

class TextSummarizerModel:
    
    def __init__(self, model_version : str, pre_prompt_path : str):
        
        self.model = model_version
        self.pre_prompting = read_content(filepath=pre_prompt_path)
    
    def processing(self, role_path : str, content : str):
        
        role = read_content(filepath=role_path)
        content = self.pre_prompting.replace("content", content)
        
        messages = [
            {"role" : "system", "content" : role},
            {"role" : "assistant", "content" : content},
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