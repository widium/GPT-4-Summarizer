"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

from .state import SummaryState
from .input import create_input_box
from .output import create_output_box

def index()-> pc.Component:
    
    header = pc.vstack(
        pc.spacer(),
        pc.spacer(),
        pc.heading("Text Summarization"),
    )

    input_box = create_input_box()
    output_box = create_output_box()
    
    content = pc.box(
        pc.vstack(
            input_box,
            output_box,
            spacing="3em",
        ),
        width="90%",
    )
    
    page = pc.vstack(
        header,
        content,
        spacing="3em",
    )
    
    # page._add_style(style=HOME_PAGE_STYLE)

    return (page)


app = pc.App(state=SummaryState)
app.add_page(index)
app.compile()

