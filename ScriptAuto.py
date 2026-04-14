# DEPLOIEMENT D'UN SCRIPT PYTHON POUR AUTOMATISER L'INVENTAIRE DES SERVICES ACTIFS ET LA VERIFICATION DE LA CONFORMITE.

import subprocess

def main():
    # Récupérer les services actifs
    result = subprocess.run(['net', 'start'], capture_output=True, text=True)
    running = [line.strip() for line in result.stdout.split('\n') if line.strip()]

    print("Services actifs:")
    for s in running:
        print(f"- {s}")

    # Services critiques (noms d'affichage)
    critical = ['Windows Update', 'Microsoft Defender Antivirus Service', 'Windows Event Log']
    issues = [c for c in critical if c not in running]

    if issues:
        print("\nProblèmes de conformité:")
        for i in issues:
            print(f"- {i} non actif")
    else:
        print("\nTous les services critiques sont conformes.")
    elif result.returncode != 0:
        print("Erreur lors de l'exécution de la commande:", result.stderr)  
    

