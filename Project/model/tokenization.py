# *************************************************************************** #
#                                                                              #
#    tokenization.py                                                           #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/20 15:43:42 by Widium                                    #
#    Updated: 2023/06/20 15:43:42 by Widium                                    #
#                                                                              #
# **************************************************************************** #

from typing import List, Dict
import tiktoken

TOKENS_LENGHT = 4096

def count_tokens_in_message(
    messages : List[Dict],
    model : str ="gpt-3.5-turbo-0613"
)->int:
    """Returns the number of tokens used by a list of messages."""
    try:
        encoder = tiktoken.encoding_for_model(model)
    except KeyError:
        encoder = tiktoken.get_encoding("cl100k_base")
    
    num_tokens = 0
    for message in messages:
        num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        
        for key, value in message.items():
            num_tokens += len(encoder.encode(value))
            if key == "name":  # if there's a name, the role is removed
                num_tokens += -1  # role is always required and always 1 token
    
    num_tokens += 2  # every reply is primed with <im_start>assistant
    
    return (num_tokens)