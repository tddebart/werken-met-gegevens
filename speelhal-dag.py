toegangsTicketPrijs = 7.45
aantalPersonen = 3
lengteVR = 45
vrPrijs = 0.37

volledigePrijs = aantalPersonen*toegangsTicketPrijs+(lengteVR/5)*vrPrijs*aantalPersonen

print("Dit geweldige dagje-uit met {} mensen in de Speelhal met {} minuten VR kost je maar {} euro".format(aantalPersonen, lengteVR, volledigePrijs))
print(volledigePrijs)