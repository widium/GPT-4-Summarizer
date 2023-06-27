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

from time import sleep

from functions.utils.file import read_content

from model.api import verify_api_key, setup_api_key
from model.summarizer.core import TextSummarizerModel
from model.tokenization import count_tokens_in_message

DATA_PATH = Path("/home/widium/Programming/AI/GPT4-Summarizer/Project/prompt") 

ROLE_PATH = DATA_PATH / "role" / "simple_summarizer.txt"
MODEL = "gpt-3.5-turbo" #"text-davinci-003"

summarizer = TextSummarizerModel(
    model_version=MODEL,
    role_path=ROLE_PATH,
)

class SummaryState(pc.State):
    
    api_key : str = ""
    is_valid : bool = False
    content : str = ""
    summary : str = ""
    key_processing : bool = False
    processing : bool = False
    is_finish : bool = False
    nbr_tokens : int = 0
    
    def test_api_key(self):
        
        self.is_valid = False
        
        if (verify_api_key(api_key=self.api_key)):
            self.is_valid = True
            setup_api_key(key=self.api_key)
            
    def clear_api_key(self):
        self.api_key = ""
        self.is_valid = False
        
    def clear_content(self):
        self.content = ""
        
    def text_processing(self):
        
        self.processing = True 
        self.is_finish = False
        
        self.messages = summarizer.processing(
            content=self.content,
        )
    
    def count_token(self):
        
        self.nbr_tokens = 0
        
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
            self.processing = False
            self.is_finish = True
            return pc.window_alert("Error with OpenAI Execution. Verify your API KEY or OpenAI Status -> https://status.openai.com/")
        
    