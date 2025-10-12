from nicegui import ui
from components.header import header

@ui.page('/protocole')
def page():
    header()
    ui.colors(primary='#555')
    with ui.stepper().props('vertical').classes('w-full') as stepper:
        with ui.step('Pétrissage'):
            ui.label("Ajouter dans l'eau à température ambiante la levure et le sel. Mélanger jusqu'à dissolution complète.")
            ui.label("Ajouter la farine et l'huile. Mélanger jusqu'à obtenir une pâte homogène.")
            ui.label("Pétrisser la pâte pendant 10 minutes.")
            with ui.stepper_navigation():
                ui.button('Suivant', on_click=stepper.next)
        with ui.step('Pointage'):
            ui.label("Laisser la pâte reposer pendant 3 heures à température ambiante dans un saladier couvert d'un film étirable.")
            with ui.stepper_navigation():
                ui.button('Suivant', on_click=stepper.next)
                ui.button('Retour', on_click=stepper.previous).props('flat')
        with ui.step('Boulage'):
            ui.label('Faire des boules de pâte de la taille désirée (250g pour une pizza de 30cm).')
            ui.label('Laisser reposer les boules de pâte à température ambiante ou température contrôlée (4°C) selon le protocole choisi.')
            with ui.stepper_navigation():
                ui.button('Suivant', on_click=stepper.next)
                ui.button('Retour', on_click=stepper.previous).props('flat')
        with ui.step('Cuisson'):
            ui.label('Préchauffer le four à 400°C')
            ui.label('Cuire les pizzas pendant 3 minutes ou jusqu\'à ce qu\'elles soient dorées.')
            with ui.stepper_navigation():
                ui.button('Terminé', on_click=lambda: ui.notify('Buon appetito!', type='positive')) 
                ui.button('Retour', on_click=stepper.previous).props('flat')
