
qte_pate = 1650
pourcentage_hydratation = 65
duree_ferment = 24
temp_ferment = 6
type_levure = "fraiche"
qte_sel_par_kg = 25
pourcentage_huile = 2.5


def calc_levure_par_kg(type_levure, temp_fermentation, duree_fermentation):
    if type_levure == "fraiche":
        ratio_levure = 1
    elif type_levure == "seche":
        ratio_levure = 0.33
    else:
        raise ValueError("type de levure inconnu")

    CONST_LEVURE = 300
    return ratio_levure * CONST_LEVURE / (temp_fermentation * duree_fermentation)


def calc_quantite(qte_pate, pourcentage_hydratation, pourcentage_huile, qte_levure_par_kg, qte_sel_par_kg):
    qte_eau = qte_pate * (pourcentage_hydratation - pourcentage_huile) / (100 + (pourcentage_hydratation - pourcentage_huile))
    qte_far = qte_pate - qte_eau
    qte_levure = qte_levure_par_kg * qte_far / 1000
    qte_sel = qte_sel_par_kg * qte_far / 1000
    qte_huile = pourcentage_huile * qte_far / 100
    return {"farine": qte_far, "eau": qte_eau, "levure": qte_levure, "sel": qte_sel, "huile": qte_huile}

levure_kg = calc_levure_par_kg(type_levure, temp_ferment, duree_ferment)

print(f"Pour {qte_pate}g de pâte à {pourcentage_hydratation}% d'pourcentage_hydratation, fermentée {duree_ferment}h à {temp_ferment}°C avec de la levure {type_levure}:")
quantites = calc_quantite(qte_pate, pourcentage_hydratation,pourcentage_huile, levure_kg, qte_sel_par_kg)

print(f"- Farine: {quantites['farine']:.0f}g")
print(f"- Eau: {quantites['eau']:.0f}g")
print(f"- Levure: {quantites['levure']:.1f}g")
print(f"- Sel: {quantites['sel']:.0f}g")
print(f"- Huile: {quantites['huile']:.0f}g")