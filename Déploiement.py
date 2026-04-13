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
