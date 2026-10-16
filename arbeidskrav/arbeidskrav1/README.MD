# Polynomial regresjon

Datasett hentes her: 
https://www.kaggle.com/datasets/sohier/calcofi?select=bottle.csv


Hypotese: Temperaturen synker med dybden i havet.

Modellens R²-score øker med økende polynomgrad.
Lineær regresjon grad 1 gir en R²-score på 0,45.
Modellen stopper å forbedre seg fra og med polynomgrad 8. 
Vi får en R²-score på 0,77 som viser en sterk sammenheng mellom havdyp og temperatur.
Dataene er ikke lineær, men flater ut nedover i dypet.
I virkeligheten er havet mye mer komplekst - datasettet består av 74 kolonner.

Som en første tilnærming så kan vi bekrefte hypotesen om at temperaturen er sterkt
avhengig av dybden. 

