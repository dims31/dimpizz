from nicegui import ui

class Pate:
    def __init__(self, qte_pate, hydra_pct, duree_ferment, temp_ferment, type_levure, qte_sel_par_kg, huile_pct):
        self.qte_pate = qte_pate
        self.hydra_pct = hydra_pct
        self.duree_ferment = duree_ferment
        self.temp_ferment = temp_ferment
        self.type_levure = type_levure
        self.qte_sel_par_kg = qte_sel_par_kg
        self.huile_pct = huile_pct
        self.qte_far = 0
        self.qte_eau = 0
        self.qte_levure = 0
        self.qte_sel = 0
        self.qte_huile = 0
        self.calc_quantite()

    def levure_par_kg(self):

        CONST_LEVURE = 300
        
        if self.type_levure == "fraiche":
            ratio_levure = 1
        elif self.type_levure == "seche":
            ratio_levure = 0.33
        else:
            raise ValueError("type de levure inconnu")
        return ratio_levure * CONST_LEVURE / (self.temp_ferment * self.duree_ferment)

    def calc_quantite(self):
        coef_total = 1 + (self.hydra_pct / 100) + (self.qte_sel_par_kg + self.levure_par_kg()) / 1000
        self.qte_far = self.qte_pate / coef_total
        self.qte_eau = (self.hydra_pct - self.huile_pct) * self.qte_far / 100
        self.qte_levure = self.levure_par_kg() * self.qte_far / 1000
        self.qte_sel = self.qte_sel_par_kg * self.qte_far / 1000
        self.qte_huile = self.huile_pct * self.qte_far / 100


def temp_moyenne(temp1,temp2,duree1,duree2):
    return (temp1*duree1 + temp2*duree2)/(duree1+duree2)


def create_pizza():
    return Pate(
        qte_pate=nombre_patons.value * poids_paton.value,
        hydra_pct=hydra_pct_input.value,
        duree_ferment=duree_ferment_tc_input.value + duree_ferment_ta_input.value,
        temp_ferment=temp_moyenne(
            temp_ferment_ta_input.value,
            temp_ferment_tc_input.value,
            duree_ferment_ta_input.value,
            duree_ferment_tc_input.value),
        type_levure=type_levure_input.value,
        qte_sel_par_kg=qte_sel_par_kg_input.value,
        huile_pct=huile_pct_input.value
    )


with ui.header().classes('bg-[#FDF7E9] flex items-center justify-center font-mono'):
    ui.image(source="logo_pizza.png").classes('w-16')
    ui.label("Dim Pizza Calculator").classes('text-2xl text-black flex-grow text-center')

nombre_patons = ui.select([1,2,3,4,5,6,7,8,9,10], value=4, label='Nombre de patons', with_input=True, on_change=lambda e: update_labels()).classes('w-full')
poids_paton = ui.number(value=250, label='Poids par paton (g)', step=5, on_change=lambda e: update_labels()).classes('w-full')
hydra_pct_input = ui.number(value=65, label="Pourcentage d'hydratation (%)",on_change=lambda e: update_labels()).classes('w-full')
huile_pct_input = ui.number(value=2.5, step=0.5, label="Pourcentage d'huile (%)",on_change=lambda e: update_labels()).classes('w-full')

ui.label("Fermentation température ambiante:")
with ui.row():
    duree_ferment_ta_input = ui.number(value=4, label='Durée (h)',on_change=lambda e: update_labels()).classes('w-[100px]')
    temp_ferment_ta_input = ui.number(value=20, label='Température (°C)',on_change=lambda e: update_labels()).classes('w-[100px]')
ui.label("Fermentation température contrôlée:")
with ui.row():
    duree_ferment_tc_input = ui.number(value=24, label='Durée (h)',on_change=lambda e: update_labels()).classes('w-[100px]')
    temp_ferment_tc_input = ui.number(value=6, label='Température (°C)',on_change=lambda e: update_labels()).classes('w-[100px]')
type_levure_input = ui.select(['fraiche', 'seche'], value="fraiche", label='Type de levure',on_change=lambda e: update_labels()).classes('w-full')
qte_sel_par_kg_input = ui.number(value=25, label='Quantité de sel par kg de farine (g)',on_change=lambda e: update_labels()).classes('w-full')


qte_pate_label = ui.label(text="Quantité de pâte : 0.00 g").classes('text-lg font-mono w-full text-center mt-4 bg-[#FDF7E9] p-1 rounded')
with ui.element('div').classes('columns-3 w-full gap-2 '):
        tailwind = f'mb-2 p-2 h-50px] break-inside-avoid bg-[#FDF7E9]'
        with ui.card().classes(tailwind):
            qte_farine_label = ui.label(text="")
        with ui.card().classes(tailwind):
            qte_eau_label = ui.label(text="")
        with ui.card().classes(tailwind):
            qte_levure_label = ui.label(text="")
        with ui.card().classes(tailwind):
            qte_sel_label = ui.label(text="")
        with ui.card().classes(tailwind):
            qte_huile_label = ui.label(text="")

def update_labels():
    pizza = create_pizza()
    qte_pate_label.text = f"Pour {pizza.qte_pate:.0f} g de pate :"
    qte_farine_label.text = f"Farine : {pizza.qte_far:.0f} g"
    qte_eau_label.text = f"Eau : {pizza.qte_eau:.0f} g"
    qte_levure_label.text = f"Levure : {pizza.qte_levure:.2f} g"
    qte_sel_label.text = f"Sel : {pizza.qte_sel:.0f} g"
    qte_huile_label.text = f"Huile : {pizza.qte_huile:.0f} g"

    # Initial update
update_labels()

ui.run(favicon='🍕', title="Dim's Pizza Calculator",port=8000)