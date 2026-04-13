# DEPLOIEMENT D'UN SCRIPT PYTHON POUR AUTOMATISER L'INVENTAIRE DES SERVICES ACTIFS ET LA VERIFICATION DE LA CONFORMITE.

import process

def main():
    # Récupérer les services actifs
    result = process.run(['systemctl', 'list-units', '--type=service', '--state=running'], capture_output=True, text=True)
    running = [line.split()[0] for line in result.stdout.split('\n') if line.endswith('running')]

    print("Services actifs:")
    for s in running:
        print(f"- {s}")

    # Services critiques (noms d'affichage)
    critical = ['ssh.service', 'nginx.service', 'mysql.service']
    issues = [c for c in critical if c not in running]

    if issues:
        print("\nProblèmes de conformité:")
        for i in issues:
            print(f"- {i} non actif")
    else:
        print("\nTous les services critiques sont conformes.")