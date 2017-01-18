##Ovo je program za računanje najkraćih puteva u grafu pomoću Dijkstrinog algoritma
##Služi kao pomoć kod izračuna rješenja prvog zadatka iz projekta (Tim Dijkstra, DSTG 2016/2017)
##
##Kod je napisan uz pomoć danih primjera source koda na stranici:
##http://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python

def Dijkstra(pocetni_vrh):
    vrhovi = ('v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8')
    udaljenosti = {
        'v1': {'v2': 2, 'v6': 4, 'v8': 5},
        'v2': {'v1': 2, 'v3': 12, 'v7': 7},
        'v3': {'v2': 12, 'v4': 3},
        'v4': {'v3': 3, 'v5': 7, 'v7': 5},
        'v5': {'v6': 4, 'v8': 3, 'v7': 1, 'v4': 7},
        'v6': {'v1': 4, 'v8': 1, 'v5': 4},
        'v7': {'v2': 7, 'v8': 4, 'v5': 1, 'v4': 5},
        'v8': {'v1': 5, 'v6': 1, 'v5': 3, 'v7': 4}}

    neposjeceni = {vrh: None for vrh in vrhovi}
    posjeceni = {}
    trenutni = pocetni_vrh
    udaljenostTrenutnog = 0
    neposjeceni[trenutni] = udaljenostTrenutnog
    korak = 0
    ukupnaUdaljenost = 0

    while True:
        for susjedni, udaljenost in udaljenosti[trenutni].items():
            if susjedni not in neposjeceni: continue
            novaUdaljenost = udaljenostTrenutnog + udaljenost
            if neposjeceni[susjedni] is None or neposjeceni[susjedni] > novaUdaljenost:
                neposjeceni[susjedni] = novaUdaljenost
        posjeceni[trenutni] = udaljenostTrenutnog

        #ispis nadjenog najkraceg puta u trenutnom koraku
        print('korak [',korak,']: ', pocetni_vrh, ' - ', trenutni, ': ' , udaljenostTrenutnog)
        korak = korak + 1;
        ukupnaUdaljenost = ukupnaUdaljenost + udaljenostTrenutnog
        
        del neposjeceni[trenutni]
        if not neposjeceni: print("Ukupna izmjerena udaljenost: ", ukupnaUdaljenost)
        if not neposjeceni: break
        kandidati = [vrh for vrh in neposjeceni.items() if vrh[1]]
        trenutni, udaljenostTrenutnog = sorted(kandidati, key = lambda x: x[1])[0]

print("Dobrodošli u program za računanje najkraćih puteva Dijkstrinim algoritmom!")
print("Tim: Dijkstra, DSTG 2016/2017")
print("*Nazivi vrhova i težine bridova za prvi zadatak već su unešeni u program*")
print("-----------------------------")
jos = 'da'
while(jos == 'da'):
    odgovor = input('Unesite početni vrh (v1, v2, ..., v8): ')
    print('------------------')
    print('Rješenje: ')
    print('------------------')
    print('Najkraći putevi (početak - kraj): ')
    Dijkstra(odgovor);
    print()
    jos = input('Želite li ponovo računati? (da/ne): ')

