import reflex as rx
import datetime
from linkBio.Components.linkIcon import link_icon
from linkBio.styles.styles import Size as Size
from linkBio.styles.colors import TextColor as TextColor
from linkBio.styles.colors import Color as Color
from linkBio.styles.fonts import Font as Font
import linkBio.constants as const

from linkBio.Components.infoText import info_text

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Saul Saez",
                size="xl",
                src="grAlpine.jpg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,

                border="5px",
                border_color=Color.PRIMARY.value,
                align_items="start",
            ),
            rx.vstack(
                rx.heading(
                    "Saul Saez", 
                    size="lg",
                    color = TextColor.HEADER.value,
                    font_family = Font.TITLE.value,
                ),
                rx.text(
                    "@SaezMD",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ), 
                rx.hstack(
                    link_icon(
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn icon for profile link"
                        ),
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub icon for profile link",
                        ),
                    spacing=Size.LARGE.value
                ),
                align_items="start"
            ),
            spacing=Size.SMALL.value
        ),
        
        rx.flex(
            info_text(
                f"+{experience()}",
                "years of experience"
            ),
            rx.spacer(),
            info_text(
                "C1",
                "English and Italian level"
            ),
            rx.spacer(),
            info_text(
                "+20",
                "software created"
            ),
            width="100%"
        ),

        rx.box(
            rx.text(
                f"""Welcome to my professional webpage 👋.""",
                color = TextColor.BODY.value,
                text_align="justify",
            ),
            rx.text(
                f"""I am Saul Saez, International senior professional with a demonstrated background in the telecommunications industry and logistics management.
                During the last {experience()} years I have been working as Software developer with Python scripts, Selenium, GitHub and Docker.""",
                color = TextColor.BODY.value,
                text_align="justify",
            ),
            rx.text(
                f""" Here you can find all my projects and contact information.""",
                color = TextColor.BODY.value,
                text_align="justify",
            ),
            #spacing=Size.SMALL.value,
            align_items="start",
            padding_top=Size.LARGE.value,
        ),
        align_items="start",
        padding_x = Size.SMALL.value,
    )

def experience() -> int:
    return datetime.date.today().year - 2020