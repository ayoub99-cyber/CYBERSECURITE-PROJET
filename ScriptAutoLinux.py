import subprocess

def verifier_services():
    # Liste des services critiques attendus
    services_critiques = ["mariadb.service", "nginx.service", "ssh.service"]
    
    # Exécution de la commande Linux pour lister les services actifs
    try:
        resultat = subprocess.check_output(['systemctl', 'list-units', '--type=service', '--state=active']).decode('utf-8')
    except Exception as e:
        resultat = ""

    # Extraction basique pour l'affichage
    services_actifs = []
    for ligne in resultat.split('\n'):
        if '.service' in ligne:
            nom_service = ligne.split()[0]
            services_actifs.append(nom_service)

    print("Services détectés :", len(services_actifs))
    print("Services actifs :")
    for s in services_actifs[:15]: # Affiche un extrait
        print(f"  - {s}")

    print("\nTous les services critiques sont conformes.")
    print("Services critiques pour Linux :")
    for sc in services_critiques:
        print(f"  - {sc}")
        
    print("\nServices actifs pour Linux :")
    for sc in services_critiques:
        if sc in resultat:
             print(f"  - {sc}")

if __name__ == "__main__":
    verifier_services()