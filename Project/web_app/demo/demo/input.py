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

import sys
sys.path.append("/home/widium/Programming/AI/GPT4-Summarizer/Project")

import pynecone as pc
from .state import SummaryState
from .style import DEMO_BOX_STYLE
from model.tokenization import TOKENS_LENGHT

def create_input_box()->pc.Component:
    
    heading = pc.center(pc.markdown("### Input Text", ))
    
    input_text = pc.text_area(
        placeholder="Paste Text Here", 
        on_blur=[SummaryState.set_content]
    )
    
    button = pc.button(
        "Summarize Text", 
        on_click=[
            SummaryState.text_processing, 
            SummaryState.count_token,
            SummaryState.summarization
        ],
    )
    
    conditional_color = pc.cond(
        condition=SummaryState.nbr_tokens > TOKENS_LENGHT,
        c1=pc.badge(SummaryState.nbr_tokens, variant="solid", color_scheme="red"),
        c2=pc.cond(
            condition=SummaryState.nbr_tokens > 3500,
            c1=pc.badge(SummaryState.nbr_tokens, variant="solid", color_scheme="yellow"),
            c2=pc.badge(SummaryState.nbr_tokens, variant="solid", color_scheme="green")
        )
    )
    
    render = pc.hstack(
        pc.text("Number of Tokens Detected :"), conditional_color,
    )
    
    tokens_counter = pc.cond(
        condition=SummaryState.content,
        c1=render,
    )
    
    stack = pc.vstack(
        heading,
        input_text,
        button,
        tokens_counter,
        spacing="3em",
    )
    
    box = pc.box(
        stack,
        style=DEMO_BOX_STYLE,
    )
    
    return (box)