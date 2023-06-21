# *************************************************************************** #
#                                                                              #
#    api.py                                                                    #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/20 17:01:20 by Widium                                    #
#    Updated: 2023/06/20 17:01:20 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import pynecone as pc

from .state import SummaryState
from .style import DEMO_BOX_STYLE

def create_api_key_input():
    
    buttons = pc.hstack(
        pc.button(
            "Submit", on_click=SummaryState.test_api_key,
        ),
        pc.button(
            "Clear", on_click=SummaryState.clear_api_key,
        ),
    )
    
    response = pc.cond(
        condition=SummaryState.is_valid,
        c1=pc.badge("API KEY is valid !", variant="solid", color_scheme="green"),
        c2=pc.badge("API KEY is not valid...", variant="solid", color_scheme="red"),
    )
            
    stack = pc.vstack(
        pc.markdown("### OpenAI API KEY"),
        pc.input(
            value=SummaryState.api_key,
            on_change=SummaryState.set_api_key,
        ),
        buttons,
        response,
        spacing="2em",
    )
    
    box = pc.box(
        stack,
        style=DEMO_BOX_STYLE,
    )
        
    return (box)



    
