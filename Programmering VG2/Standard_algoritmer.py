"""
Halveringsmetoden er en numerisk metode for å finne 
nullpunkter til en funksjon f i en gitt intervall [a,b]

Gitt en funksjon f og en toleranse f.eks. lik 0.0001
kan Halveringsalgoritmen på norsk beskrives med følgende
algoritme:

 1) Velg to startpunkter a og b slik at f (a)·f(b ) < 0. 
 2) Beregn midtpunktet  m = (a+b)/2 

 3) Gjenta trinn 4 og 5 så lenge abs(f(m)) > toleranse
    4) Sjekk f(m): 
        • Hvis f(m)·f (b) < 0, sett a = m 
        • Ellers, sett b = m  
    5) Beregn midtpunktet  m = (a+b)/2 

Da er m et tilnærmet verdi for nullpunktet
"""

def halveringsmetode(f, a:int, b:int, toleranse=1E-08)-> float:
    """Numerisk metode for å finne nullpunkter til en 
    funksjon f i en gitt intervall [a,b]"""

    m = (a + b)/2

    while abs(f(m)) > toleranse:
        if f(m)*f(b) < 0:   #Nullpunkt i [m,b]
            a = m
        else:               #Nullpunkt i [a,m]
            b = m
        m = (a+b)/2
    
    return m

if __name__ == "__main__":
    def test_halveringsmetode():
        def f(x) : return 10**x - 100

        nullpunkt = halveringsmetode(f, 0, 3)
        assert nullpunkt - 2 < 1E-8

    test_halveringsmetode()
    
    
