from nicegui import ui
from components.header import header

@ui.page('/protocole')
def page():
    header()
    ui.label("Protocole de fabrication").classes('text-2xl text-black flex-grow text-center')
