
import reflex as rx
from linkBio.styles.styles import Size as Size
import linkBio.styles.styles as styles
from linkBio.styles.colors import TextColor as TextColor
from linkBio.styles.colors import Color as Color

def navbar() -> rx.Component:
    return rx.hstack(
        #rx.spinner(color="white", size="md"),
        rx.box(
            rx.span("Saez",color=Color.PRIMARY.value ),
            rx.span("MD",color=Color.SECONDARY.value, font_weight= "bold" ),
            style=styles.navbar_title_style,
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index=999,
        top=0    
    )
