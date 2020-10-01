#   Vragenlijst Studenten Queries - Matthias Vermeulen
#   -----------------------------
import pandas as pd
import matplotlib.pyplot as plt

naValues = ['Onbekend']

vragenLijst = pd.read_csv('VragenlijstStudenten.csv', sep='\t', na_values=naValues)
metNa = vragenLijst
vragenLijst.dropna()

#   1. Hoeveel onbekende Resus waarden zijn er ?
print('\n1. Aantal onbekende Resus waarden = ', metNa['Resus'].isna().sum())

#   2. Hoeveel studenten wonen er in Antwerpen ?
studentenAntwerpen = vragenLijst['AdresAntwerpen']
print('\n2. Aantal studenten die wonen in Antwerpen = ', studentenAntwerpen[studentenAntwerpen == 'Ja'].count())

#   3. Hoeveel studenten wonen er in Antwerpen, op minder dan een half uur rijden van de campus ?
studentenLokaal = vragenLijst[(vragenLijst['AdresAntwerpen'] == 'Ja') & (vragenLijst['AfstandKdgMinuten'] < 30)]
print('\n3. Aantal studenten die wonen in Antwerpen, op minder dan een half uur rijden van de campus = ',
      studentenLokaal['AdresAntwerpen'].count())

#   4. Bij hoeveel studenten staat Kiwi op de eerste plaats bij FruitVoorkeur ?
studentenKiwi = vragenLijst[vragenLijst['FruitVoorkeur'].str.contains("1=Kiwi")]
print('\n4. Aantal studenten met Kiwi op eerste plaats = ', studentenKiwi['FruitVoorkeur'].count())

#   5. Geef een verdeling van de Besturingssystemen. Voor elke mogelijkheid het percentage.
#   Plot deze verdeling in een piechart.
# verdeling van besturingssystemen
print('\n5. Verdeling van Besturingssystemen:\n')
print(vragenLijst['BesturingsSysteem'].value_counts(normalize=True))
# opsplitsen van index en waarden in verschillende lists
besturingsSysteem = vragenLijst['BesturingsSysteem'].value_counts(normalize=True).index.tolist()
besturingsPercentage = vragenLijst['BesturingsSysteem'].value_counts(normalize=True).tolist()

# initiatie van pieplot
fig1, ax1 = plt.subplots()
ax1.pie(besturingsPercentage, labels=besturingsSysteem, autopct='%1.2f%%', shadow=True, startangle=90, normalize=True)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#   6. Hoeveel linkshandige vrouwen zijn er ?
vrouwenLinks = vragenLijst[(vragenLijst['Geslacht'] == 'Vrouw') & (vragenLijst['Schrijfhand'] == 'Links')]
print('\n6. Aantal linkshandige vrouwen = ', vrouwenLinks['Geslacht'].count())

#   7. Hoeveel studenten wonen niet in Antwerpen, hebben geen rijbewijs en roken niet (alle 3 tesamen) ?
studenten = vragenLijst[(vragenLijst['AdresAntwerpen'] == 'Nee')
                        & (vragenLijst['Rijbewijs'] == 'Nee')
                        & (vragenLijst['Tabak'] == 'Nee')]
print('\n7. Aantal studenten die niet in Antwerpen wonen, geen rijbewijs hebben en niet roken = ',
      studenten['AdresAntwerpen'].count())

#   8. Verander in InternetAankoop alle 'Ja' door 'Yes' en alle 'Nee' door 'No'.
vragenLijst['InternetAankoop'] = vragenLijst['InternetAankoop'].replace('Ja', 'Yes')
vragenLijst['InternetAankoop'] = vragenLijst['InternetAankoop'].replace('Nee', 'No')

#   9. Zet alle entries bij BelangInformaticus in lower case.
vragenLijst['BelangInformaticus'] = vragenLijst['BelangInformaticus'].str.lower()

#   10. Verander alle schoenmaten die kleiner zijn dan 40 in 0.
vragenLijst.loc[(vragenLijst.Schoenmaat < 40), 'Schoenmaat'] = 0
