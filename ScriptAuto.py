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
    critical = ['Windows Update', 'Service antivirus Microsoft Defender', 'Journal d’événements Windows']
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
    services_critiques_windows = ['Windows Update', 'Microsoft Defender Antivirus Service', 'Windows Event Log']
    print("\nServices critiques pour Windows:")
    filter = [s for s in running if s in services_critiques_windows]
    for s in filter:
        print(f"- {s}")
    # Array filtré les services actifs pour Windows
    services_actifs_windows = [s for s in running if s in services_critiques_windows]
    print("\nServices actifs pour Windows:")
    for s in services_actifs_windows:
        print(f"- {s}")





