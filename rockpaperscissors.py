rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

secimim = input("Seçiminiz nedir taş mı kağıt mı makas mı ?")

list = ["taş" , "kağıt","makas"]

bilgisayar_skoru = random.choice(list)
print(bilgisayar_skoru)


if secimim == "makas" and bilgisayar_skoru =="kağıt":
    print("Kazandık")
elif secimim == "makas" and bilgisayar_skoru == "taş":
    print("Kaybettik")
elif secimim == "makas" and bilgisayar_skoru =="makas":
    print("Beraberlik")


if secimim == "taş" and bilgisayar_skoru =="makas":
    print("Kazandık")
elif secimim == "taş" and bilgisayar_skoru == "taş":
    print("Beraberlik")
elif secimim == "taş" and bilgisayar_skoru =="kağıt":
    print("Kaybettik")


if secimim == "kağıt" and bilgisayar_skoru =="makas":
    print("Kaybettik")
elif secimim == "kağıt" and bilgisayar_skoru == "kağıt":
    print("Beraberlik")
elif secimim == "kağıt" and bilgisayar_skoru =="taş":
    print("Kazandık")

