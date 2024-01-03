import reflex as rx
from linkBio.Components.linkButton import link_button
from linkBio.Components.title import title
from linkBio.styles.styles import Size as Size
from linkBio.styles.fonts import Font as Font 
from linkBio.styles.colors import TextColor as TextColor
import linkBio.constants as const

def links() -> rx.Component:
    return rx.vstack(
        title("Links"),
        link_button(
            "LinkedIn", 
            "My professional CV.",
            "icons/linkedin.svg",  
            const.LINKEDIN_URL
        ),
        link_button(
            "GitHub",
            "My public code creations. For private scripts and development please contact me and I will show you.",
            "icons/github.svg", 
            const.GITHUB_URL
        ),
        link_button(
            "Amazon",
            "My AWS cloud creations for professional and personal use.",
            "icons/aws.svg",  
            const.AMAZON_URL
        ),
        link_button(
            "Oracle",
            "My Oracle deployment mainly for personal use.",
            "icons/cloud.svg", 
            const.ORACLE_URL
        ),

        title("Contact"),

        link_button(
            "Email",
            "Send an eMail to: saulsaezrodriguez@gmail.com",
            "icons/checkemail.svg", 
            f"mailto:{const.EMAIL}"
        ),
        link_button(
            "Phone",
            "Call me",
            "icons/phone.svg", 
            f"tel:{const.PHONE_NUMBER}"
        ),
        width="100%",
        spacing=Size.DEFAULT.value
    )