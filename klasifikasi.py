import sys

kamus_S = ['aku', 'saya', 'kamu', 'dia', 'anda']
kamus_P = ['sedang makan', 'lagi tidur']
kamus_O = ['nasi goreng', 'bakso', 'tempe']
kamus_K = ['di kantin', 'di rumah', 'di sauna', 'di masjid']

arrayKalimat = []
kevalidan_kalimat = [False, False, False, False]

counter_sama = 0

def rekursifKata(kamus, k, l):
    global counter_sama
    global arrayKalimat
    
    try:
        if counter_sama is len(kamus[k]):
            try:
                if arrayKalimat[0] is ' ': arrayKalimat.pop(0)
            except IndexError:
                pass
            # print(f'{counter_sama, len(kamus[k])}, {kamus[k]}')
            counter_sama = 0
            return True
    except IndexError:
        return False

    print(f'{kamus[k][l], arrayKalimat}, {kamus[k]}')
    if kamus[k][l] is arrayKalimat[0] :
        counter_sama += 1
        arrayKalimat.pop(0)
        if not arrayKalimat : return True
        return rekursifKata(kamus, k, l+1)
    else:
        if counter_sama is 0:
            return rekursifKata(kamus, k+1, l)
        else : 
            try:
                counter_sama = 0
                return rekursifKata(kamus, k+1, l)
            except IndexError:
                pass
    

def main():
    kalimat = 'saya sedang makan di masjid'

    for x in kalimat:
        arrayKalimat.append(x)

    kevalidan_kalimat[0] = rekursifKata(kamus_S, 0, 0)
    kevalidan_kalimat[1] = rekursifKata(kamus_P, 0, 0)
    kevalidan_kalimat[2] = rekursifKata(kamus_O, 0, 0)
    kevalidan_kalimat[3] = rekursifKata(kamus_K, 0, 0)
    
    if kevalidan_kalimat[0] :
        print(f'S valid')
    if kevalidan_kalimat[1] :
        print(f'P valid')
    if kevalidan_kalimat[2] :
        print(f'O valid')
    if kevalidan_kalimat[3] :
        print(f'K valid')

    print(arrayKalimat)

if __name__ == "__main__":
    main()