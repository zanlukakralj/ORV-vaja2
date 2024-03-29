import cv2 as cv
import numpy as np

def konvolucija(slika, jedro):
    '''Izvede konvolucijo nad sliko z dodajanjem robov glede na velikost jedra.'''
    visina, sirina, kanali = slika.shape
    jedro_sirina, jedro_visina = jedro.shape

    # Določimo število pikslov za polnjenje na vsaki strani slike
    padding_vodoravno = (jedro_sirina - 1) // 2
    padding_navpicno = (jedro_visina - 1) // 2

    # Dodamo robove (padding) k sliki
    slika_pad = np.pad(slika, ((padding_navpicno, padding_navpicno), (padding_vodoravno, padding_vodoravno), (0, 0)), mode='edge')

    # Ustvarimo novo sliko za rezultate konvolucije
    rez_konvolucije = np.zeros((visina, sirina, kanali))

    # Sprehodimo se skozi sliko s celotnim jedrom
    for x in range(visina):
        for y in range(sirina):
            for c in range(kanali):
                # Izrežemo ustrezno regijo iz padane slike
                regija = slika_pad[x:x + jedro_visina, y:y + jedro_sirina, c]
                # Izvedemo konvolucijo za vsak kanal posebej
                rez_konvolucije[x, y, c] = np.sum(regija * jedro)

    return rez_konvolucije

def filtriraj_z_gaussovim_jedrom(slika, sigma):
    '''Filtrira sliko z Gaussovim jedrom.'''
    velikost_jedra = (2 * sigma) * 2 + 1

    # Ustvarimo jedro z Gaussovim filtro
    jedro = np.zeros((velikost_jedra, velikost_jedra))
    k = (velikost_jedra / 2) - 1/2

    for i in range(velikost_jedra):
        for j in range(velikost_jedra):
            jedro[i, j] = (1 / (2 * np.pi * sigma**2)) * np.exp(-((i - k - 1)**2 + (j - k - 1)**2) / (2 * sigma**2))

    return konvolucija(slika, jedro).astype(np.uint8)

def filtriraj_sobel_horizontalno(slika):
    '''Filtrira sliko z Sobelovim jedrom horizontalno in označi slikovne elemente z močnejšim gradientom.'''
    pass

if __name__ == '__main__':
    pass
