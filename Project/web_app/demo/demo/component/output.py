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
from ..state import SummaryState
from ..style import DEMO_BOX_STYLE

def create_output_box()->pc.Component:
    
    heading = pc.center(pc.markdown("### Summary", ))
    
    output_text = pc.box(
        pc.markdown(SummaryState.summary),
        style=DEMO_BOX_STYLE,
    )
    
    loading_render = pc.stack(
        pc.center(pc.circular_progress(is_indeterminate=True)),
        pc.skeleton_circle(size="30px"),
        pc.skeleton_text(no_of_lines=8),
        width="50%",
    )
    
    
    output = pc.cond(
        condition=SummaryState.processing,
        c1=loading_render,
        c2=pc.cond(
            condition=SummaryState.is_finish,
            c1=output_text,
        ),
    )
    
    stack = pc.vstack(
        heading,
        output,
        spacing="3em",
    )
    
    box = pc.box(
        stack,
        style=DEMO_BOX_STYLE,
    )
    
    return (box)