# Naam:     Elco van Rijswijk
# Datum:    24-10-2017 / 13-11-2017
# Versie:   



def main():
    bes1    = "GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna"     # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    bes2    = "GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna"
    bes3    = "GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna"

    
    fout    = "error.txt"
    error   = ""
    bes     = ""
    
    zoekwoord = input("typ start om te beginnen: ")
    if zoekwoord == "start":
        print("kies uit volgende bestanden: bes1, bes2, bes3,....")
        k = input("geef je bestand: ")
        
        if k == "bes1":
            bes = bes1
        elif k =="bes2":
            bes = bes2
        elif k =="bes3":
            bes = bes3
        elif k == "fout":
            bes = fout
        else:
            bes = error
            
        headers_li, seqs_li = lees_inhoud(bes)       
        
        print("maak een keuze, dna, knip of beide")       #de keuze laten maken
        a = input("=")
                
        if a == "dna":
            print("dna gekozen")
            print("hoeveel wil je er zien (pas op boven 500 duurt het erg lang)")
            aantal=int(input(":"))
            print(40*"-")
            is_dna(seqs_li, headers_li, aantal)
                    
        elif a == "knip":
            print("knip sequentie gekozen")
            print("hoeveel wil je er zien (pas op boven 500 duurt het erg lang)")
            aantal=int(input(":"))
            print(40*"-")
            knipt(seqs_li, headers_li, aantal)
                    
        elif a == "beide":
            print("beide gekozen")
            print("hoeveel wil je er zien (pas op boven 500 duurt het erg lang)")
            aantal=int(input(":"))
            print(40*"-")
            is_dna(seqs_li, headers_li, aantal)                             #vragen hoeveel je wil laten printen
            knipt(seqs_li, headers_li, aantal)
                    
        else:
            print("foutmelding")
    else:
        print("foutmelding")
        
       
  
def lees_inhoud(bes):
    try:
        bes = open(bes)                         #het bestand proberen te openen anders error
    except FileNotFoundError:
        print("file niet gevonden")
        quit()
        
    
    seqs_li     =    []
    headers_li  =    []

    for line in bes:
        if line[0] == ">":
            headers_li.append(line)         # splitten op > en in lijsten zetten

        else:
            seqs_li.append(line)
    
    
    return headers_li, seqs_li
    
def is_dna(seqs_li, headers_li, aantal):

    li_a=[]                        
    li_t=[]                     
    li_c=[]
    li_g=[]
    li_u=[]
    totaal=[]
    try:
        for line in seqs_li:
            
            a=line.count("A")        #het tellen van het aantal ATCG en totaal
            li_a.append(a)

            t=line.count("T")
            li_t.append(t)

            c=line.count("C")
            li_c.append(c)

            g=line.count("G")
            li_g.append(g)

            tot = line.count("")
            totaal.append(tot)

        i = 0
        while i < aantal  :                         #het gekozen aantal printen
            i += 1
            if li_a[i]+li_t[i]+li_c[i]+li_g[i] == (totaal[i] -2):
                print(headers_li[i],"-dit is mRNA")  #het totaal vergelijken
                print(50*"-")
            else:
                print(headers_li[i],"-dit is geen mRNA")
                print(50*"-")
    except IndexError:
        print("geen fasta bestand")
        quit()
            
def knipt(seqs_li, headers_li, aantal):
    
    bestand =   open("enzymen.txt")            #het bestand van afvink4
    list1    =   []
    i2       =   0
    i3       =   0
    
    
    try:
        while i2 < aantal:                          #het gekozen aantal printen
            i2 += 1
            for line in bestand:
                enzym, seq = line.split()               #enzym en seq splitsen
                seq = seq.replace("^","")
                list1.append(seq)
                
                for l in seqs_li[:aantal]:
                    x = seqs_li[i3].find(seq)               #is er een match?
                    i3 += 1
                    if x > 0:
                        print(x)
                        print("match met",enzym, "met sequentie van:")      #print de match met de positie
                        print(headers_li[i3])
                        print("op positie",x)    
                        print(seqs_li[i3])
                        print((x-1)*"-",seq)
                        print(50*"-")
    except IndexError:
        print("fout bestand")
        quit()

                  
main()
