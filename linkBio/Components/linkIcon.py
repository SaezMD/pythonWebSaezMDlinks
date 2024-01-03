import reflex as rx
from linkBio.styles.styles import Size as Size

def link_icon(image:str, url:str, alt:str) ->rx.Component:

    return rx.link(
        rx.image(
            src=image,
            width=Size.DEFAULT.value,
            alt=alt, 
        ),
        href=url,
        is_external=True,
    )