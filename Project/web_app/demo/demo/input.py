# *************************************************************************** #
#                                                                              #
#    input.py                                                                  #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/16 17:01:15 by Widium                                    #
#    Updated: 2023/06/16 17:01:15 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import pynecone as pc
from .state import SummaryState
from .style import DEMO_BOX_STYLE

def create_input_box()->pc.Component:
    
    heading = pc.center(pc.markdown("### Input Text", ))
    
    input_text = pc.text_area(
        placeholder="Paste Text Here", 
        on_blur=SummaryState.set_content,
    )
    
    stack = pc.vstack(
        heading,
        input_text,
        spacing="3em",
    )
    
    box = pc.box(
        stack,
        style=DEMO_BOX_STYLE,
    )
    
    return (box)