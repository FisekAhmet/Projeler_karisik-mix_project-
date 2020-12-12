motor_hacmi=int(input("Motor Hacmini Giriniz: "))
fiyat=int(input("Vergiler Dahil Aracın Fiyatını Giriniz: "))
if motor_hacmi<=1600 and fiyat<=145435:
    net1 = ((fiyat * 100) / 1711)*10
    otv1 = (net1*45)/100
    kdv1 = (((net1 + otv1) * 18) / 100)
    print(f"Aracın net fiyatı: {net1} Tl'dir.")
    print(f"""Arabanın "ÖTV" miktarı:{otv1} """)
    print(f"""Arabanın "KDV" miktarı:{kdv1} """)
elif motor_hacmi<=1600 and 145435<fiyat<=230100:
    net2=(fiyat*100)/177
    otv2=((net2*50)/100)
    kdv2=(((net2+otv2)*18)/100)
    print(f"Aracın net fiyatı: {net2}")
    print(f"""Arabanın "ÖTV" miktarı:{otv2} """)
    print(f"""Arabanın "KDV" miktarı:{kdv2} """)
elif motor_hacmi<=1600 and 230100<fiyat:
    net3 = (fiyat * 1000) / 2124
    otv3 = ((net3 * 80) / 100)
    kdv3 = (((net3 + otv3) * 18) / 100)
    print(f"Aracın net fiyatı: {net3}")
    print(f"""Arabanın "ÖTV" miktarı:{otv3} """)
    print(f"""Arabanın "KDV" miktarı:{kdv3} """)
elif 1600<motor_hacmi<2000 and fiyat<461380:
    net4 = (fiyat * 1000) / 2714
    otv4 = ((net4 * 130) / 100)
    kdv4 = (((net4 + otv4) * 18) / 100)
    print(f"Aracın net fiyatı: {net4}")
    print(f"""Arabanın "ÖTV" miktarı:{otv4} """)
    print(f"""Arabanın "KDV" miktarı:{kdv4} """)
elif 1600<motor_hacmi<=2000 and 461380<=fiyat:
    net5 = (fiyat * 100) / 295
    otv5 = ((net5 * 150) / 100)
    kdv5 = (((net5 + otv5) * 18) / 100)
    print(f"Aracın net fiyatı: {net5}")
    print(f"""Arabanın "ÖTV" miktarı:{otv5} """)
    print(f"""Arabanın "KDV" miktarı:{kdv5} """)
elif 2000<=motor_hacmi and 461381<=fiyat:
    net6 = (fiyat * 1000) / 3776
    otv6 = ((net6 * 220) / 100)
    kdv6 = (((net6 + otv6) * 18) / 100)
    print(f"Aracın net fiyatı: {net6}")
    print(f"""Arabanın "ÖTV" miktarı:{otv6} """)
    print(f"""Arabanın "KDV" miktarı:{kdv6} """)
print("NOT: Noktadan önceki rakamlar lira sonraki rakamlar kuruş türündendir.")
print("UYARI! Verilen miktarlarda ufak sapmalar olabilir.")