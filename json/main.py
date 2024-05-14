import json


class json:
    
    def test_json(self):


        n = {"id": 1,
         "name": "nk",
         "sehir": "Adana"
         }

    with open('info.json', 'r+', encoding="utf8") as dosya:
        veri = json.load(dosya)
        #veri["info"].append(n)
        #dosya.seek(0)
        #json.dump(veri, dosya, indent=4)
        #print("Kaydettim Gec Kardesim Bekleme Yapma")

    aranan_id = 1
    yeni_name = "Ali Can gfjgdsfsdjf"

    for ticket in veri.get("info", []):
        if ticket.get("id") == aranan_id:
            print("Buldum seni oglum , Sen simdi naneyi yimedin mi ?")
            ticket["name"] = yeni_name
            with open('info.json', 'w', encoding="utf8") as dosya:
                json.dump(veri, dosya, ensure_ascii=False, indent=2)
            print(f"Datadaki {aranan_id} id'sine sahip verinin (name) degiskeni {yeni_name} olarak guncellendi")
            break
        else:
            "Gec Lan"


    """
JSON dosyalarından veri çekmek için Python'da json kütüphanesini kullanabilirsiniz. Bu kütüphane, JSON verilerini 
Python nesnelerine dönüştürmeyi ve işlemenizi kolaylaştırır.

Adımlar:

Gerekli Kütüphaneyi İçe Aktarın:
Python
import json
Use code with caution.
content_copy
JSON Dosyasını Açın:
Python
with open("data.json", "r") as dosya:
    # Dosyadaki JSON verisini yükleyin
    veriler = json.load(dosya)

Bu kod, data.json adlı bir dosyayı "okuma" modu ("r") ile açar ve dosya nesnesini dosya değişkenine atar. 
Dosya açıldıktan sonra otomatik olarak kapanacaktır. Ardından, json.load() fonksiyonu dosyadaki JSON verisini okur ve 
Python'da kullanılabilecek bir nesneye dönüştürerek veriler değişkenine atar.

Verilere Erişin:
JSON nesnesi, anahtar-değer çiftleri içeren bir sözlüktür. Anahtarlara erişmek için köşeli parantez kullanabilirsiniz. 
Örneğin:

Python
ad = veriler["kisi"]["ad"]
soyad = veriler["kisi"]["soyad"]
yas = veriler["kisi"]["yas"]

print(f"Ad: {ad}")
print(f"Soyad: {soyad}")
print(f"Yaş: {yas}")

Bu kod, veriler nesnesindeki "kisi" anahtarının altındaki "ad", "soyad" ve "yas" anahtarlarına erişerek kişinin 
adını, soyadını ve yaşını ad, soyad ve yas değişkenlerine atar. Ardından, bu değişkenlerin değerlerini konsola yazdırır.

Dizi Verilere Erişin:
JSON nesnesi, diziler de içerebilir. Dizilere erişmek için köşeli parantez ve dizin kullanabilirsiniz. Örneğin:

Python
sehirler = veriler["sehirler"]
print(f"İlk şehir: {sehirler[0]}")
print(f"Son şehir: {sehirler[-1]}")

Bu kod, veriler nesnesindeki "sehirler" anahtarına erişerek bir şehirler dizisini sehirler değişkenine atar. 
Ardından, dizinin ilk ve son öğelerini konsola yazdırır.

Önemli Notlar:

Bu kod sadece bir örnektir. Kendi JSON dosyanızın ve verilerinizin yapısına göre uyarlamanız gerekir.
Dosya yolu ve JSON anahtar adları, kendi dosyanıza göre değişiklik gösterebilir.
Daha karmaşık JSON yapıları için, veriler nesnesine erişmek için dizinler ve anahtarlar kullanabilirsiniz.
"""













































