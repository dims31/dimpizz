from nicegui import ui

def header():
    with ui.header().classes('bg-[#FDF7E9] flex items-center justify-center font-mono'):
        with ui.link(target='/'):
            ui.image(source="static/logo_pizza.png").classes('w-16')
        ui.label("Dim Pizza Calculator").classes('text-2xl text-black flex-grow text-center')
