from io import StringIO
recnik = {}
def kompresiraj(nekompresirano):
    vlez = nekompresirano

    karakteri = []
    for i in vlez:
        if i not in karakteri:
            karakteri.append(i)
            print("Vnesete index za '"+i+"'")
            indeks = input()
            recnik[i] = int(indeks)


    sorted_recnik = sorted(recnik.items(), key=lambda kv: (kv[1], kv[0]))
    recnik.clear()
    for i, j in sorted_recnik:
        recnik[i] = j

    golemina_recnik = recnik.__len__()

    flag = 0
    for i in recnik.values():
        if i == 0:
            flag = 1

    w = ""
    kompresirano = []
    for c in nekompresirano:
        wc = w + c
        if wc in recnik:
            w = wc
        else:
            if  flag == 0:
                golemina_recnik += 1
                flag = 1
            kompresirano.append(recnik[w])
            recnik[wc] = golemina_recnik
            golemina_recnik += 1
            w = c

    if w:
        kompresirano.append((recnik[w]))

    temp = dict((y, x) for x, y in recnik.items())
    recnik.clear()
    for i, j in temp.items():
        recnik[i] = j
    print()
    print(recnik)
    print()
    return kompresirano


def dekompresiraj(kompresirano):
    dekompresirano = StringIO()

    for i in kompresirano:
        if i in recnik:
            dekompresirano.write(recnik[i])

    return dekompresirano.getvalue()

#   Primeri:
#       /THIS/IS/HIS/IS/
#       / - 1
#       T - 5
#       H - 2
#       I - 3
#       S - 4

#       xxyyxyxyxxyyyxyxxyxxyyx
#       x - 0
#       y - 1

print("Vnesete string za kompresiranje: ")
kompresirano = kompresiraj(input())
print("Kompresirano:", kompresirano)
dekompresirano = dekompresiraj(kompresirano)
print("Dekompresirano:", dekompresirano)