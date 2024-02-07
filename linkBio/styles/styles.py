import reflex as rx
from enum import Enum
from linkBio.styles.colors import Color as Color
from linkBio.styles.colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import FontWeight 


# Constants
MAX_WIDTH = "620px"

#Style sheets (Fonts)
STYLESHEETS = [
   "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
   "https://fonts.googleapis.com/css2?family=Bitter:wght@500&display=swap",
]

# Sizes
class Size(Enum):
    ZERO= "0px !important"
    SMALL="0.5em" #em is the default by font size
    MEDIUM= "0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    VERY_BIG = "4em"

#Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color" : Color.BACKGROUND.value,
    
    rx.Heading:{    
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
    },
    
    rx.Button:{
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color" : Color.CONTENT.value,
        "white_space": "normal",
        "text_aling":"start",
        "_hover" : {
            "background_color" : Color.SECONDARY.value,
        }
    },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_size=Size.LARGE.value,
    font_family=Font.LOGO.value,
    font_weight= FontWeight.MEDIUM.value,
    )

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value,
    )

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    font_family= Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
    color = TextColor.HEADER.value,
)

button_body_style = dict(
    font_weight= FontWeight.LIGHT.value,
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value,
)
