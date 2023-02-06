from OmaMoodul import *
ikood=""
arvud=["100","1001","211","222"]
ikoodid=[]
while True:
    ikood=input("Sisesta isikukood: ")
    if ikood=="0": break
    if pikkus(ikood)==False:
        print("Liiga pikk või lühike isikukood")
        arvud.append(ikood)
    else:
        s=sugu(ikood)
        if s=="viga":
            print("Esimene täht ei ole õige")
        else:
            print(s)
            if sunnipaev(ikood)=="viga":
                print("2-7 tähed on valesti sisestatud")
            else:
                lause(ikood)
                if (kontrollnr(ikood)):
                    print("OK")
                    ikoodid.append(ikood)
                else:
                    print("! ! !")
print()
naised_mehed(ikoodid)
print(ikoodid)
arvud_sorted(arvud)
print(arvud)
