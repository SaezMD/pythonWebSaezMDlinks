import reflex as rx
from linkBio.Components.title import title
from linkBio.Components.linkSponsor import link_sponsor
import linkBio.constants as const
from linkBio.styles.styles import Size as Size

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Sponsored by"),
           
        rx.flex(
            rx.box(link_sponsor(
                "logi.png",
                const.LOGITECH_URL,
                "LOGITECH icon"
            )),
            rx.spacer(),
            rx.box(link_sponsor(
                "oracle.png",
                const.ORACLE_URL,
                "Oracle icon"
            )),
            rx.spacer(),
            rx.box(link_sponsor(
                "amazon.png",
                const.AWS_URL,
                "Amazon web services icon"
            )),
            width="100%"
        ),
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value,
        )
