from nicegui import ui

def header():

    ui.add_head_html('''
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gochi+Hand&display=swap" rel="stylesheet">
''')

    with ui.header().classes('bg-[#FDF7E9] flex items-center justify-center font-GochiHand').style('font-family: "Gochi Hand", cursive;'):
        with ui.link(target='/'):
            ui.image(source="static/logo_pizza.png").classes('w-18')
        ui.label("Dim Pizza Calculator").classes('text-4xl text-black flex-grow text-center')
