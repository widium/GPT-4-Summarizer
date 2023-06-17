# *************************************************************************** #
#                                                                              #
#    output.py                                                                 #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/16 17:09:02 by Widium                                    #
#    Updated: 2023/06/16 17:09:02 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import pynecone as pc
from .state import SummaryState
from .style import DEMO_BOX_STYLE

def create_output_box()->pc.Component:
    
    heading = pc.center(pc.markdown("### Summary", ))
    
    output_text = pc.box(
        pc.markdown(
            SummaryState.summarization,
        ),
        style=DEMO_BOX_STYLE,
    )
    
    stack = pc.vstack(
        heading,
        output_text,
        spacing="3em",
    )
    
    box = pc.box(
        stack,
        style=DEMO_BOX_STYLE,
    )
    
    return (box)