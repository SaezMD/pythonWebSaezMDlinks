"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from linkBio.Components.navbar import navbar
from linkBio.Components.footer import footer
from linkBio.views.header.header import header
from linkBio.views.links.links import links
from linkBio.views.sponsors.sponsors import sponsors
import linkBio.styles.styles as styles
from linkBio.styles.styles import Size as Size


#class State(rx.State):
#    """The app state."""
#    pass

def index() -> rx.Component:

    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                #sponsors(), remove until next update
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value
            )),
        footer()
    )

# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,

)
app.add_page(
    index,
    title="SaezMD | Software Developer",
    description= "International Software Developer with a demonstrated background in the telecommunications industry and logistics management.",
    image="logo.jfif"
)
app.compile()
