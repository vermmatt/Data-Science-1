import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import math


def main():
    print('Synthese Oefening Samenhang')

    # Open de file 'eegdata.csv' en maak een dataframe van kolom AF3 tot en met AF4.
    eegdata = pd.read_csv('eegdata.csv', sep=';', decimal=",")
    df = eegdata.iloc[:, 3:17]

    # geneste for-loop om elke combinatie van kolom met een andere kolom in het dataframe te doorlopen
    for i in range(len(df.columns)):
        print('\nColumn', df.columns[i])
        # twee lists om de berekende explained variance in op te slaan, en de kolomnamen die zijn doorlopen
        varlist = []
        collist = []
        for j in range(len(df.columns)):
            # De correlatie en regressie voor dezelfde contact punten mag je niet berekenen, die is altijd maximaal.
            if i != j:
                # selectie van de onafhankelijke reeks en de afhankelijke
                s1 = df.iloc[:, i]
                s2 = df.iloc[:, j]
                # berekening van correlatie, bepaling model, voorspelde waarde, mean error en explained variance
                corr = s1.corr(s2)
                model = np.polyfit(s1, s2, 1)
                predict = np.poly1d(model)
                error = math.sqrt(((predict(s1) - s2) ** 2).mean())
                exvar = corr ** 2
                # voeg berekende explained variance toe aan lijst en voeg de kolomnaam toe aan kolomlijst
                varlist.append(exvar)
                collist.append(df.columns[j])
                # informatie loggen naar de console met bijhorende tekst formatering
                print("{} {:^5} {:^} {:^9} {:^} {:^9} {:^} {:^9}".format('   Column', df.columns[j], 'pearson =',
                                                        round(corr, 1), 'regression meanError =', round(error, 1),
                                                        'explained varriance =', round(exvar, 1)))
        # na doorlopen van een set van combinaties wordt de minimale en maximale explained variance bepaald
        minvar = min(varlist)
        # na de bepaling van min of max wordt de index van dit element in de lijst toegekend aan een index variable
        minindex = varlist.index(minvar)
        maxvar = max(varlist)
        maxindex = varlist.index(maxvar)
        # loggen naar console
        print('\n   CurrentColumn =', df.columns[i])
        # op basis van index variabele kunnen we de kolomnnaam uit de kolomlijst halen
        print('   Column with max explainedVariance =', collist[maxindex])
        print('   Column with min explainedVariance =', collist[minindex])

    # Plot max variantie
        x = df.loc[:, df.columns[i]]
        y = df.loc[:, collist[maxindex]]

        model = np.polyfit(x, y, 1)
        predict = np.poly1d(model)
        error = math.sqrt(((predict(x) - y) ** 2).mean())

        plot.figure()
        plot.scatter(x, y)
        xx = np.arange(x.min(), x.max(), (x.max() - x.min()) / 100)
        yy = predict(xx)
        plot.title('Contact points with MAX explained variance')
        plot.fill_between(xx, yy - error, yy + error, color="#FFFF0080")
        plot.plot(xx, yy, color="red")
        plot.xlabel(df.columns[i])
        plot.ylabel(collist[maxindex])
        # exporteren van plots, formatering van filename
        plot.gcf().savefig('max ' + df.columns[i] + ' versus ' + collist[maxindex] + ".png")
        plot.show()

    # Plot min variantie
        x = df.loc[:, df.columns[i]]
        y = df.loc[:, collist[minindex]]

        model = np.polyfit(x, y, 1)
        predict = np.poly1d(model)
        error = math.sqrt(((predict(x) - y) ** 2).mean())

        plot.figure()
        plot.scatter(x, y)
        xx = np.arange(x.min(), x.max(), (x.max() - x.min()) / 100)
        yy = predict(xx)
        plot.title('Contact points with MIN explained variance')
        plot.fill_between(xx, yy - error, yy + error, color="#FFFF0080")
        plot.plot(xx, yy, color="red")
        plot.xlabel(df.columns[i])
        plot.ylabel(collist[minindex])
        # exporteren van plots, formatering van filename
        plot.gcf().savefig('min ' + df.columns[i] + ' versus ' + collist[minindex] + ".png")
        plot.show()

if __name__ == "__main__":
    main()
