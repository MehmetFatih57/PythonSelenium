import json

person_string = '{"Isim " : "Ali" , "SoyIsim " : "Veli" , "Yas " : "15"}'

# JSON dosyasını oku
with open("person.json")  as file:
        data = json.load(file)

        print(data)

        # Verileri ekrana yazdır
        print("Isim:", data["isim"])
        print("SoyIsim:", data["soyIsim"])
        print("Yas:", data["yas"])
