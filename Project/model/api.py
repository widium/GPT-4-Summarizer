# *************************************************************************** #
#                                                                              #
#    api.py                                                                    #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/16 15:02:19 by Widium                                    #
#    Updated: 2023/06/16 15:02:19 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import openai   
from openai import ChatCompletion

def setup_api_key(key : str):
    openai.api_key = key
    
def verify_api_key(api_key : str):
    
    openai.api_key = api_key

    try:
        _ = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Write 'All test Passed'"},
            ]
        )
        return (True)
    
    except Exception as e:
        return (False)