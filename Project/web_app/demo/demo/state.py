# *************************************************************************** #
#                                                                              #
#    state.py                                                                  #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/16 17:05:24 by Widium                                    #
#    Updated: 2023/06/16 17:05:24 by Widium                                    #
#                                                                              #
# **************************************************************************** #
import sys
sys.path.append("/home/widium/Programming/AI/GPT4-Summarizer/Project")

import pynecone as pc
from pathlib import Path
from model.core import TextSummarizerModel

DATA_PATH = Path("/home/widium/Programming/AI/GPT4-Summarizer/Project/prompt") 

ROLE_PATH = DATA_PATH / "role" / "role.txt"
PRE_PROMPT_PATH = DATA_PATH / "role" / "pre-prompt.txt"
MODEL = "gpt-3.5-turbo" #"text-davinci-003"

summarizer = TextSummarizerModel(
    model_version=MODEL,
    pre_prompt_path=PRE_PROMPT_PATH,
)

class SummaryState(pc.State):
    
    content : str = ""
    
    @pc.var
    def summarization(self):
        
        if self.content :
            summary = summarizer.summarize(
                role_path=ROLE_PATH,
                content=self.content,
            )
            return (summary)