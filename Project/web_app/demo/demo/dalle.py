"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc
import openai

openai.api_key = "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"


class State(pc.State):
    """The app state."""

    prompt = ""
    image_url = ""
    image_processing = False
    image_made = False

    def process_image(self):
        """Set the image processing flag to true and indicate that the image has not been made yet."""
        self.image_made = False
        self.image_processing = True

    def get_image(self):
        """Get the image from the prompt."""
        try:
            response = openai.Image.create(prompt=self.prompt, n=1, size="1024x1024")
            self.image_url = response["data"][0]["url"]
            # Set the image processing flag to false and indicate that the image has been made.
            self.image_processing = False
            self.image_made = True
        except:
            self.image_processing = False
            return pc.window_alert("Error with OpenAI Execution.")


def index():
    
    header = pc.heading("DALL-E", font_size="1.5em")
    
    prompt = pc.input(
        placeholder="Enter a prompt..", 
        on_blur=State.set_prompt
    )
    
    button = pc.button(
        "Generate Image",
        on_click=[State.process_image, State.get_image],
        width="100%",
    )
    
    conditionnal_rending = pc.cond(
        condition=State.image_processing,
        c1=pc.circular_progress(is_indeterminate=True),
        c2=pc.cond(
            condition=State.image_made,
            c1=pc.image(
                src=State.image_url,
                height="25em",
                width="25em",
            ),
        ),
    )
    
    stack = pc.vstack(
        header,
        prompt,
        button,
        pc.divider(),
        conditionnal_rending,
        bg="white",
        padding="2em",
        shadow="lg",
        border_radius="lg",
    )
    
    page = pc.center(
        stack,
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )
    
    return (page)


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, title="Pynecone:DALL-E")
app.compile()