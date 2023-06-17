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

def setup_api_key(key : str):
    openai.api_key = key