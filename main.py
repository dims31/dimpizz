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
        if self.type_levure == "fraiche":
            ratio_levure = 1
        elif self.type_levure == "seche":
            ratio_levure = 0.33
        else:
            raise ValueError("type de levure inconnu")
        CONST_LEVURE = 300
        return ratio_levure * CONST_LEVURE / (self.temp_ferment * self.duree_ferment)

    def calc_quantite(self):
        coef_total = 1 + (self.hydra_pct / 100) + (self.qte_sel_par_kg + self.levure_par_kg()) / 1000
        self.qte_far = self.qte_pate / coef_total
        self.qte_eau = (self.hydra_pct - self.huile_pct) * self.qte_far / 100
        self.qte_levure = self.levure_par_kg() * self.qte_far / 1000
        self.qte_sel = self.qte_sel_par_kg * self.qte_far / 1000
        self.qte_huile = self.huile_pct * self.qte_far / 100


def create_pizza():
    return Pate(
        qte_pate=nombre_patons.value * poids_paton.value,
        hydra_pct=hydra_pct_input.value,
        duree_ferment=duree_ferment_input.value,
        temp_ferment=temp_ferment_input.value,
        type_levure=type_levure_input.value,
        qte_sel_par_kg=qte_sel_par_kg_input.value,
        huile_pct=huile_pct_input.value
    )


with ui.header():
    ui.label("Dim's Pizza Calculator").classes('text-2xl font-bold')

with ui.card().classes('w-[300px]'):
    nombre_patons = ui.select([1,2,3,4,5,6,7,8,9,10], value=4, label='Nombre de patons', with_input=True, on_change=lambda e: update_labels()).classes('w-full')
    poids_paton = ui.number(value=250, label='Poids par paton (g)', step=5, on_change=lambda e: update_labels()).classes('w-full')
    hydra_pct_input = ui.number(value=65, label="Pourcentage d'hydratation (%)",on_change=lambda e: update_labels()).classes('w-full')
    duree_ferment_input = ui.number(value=24, label='Durée de fermentation (h)',on_change=lambda e: update_labels()).classes('w-full')
    temp_ferment_input = ui.number(value=20, label='Température de fermentation (°C)',on_change=lambda e: update_labels()).classes('w-full')
    type_levure_input = ui.select(['fraiche', 'seche'], value="fraiche", label='Type de levure',on_change=lambda e: update_labels()).classes('w-full')
    qte_sel_par_kg_input = ui.number(value=25, label='Quantité de sel par kg de farine (g)',on_change=lambda e: update_labels()).classes('w-full')
    huile_pct_input = ui.number(value=2.5, step=0.5, label="Pourcentage d'huile (%)",on_change=lambda e: update_labels()).classes('w-full')
with ui.card().classes('w-[300px]'):
    qte_pate_label = ui.label(text="Quantité de pâte : 0.00 g")
    qte_farine_label = ui.label(text="Quantité de farine : 0.00 g")
    qte_eau_label = ui.label(text="Quantité d'eau : 0.00 g")
    qte_levure_label = ui.label(text="Quantité de levure : 0.00 g")
    qte_sel_label = ui.label(text="Quantité de sel : 0.00 g")
    qte_huile_label = ui.label(text="Quantité d'huile : 0.00 g")

    def update_labels():
        pizza = create_pizza()
        qte_pate_label.text = f"Quantité de pâte : {pizza.qte_pate:.0f} g"
        qte_farine_label.text = f"Quantité de farine : {pizza.qte_far:.0f} g"
        qte_eau_label.text = f"Quantité d'eau : {pizza.qte_eau:.0f} g"
        qte_levure_label.text = f"Quantité de levure : {pizza.qte_levure:.2f} g"
        qte_sel_label.text = f"Quantité de sel : {pizza.qte_sel:.0f} g"
        qte_huile_label.text = f"Quantité d'huile : {pizza.qte_huile:.0f} g"

    # Initial update
    update_labels()

ui.run(favicon='🍕', title="Dim's Pizza Calculator",port=8000)