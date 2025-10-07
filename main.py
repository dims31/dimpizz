from nicegui import ui
from nicegui.events import ValueChangeEventArguments


class Pate:
    def __init__(self, qte_pate, hydra_pct, duree_ferment, temp_ferment, type_levure, qte_sel_par_kg, huile_pct):
        self.qte_pate = qte_pate
        self.hydra_pct = hydra_pct
        self.duree_ferment = duree_ferment
        self.temp_ferment = temp_ferment
        self.type_levure = type_levure
        self.qte_sel_par_kg = qte_sel_par_kg
        self.huile_pct = huile_pct
        self.calc_quantite()


    def calc_quantite(self):
        coef_total = 1 + (self.hydra_pct / 100) + (self.qte_sel_par_kg + self.levure_par_kg()) / 1000
        self.qte_far = self.qte_pate / coef_total
        self.qte_eau = (self.hydra_pct - self.huile_pct) * self.qte_far / 100
        self.qte_levure = self.levure_par_kg() * self.qte_far / 1000
        self.qte_sel = self.qte_sel_par_kg * self.qte_far / 1000
        self.qte_huile = self.huile_pct * self.qte_far / 100

    def levure_par_kg(self):
        if self.type_levure == "fraiche":
            ratio_levure = 1
        elif self.type_levure == "seche":
            ratio_levure = 0.33
        else:
            raise ValueError("type de levure inconnu")

        CONST_LEVURE = 300
        return ratio_levure * CONST_LEVURE / (self.temp_ferment * self.duree_ferment)


pizza = Pate(
    qte_pate=100,
    hydra_pct=65,
    duree_ferment=24,
    temp_ferment=20,
    type_levure="fraiche",
    qte_sel_par_kg=25,
    huile_pct=2.5
)


qte_pate = ui.number(value=pizza.qte_pate, label='Quantité de pâte (g)')
hydra_pct = ui.number(value=pizza.hydra_pct, label='Pourcentage d\'hydratation (%)')
duree_ferment = ui.number(value=pizza.duree_ferment, label='Durée de fermentation (h)')
temp_ferment = ui.number(value=pizza.temp_ferment, label='Température de fermentation (°C)')
type_levure = ui.select(['fraiche', 'seche'], value=pizza.type_levure, label='Type de levure')
qte_sel_par_kg = ui.number(value=pizza.qte_sel_par_kg, label='Quantité de sel par kg de farine (g)')
huile_pct = ui.number(value=pizza.huile_pct, step=0.5, label='Pourcentage d\'huile (%)')

qte_farine = ui.label(text=f"Quantité de farine : {pizza.qte_far:.2f} g")
qte_eau = ui.label(text=f"Quantité d'eau : {pizza.qte_eau:.2f} g")
qte_levure = ui.label(text=f"Quantité de levure : {pizza.qte_levure:.2f} g")
qte_sel = ui.label(text=f"Quantité de sel : {pizza.qte_sel:.2f} g")
qte_huile = ui.label(text=f"Quantité d'huile : {pizza.qte_huile:.2f} g")

def update_values(e=None):
    pizza.qte_pate = qte_pate.value
    pizza.hydra_pct = hydra_pct.value
    pizza.duree_ferment = duree_ferment.value
    pizza.temp_ferment = temp_ferment.value
    pizza.type_levure = type_levure.value
    pizza.qte_sel_par_kg = qte_sel_par_kg.value
    pizza.huile_pct = huile_pct.value
    pizza.calc_quantite()

    qte_farine.text = f"Quantité de farine : {pizza.qte_far:.2f} g"
    qte_eau.text = f"Quantité d'eau : {pizza.qte_eau:.2f} g"
    qte_levure.text = f"Quantité de levure : {pizza.qte_levure:.2f} g"
    qte_sel.text = f"Quantité de sel : {pizza.qte_sel:.2f} g"
    qte_huile.text = f"Quantité d'huile : {pizza.qte_huile:.2f} g"

    # Recalculer à chaque changement de valeur
qte_pate.on('change', update_values)
hydra_pct.on('change', update_values)
duree_ferment.on('change', update_values)
temp_ferment.on('change', update_values)
type_levure.on('change', update_values)
qte_sel_par_kg.on('change', update_values)
huile_pct.on('change', update_values)


ui.run()