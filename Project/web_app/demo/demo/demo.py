# *************************************************************************** #
#                                                                              #
#    demo.py                                                                   #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/21 12:32:10 by Widium                                    #
#    Updated: 2023/06/21 12:32:10 by Widium                                    #
#                                                                              #
# **************************************************************************** #

"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

from .state import SummaryState
from .component.description import create_model_description
from .component.api import create_api_key_input
from .component.input import create_input_box
from .component.output import create_output_box
from .style import DEMO_BOX_STYLE


def index()-> pc.Component:
    
    header = pc.vstack(
        pc.spacer(),
        pc.heading("Text Summarization"),
        spacing="1em",
    )
    
    description = create_model_description()
    api_key_box = create_api_key_input()
    input_box = create_input_box()
    output_box = create_output_box()
    
    content = pc.box(
        pc.vstack(
            api_key_box,
            input_box,
            output_box,
            spacing="3em",
        ),
        width="90%",
    )
    
    page = pc.vstack(
        header,
        description,
        content,
        pc.spacer(),
        pc.spacer(),
        spacing="3em",
    )
    
    # page._add_style(style=HOME_PAGE_STYLE)

    return (page)


app = pc.App(state=SummaryState)
app.add_page(index)
app.compile()

