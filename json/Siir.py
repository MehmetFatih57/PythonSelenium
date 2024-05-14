from bs4 import BeautifulSoup
import requests

def rastele_siir():
    r = requests.get("https://antoloji.com/siir/rastgele/")
    soup = BeautifulSoup(r.content, "html.parser")
    siir_baslik = soup.find("div", attrs={"class": "pd-title-a"})
    siir_icerik = soup.find("div", attrs={"class": "pd-text"})
    basliklar = siir_baslik.find_all("h3")
    siir_link = siir_baslik.find("a")
    p_etiketler = siir_icerik.find_all("p")
    a_etiketler = siir_icerik.find_all("a")
    for h3_etiket in basliklar:
        baslik1 = h3_etiket.get_text()
        print(baslik1)
    for petiket in p_etiketler:
        siir = petiket.get_text()
        print(siir)
    for yazarlar in a_etiketler:
        yazar = yazarlar.get_text()
        print(f"Sair: {yazar}")

    href_degeri = siir_link.get("href")
    link = "https://antoloji.com/" + href_degeri
    print(f"href degeri : {link}")

rastele_siir()
