# ScriptAuto.py - Automatisation de l'Inventaire des Services Actifs et Vérification de Conformité

## Description

Ce script Python automatise l'inventaire des services actifs sur un système Windows et effectue une vérification de conformité en s'assurant que certains services critiques sont en cours d'exécution.

### Fonctionnalités

- **Inventaire des Services Actifs** : Récupère la liste de tous les services Windows et filtre ceux qui sont actuellement en état "RUNNING".
- **Vérification de Conformité** : Vérifie si une liste prédéfinie de services critiques est active. Si un service critique est arrêté, un avertissement est généré.

### Services Critiques Vérifiés

- `wuauserv` : Service de mise à jour Windows
- `WinDefend` : Service de sécurité Windows Defender
- `EventLog` : Service de journalisation des événements

## Prérequis

- Python 3.x installé sur le système.
- Système d'exploitation Windows (le script utilise la commande `sc query` native).
- Privilèges administrateur pour exécuter le script (recommandé pour interroger les services système).

## Installation

1. Téléchargez ou copiez le fichier `ScriptAuto.py` dans un répertoire de votre choix.
2. Assurez-vous que Python est accessible via la ligne de commande.

## Utilisation

1. Ouvrez un terminal de commande (avec privilèges administrateur si nécessaire).
2. Naviguez vers le répertoire contenant le script :
   ```
   cd chemin\vers\le\script
   ```
3. Exécutez le script :
   ```
   python ScriptAuto.py
   ```

### Exemple de Sortie

```
Services Actifs:
- wuauserv : Windows Update
- WinDefend : Microsoft Defender Antivirus Service
- EventLog : Windows Event Log

Tous les services critiques sont conformes.
```

Ou en cas de problème :

```
Services Actifs:
- wuauserv : Windows Update
- EventLog : Windows Event Log

Problèmes de Conformité:
- Le service critique WinDefend n'est pas en cours d'exécution
```

## Personnalisation

- **Liste des Services Critiques** : Modifiez la liste `critical_services` dans la fonction `main()` pour ajouter ou supprimer des services à vérifier.
- **Format de Sortie** : Le script imprime les résultats dans la console. Vous pouvez modifier le code pour exporter vers un fichier (par exemple, en ajoutant `with open('rapport.txt', 'w') as f: f.write(...)`).

## Gestion des Erreurs

- Si la commande `sc query` échoue, le script affiche un message d'erreur et retourne une liste vide.
- Assurez-vous que la commande `sc` est disponible (elle l'est par défaut sur Windows).

## Licence

Ce script est fourni tel quel, sans garantie. Utilisez-le à vos propres risques.

## Auteur

Généré automatiquement pour automatiser les tâches d'inventaire et de conformité.