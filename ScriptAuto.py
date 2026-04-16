# DEPLOIEMENT D'UN SCRIPT PYTHON POUR AUTOMATISER L'INVENTAIRE DES SERVICES ACTIFS ET LA VERIFICATION DE LA CONFORMITE.

import subprocess
from unittest import result

def main():
    # Récupérer les services actifs
    result = subprocess.run(['net', 'start'], capture_output=True, text=True)
    running = [line.strip() for line in result.stdout.split('\n') if line.strip()]

    print("Services actifs:")
    for s in running:
        print(f"- {s}")

    # Services critiques (noms d'affichage)
    critical = ['Windows Update','Pare-feu Windows Defender', 'Service antivirus Microsoft Defender', 'Journal d’événements Windows']
    issues = [c for c in critical if c not in running]

    if issues:
        print("\nProblèmes de conformité:")
        for i in issues:
            print(f"- {i} non actif")
    elif result.returncode != 0:
        print("Erreur lors de l'exécution de la commande:", result.stderr)
    else:
        print("\nTous les services critiques sont conformes.")
     # Array filtré des services critiques pour Windows
    services_critiques_windows = ['Windows Update','Pare-feu Windows Defender', 'Service antivirus Microsoft Defender', 'Journal d’événements Windows'] 
    print("\nServices critiques pour Windows:")
    filter = [s for s in running if s in services_critiques_windows]
    for s in filter:
        print(f"- {s}")
    # Array filtré les services actifs pour Windows
    services_actifs_windows = [s for s in running if s in services_critiques_windows]
    print("\nServices actifs pour Windows:")
    for s in services_actifs_windows:
        print(f"- {s}")

if __name__ == "__main__":    main()  
    #récupation des log a partir des Arrays filtrés des services critiques et actifs pour Windows
array_services_critiques_windows = ['Windows Update','Pare-feu Windows Defender', 'Service antivirus Microsoft Defender', 'Journal d’événements Windows']
array_services_actifs_windows = ['Windows Update','Pare-feu Windows Defender', 'Service antivirus Microsoft Defender']
print("\nRécupération des logs pour les services critiques et actifs:")
for service in array_services_critiques_windows:
    if service in array_services_actifs_windows:
        print(f"Récupération des logs pour {service}...")
        result = subprocess.run(['wevtutil', 'qe', service, '/q:"*[System[TimeCreated[timediff(@SystemTime) <= 3600000]]]"', '/f:text'], capture_output=True, text=True)
        print(result.stdout)
        





