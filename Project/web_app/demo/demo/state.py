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
from model.tokenization import count_tokens_in_message

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
    summary : str = ""
    processing : bool = False
    is_finish : bool = False
    nbr_tokens : int = 0
    
    def text_processing(self):
        
        self.processing = True 
        self.nbr_tokens = 0
        self.is_finish = False
        
        self.messages = summarizer.processing(
            role_path=ROLE_PATH,
            content=self.content,
        )
    
    def count_token(self):
        
        self.nbr_tokens = count_tokens_in_message(
            messages=self.messages,
            model=MODEL,
        )
        
        print(self.nbr_tokens)
        
    def summarization(self):
        
        try:
            self.summary = summarizer.summarize(messages=self.messages)
            self.processing = False
            self.is_finish = True
            
        except:
            self.image_processing = False
            return pc.window_alert("Error with OpenAI Execution.")
        
    