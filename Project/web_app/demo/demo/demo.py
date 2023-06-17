"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

from .state import SummaryState
from .input import create_input_box
from .output import create_output_box

def index()-> pc.Component:
    
    header = pc.heading("Text Summarization")

    input_box = create_input_box()
    output_box = create_output_box()
    
    
    box = pc.box(
        pc.vstack(
            input_box,
            output_box,
            spacing="3em",
    #     # style=DEMO_BOX_STYLE,
        ),
        width="90%",
    )
    
    page = pc.vstack(
        header,
        box,
        spacing="3em",
    )
    
    # page._add_style(style=HOME_PAGE_STYLE)

    return page


# Add state and page to the app.
app = pc.App(state=SummaryState)
app.add_page(index)
app.compile()
