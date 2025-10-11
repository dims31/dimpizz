from nicegui import ui
import pages.home, pages.protocole
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(favicon='🍕', title="Dim Pizza Calculator", port=8000)