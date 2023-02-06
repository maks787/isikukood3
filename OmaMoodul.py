from re import S


def pikkus(ikood:str)->bool:
    """Funktsioon tagastab True, kui pikkus on 11sümbolid
    :param str ikood: Inimese isikukood
    :rtype: bool
    """
    if len(ikood)==11:
        flag=True
    else:
        flag=False
    return flag

def sugu(ikood:str)->str:
    """kui esimene täht on [1,2,3,4,5,6], siis määrane sugu
    :param str ikood: Isikukood
    :rtype: str
    """
    ikood_list=list(map(int,ikood))
    if ikood_list[0] in [1,3,5]:
        s="mees"
    elif ikood_list[0] in [2,4,6]:
        s="naine"
    else:
        s="viga"
    return s
def sunnipaev(ikood:str):
    ikood_list=list(map(int,ikood))
    y=str(ikood_list[1])+str(ikood_list[2])
    m=str(ikood_list[3])+str(ikood_list[4])
    d=str(ikood_list[5])+str(ikood_list[6])
    if int(m)>0 and int (m)<13 and int(d)>0 and int(d)<32:

        if ikood_list[0] in [1,2]:
            yy="18"
        elif ikood_list[0] in [3,4]:
            yy="19"
        else:
            yy="20"
        spaev=d+"."+m+"."+yy+y
    else:
        spaev="viga"
    return spaev
def sunnikoht(ikood: str)->str:
    ikood_list=list(ikood)
    tahed_8910=ikood_list[7]+ikood_list[8]+ikood_list[9]
    t=int(tahed_8910)
    if 1<t<10:
        haigla="Kuressaare Haigla"
    elif 11<t<19:
        haigla="Tartu ülikooli naistekliinik, Tartumaa, Tartu"
    elif 22<t<220:
        haigla="Ida Virumaa Keskhaigla, Pelgulinna sünnitusmaja, hiiumaa, keila, rapla haigla, loksa haigla"
    elif 221<t<270:
        haigla="ida virumaa keskhaigla (kohtla järve, endine jõhvi)"
    elif 271<t<370:
        haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371<t<420:
        haigla="Narva Haigla"
    elif 421<t<490:
        haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491<t<520:
        haigla="Järvamaa Haigla (Paide)"
    elif 521<t<570:
        haigla="Rakvere, Tapa haigla"
    elif 571<t<600:
        haigla="Valga Haigla "
    elif 601<t<650:
        haigla="Viljandi Haigla"
    elif 651<t<700:
        haigla="Lõuna-Eesti Haigla (Võru), Põlva Haigla "
    else:
        haigla="Välismaal"
    return haigla
def lause(ikood: str)->str:
    print(f"see on {sugu(ikood)} ta on sündinud {sunnipaev(ikood) }, tema sünnikoht on {sunnikoht(ikood)}")

def kontrollnr(ikood:str)->int:
    astme1=[1,2,3,4,5,6,7,8,9,1]
    astme2=[3,4,5,6,7,8,9,1,2,3]
    ik_list=list(ikood)
    ik_list=list(map(int,ik_list))
    summa=0
    for i in range(0,10,1):
         summa+=ik_list[i]*astme1[i]
    s=(summa//11)*11
    jaak=summa-s
    if jaak==int(ik_list[10]):
        return jaak
    else:
        summa=0
        for i in range(0,10,1):
            summa+=ik_list[i]*astme1[i]
        s=(summa//11)*11
        jaak=summa-s
        return jaak
def naised_mehed(ikoodid:list)->list:
    naised=[]
    mehed=[]
    for kood in ikoodid:
        kood=list(kood)
        if int(kood[0])%2==0:
            naised.append(kood)
        else:
            mehed.append(kood)
    naised.extend(mehed)
    naised.extend(mehed)
    return naised

def arvud_sorted(arvud:list)->list:
    arvud=list(map(int,arvud))
    arvud.sort()
    return arvud

def lause(ikood: str) ->list:
    print(f"see on ")