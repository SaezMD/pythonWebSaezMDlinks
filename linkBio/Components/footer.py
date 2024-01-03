import reflex as rx
import datetime
from linkBio.styles.styles import Size as Size
from linkBio.styles.colors import TextColor as TextColor
from linkBio.styles.colors import Color as Color
import linkBio.constants as const

def footer() -> rx.Component:
    return rx.vstack(           
        rx.image(
            src="logo.jfif", 
            width=Size.VERY_BIG.value, 
            height="auto",
            border_radius=Size.SMALL.value,
            border="2px solid #555",
            box_shadow="lg",
            alt="Saul Saez icon with two \"S\" and one \"M\""
            ),
        rx.link(
            rx.box(
                f"© 2020-{datetime.date.today().year} ",
                rx.span(
                    "Saul Saez Muñoz",
                    color=Color.PRIMARY.value,
                    ),
                    " V-1."
                ),
            href=const.WEBPAGE_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
            ),
        rx.box(
                f"Creating Software and Automations with ",
                rx.span(
                "❤",
                font_weight="bold",
                color= Color.RED.value,
                font_size=Size.LARGE.value,
                ),
                f". Always GOOD vibes ♫",
                font_size=Size.MEDIUM.value,
                margin_top = Size.ZERO.value,     
            ),
        margin_bottom=Size.BIG.value,
        padding_bottom = Size.BIG.value,
        padding_x = Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color = TextColor.FOOTER.value
        )