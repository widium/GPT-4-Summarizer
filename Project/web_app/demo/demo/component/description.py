# *************************************************************************** #
#                                                                              #
#    description.py                                                            #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/20 16:48:00 by Widium                                    #
#    Updated: 2023/06/20 16:48:00 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import pynecone as pc

def create_model_description():
    
    infos = pc.list(
        pc.list_item(
            pc.icon(tag="settings", color="grey"), "  Max Number of Tokens : 4096"
        ),
        pc.list_item(
            pc.icon(tag="info", color="blue"), "  Model : gpt-3.5-turbo",
        ),
        spacing=".25em",
    )
    
    return (infos)