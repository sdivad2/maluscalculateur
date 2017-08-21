print("Calcul des conséquences d'un malus en cas de sinistre")
print("")
prime = round(float(input("Montant actuel annuel de votre prime d'assurance")),2)
crm = round(float(input("Voéfficient actuel ?")),2)
if (crm==0.5):
    caspart1 = input("Etes vous au coéfficient 0.5 depuis au moins 3 ans sans aucun sinistre ? o/n")
resp = input("1. Responsabilité totale, malus 25%  --- 2. Responsabilité partagée, maluss 12.5%")
franchise = round(float(input("Montant de la franchise ?")),2)
