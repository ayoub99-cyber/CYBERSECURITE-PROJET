# DEPLOIEMENT D'UN SCRIPT PYTHON POUR AUTOMATISER L'INVENTAIRE DES SERVICES ACTIFS ET LA VERIFICATION DE LA CONFORMITE.

import subprocess
from unittest import result
def main():
    # Récupérer les services actifs
    result = subprocess.run(['systemctl', 'list-units', '--type=service', '--state=running'], capture_output=True, text=True)
    running = [line.split()[0] for line in result.stdout.split('\n') if line.endswith('running')]

    print("Services actifs:")
    for s in running:
        print(f"- {s}")

    # Services critiques (noms d'affichage)
    critical = ['ssh.service', 'nginx.service', 'mysql.service']
    issues = [c for c in critical if c not in running]

    if result.returncode != 0:
        print("Erreur lors de l'exécution de la commande:", result.stderr)
    elif issues:
        print("\nProblèmes de conformité:")
        for i in issues:
            print(f"- {i} non actif")
    else:
        print("\nTous les services critiques sont conformes.")

    # Array filtré des services critiques pour Linux
    services_critiques_linux = ['ssh.service', 'nginx.service', 'mysql.service']
    print("\nServices critiques pour Linux:")
    filter = [s for s in running if s in services_critiques_linux]
    for s in filter:
        print(f"- {s}")
    # Array filtré les services actifs pour Linux
    services_actifs_linux = [s for s in running if s in services_critiques_linux]
    print("\nServices actifs pour Linux:")  
    for s in services_actifs_linux:
        print(f"- {s}")
    