import numpy as np

#hjelpefunksjon for å hente koordinater til punkter
def Punkt(antallPunkter):
    '''
    Dette er en hjelpefunksjon for å la bruker skrive inn koordinater til x-antall punkter
    Jeg lager en funksjon, fordi jeg ser at jeg vil trenge det i flere oppgaver.
    Den tar inn en parameter som sier hvor mange punkter jeg trenger, og den returnerer 
    en liste med tupler f.eks.
    A, B = getPunktKoordinater(2)
    Du kan aksessere x- og y-koordinat til punktene slik:
    x-koor = A[0]
    y-koor = A[1]
    '''
    punkter = []
    for i in range(antallPunkter):
        x = int(input(f"x-koordinat for {i+1}. punkt = "))
        y = int(input(f"y-koordinat for {i+1}. punkt = "))
        punkter.append((x,y))
    return punkter

def VektorMellomToPunkt(A, B):
    '''
    Finner koordinater til vektor mellom punkt A(x1,y1) og B(x2, y2) ved regne [x2-x1, y2-y1]
    Tar inn to tupler med koordinater til de to punkter
    '''
    return np.array([B[0]-A[0], B[1]-A[1]])    

def Posisjonsvektor(punkt):
    origo = (0,0)
    return VektorMellomToPunkt(origo, punkt)


def Oppgave1():

    A,B = Punkt(2)   #Hente koordinater til 2 punkter
    #Bestemt AB = [x2-x1, y2-y1]
    AB = VektorMellomToPunkt(A,B)
    print(f"Vektor AB = {AB}")

    #Bestemt AB = OB - OA
    OA = Posisjonsvektor(A)
    OB = Posisjonsvektor(B)
    AB = OB - OA
    print(f"Vektor AB = {AB}")    

    #En vektor som har samme retning som AB og er 3 ganger så lang
    ABx3 = 3*AB
    print(f"Vektor {ABx3} er 3 ganger så lang som {AB}")

    #En vektor som har motsatt regning som AB og er 5 ganger så lang
    ABx5 = -5*AB
    print(f"Vektor {ABx5} er 5 ganger så lang som {AB}, og har motsatt retning")

    halvAB = AB/2
    print(f"Vektor {halvAB} er halvparten så lang som {AB}")

    AB_25percent = AB*1.25
    print(f"Vektor {AB_25percent} er 25% lengre som {AB}")


def Oppgave2():
    S, P = Punkt(2)
    radius = int(input("Skriv lengde til radius: "))

    #Bruker avstand i annet for å unngå avrundningsfeil i python med kvadratrot
    avstandSP = (P[0]-S[0])**2 + (P[1]-S[1])**2
    print(avstandSP)

    if avstandSP == radius**2:
        print(f"Punkt P{P} ligger på sirkel (x-{S[0]})^2 + (y-{S[1]})^2 = {radius**2}")
    elif avstandSP > radius**2:
        print(f"Punkt P{P} ligger utenfor sirkel (x-{S[0]})^2 + (y-{S[1]})^2= {radius**2}")
    else: 
        print(f"Punkt P{P} ligger innefor sirkel (x-{S[0]})^2 + (y-{S[1]})^2= {radius**2}")



if __name__ == "__main__":
    #A, B = getPunktKoordinater(2)
    #print(A, B)

    #Oppgave1()
    Oppgave2()
