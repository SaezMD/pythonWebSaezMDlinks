import reflex as rx
import linkBio.styles.styles as styles
from linkBio.styles.styles import Size as Size

def link_button(title: str, body: str, image: str, url: str) ->rx.Component:
    
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing=Size.SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                    text_align= "left",
                ),
                width="100%",
            )     
        ),
        href=url,
        is_external=True,
        width="100%",
    )
