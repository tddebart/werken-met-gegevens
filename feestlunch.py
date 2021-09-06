croissantHoeveelheid = 17
croissantPrijs = 0.39
stockbroodHoeveelheid = 2
stockbroodPrijs = 2.78
bonnenHoeveelheid = 3
bonnenKorting = 0.50

volledigePrijs = (croissantHoeveelheid*croissantPrijs+stockbroodHoeveelheid*stockbroodPrijs-bonnenHoeveelheid*bonnenKorting)

print("De feestlunch kost je bij de bakker " + str(volledigePrijs) + " euro voor de " + str(croissantHoeveelheid) + " croissantjes en de " + str(stockbroodHoeveelheid) + " stokbroden als de " + str(bonnenHoeveelheid) + " kortingsbonnen nog geldig zijn!")
print(volledigePrijs)

