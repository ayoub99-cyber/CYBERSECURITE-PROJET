import ScriptAuto
import ScriptAutoLinux
import subprocess
#démarrage du script de déploiement
def main():
    print("Souhaitez-vous exécuter le script de déploiement pour Windows(1) ou Linux(2) ? (1/2)")
    choix = input()
    if choix == "1":
        ScriptAuto.main()
    elif choix == "2":
        ScriptAutoLinux.main()
    else:
        print("Choix invalide Veuilliez Réssayez .")
#Résultat du script de déploiement
print("Script de déploiement terminé. Veuillez vérifier les résultats ci-dessus pour les services actifs et les problèmes de conformité.")
if __name__ == "__main__":    main()    
# afichage des logs et des messages sur Windows 
def afficher_logs_windows():
    print("Affichage des logs pour Windows...")
    # Exemple de commande pour afficher les logs d'un service spécifique (ex: sshd)
    subprocess.run(['powershell', '-Command', 'Get-EventLog -LogName Application -Source sshd -Newest 10'], check=True) 
# afichage des logs et des messages sur Linux
def afficher_logs_linux():
    print("Affichage des logs pour Linux...")
    # Exemple de commande pour afficher les logs d'un service spécifique (ex: ssh)
    subprocess.run(['journalctl', '-u', 'ssh.service', '-n', '10'], check=True)
result = input("Souhaitez-vous afficher les logs pour Windows(1) ou Linux(2) ? (1/2)")
if result == "1":   afficher_logs_windows()
elif result == "2":   afficher_logs_linux()
else:   print("Choix invalide Veuilliez Réssayez .")
   # Récuperation des Array de services critiques pour les deux systèmes
services_critiques_windows = ['Windows Update', 'Microsoft Defender Antivirus Service', 'Windows Event Log']
services_critiques_linux = ['ssh.service', 'nginx.service', 'mysql.service']
print("\nServices critiques pour Windows:")
for service in services_critiques_windows:  print(f"- {service}")
print("\nServices critiques pour Linux:")   
for service in services_critiques_linux:    print(f"- {service}")