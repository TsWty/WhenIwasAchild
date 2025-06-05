import random


# def sayi_sayi_tahmin_oyunu():
#     print("Sayı sayi_tahmin oyununa hoş geldiniz!")
#     print("1 ile 100 arasında bir sayı tuttumMmmMmmMmm. sayi_tahmin etmeye başlayabilirsiniz.")

#     sayi_tahmin_edilecek_sayi = random.randint(1, 100)
#     sayi_tahmin_hakki = 8

#     for _ in range(sayi_tahmin_hakki):
#         print("Kalan sayi_tahmin hakkınız:", sayi_tahmin_hakki)
#         sayi_tahmin = int(input("sayi_tahmininizi girin: "))

#         if sayi_tahmin == sayi_tahmin_edilecek_sayi:
#             print("Tebrikler! Doğru sayi_tahmin ettiniz.")
#             return

#         if sayi_tahmin < sayi_tahmin_edilecek_sayi:
#             print("Daha yüksek bir sayı dene gardaş.")
#         else:
#             print("Daha düşük bir sayı dene gardaş.")

#         sayi_tahmin_hakki -= 1

#     print("sayi_tahmin hakkın kalmadı BB . Tutulan sayı:", sayi_tahmin_edilecek_sayi)

# sayi_sayi_tahmin_oyunu()

def sayi_sayi_tahmin(en_dusuk_sayi, en_yuksek_sayi, deneme_hakki=1):
    sayi_tahmin = random.randint(en_dusuk_sayi, en_yuksek_sayi)
    print("Sistem tahmini:", sayi_tahmin)

    cevap = input("Tahmin doğru mu? (E/H): ")

    if cevap.upper() == "E":
        print("Sistem bildi هياااااااال")
        return
    elif cevap.upper() == "H":
        if deneme_hakki == 1:
            s1 = input("Daha yukarı (Y) veya daha aşağı (A) bir sayı belirtin: ")
        else:
            s1 = input("Daha yukarı (Y) veya daha aşağı (A) bir sayı belirtin (Son sayi_tahmin ettiğin sayı {}): ".format(sayi_tahmin))

        if s1.upper() == "Y":
            en_dusuk_sayi = sayi_tahmin +1
        elif s1.upper() == "A":
            en_yuksek_sayi = sayi_tahmin - 1
        else:
            print("Sanırım farklı bir tuşa bastın 'Y' veya 'A' harflerinden birini seç.")

        sayi_sayi_tahmin(en_dusuk_sayi, en_yuksek_sayi, deneme_hakki+1)
    else:
        print("Sanırım farklı bir tuşa bastın 'E' veya 'H' seç.")
        sayi_sayi_tahmin(en_dusuk_sayi, en_yuksek_sayi)

print("Sistem sayı tahmin oyununa hoş geldiniz!")
print("1 ile 100 arasında bir sayı tutun ve sistem bulsun :)")

sayi_sayi_tahmin(1, 100)
