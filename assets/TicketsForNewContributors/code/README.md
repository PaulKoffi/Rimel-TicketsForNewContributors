# Rimel-TicketsForNewContributors

## Auteurs

* Paul-Marie DJEKINNOU <[paul-marie.djekinnou@etu.univ-cotedazur.fr](paul-marie.djekinnou@etu.univ-cotedazur.fr)>
* Paul KOFFI <[merveille.koffi@etu.univ-cotedazur.fr](merveille.koffi@etu.univ-cotedazur.fr)>
* Florian AINADOU <[florian.ainadou@etu.univ-cotedazur.fr](florian.ainadou@etu.univ-cotedazur.fr)>
* Djotiham NABAGOU <[djotiham.nabagou@etu.univ-cotedazur.fr](djotiham.nabagou@etu.univ-cotedazur.fr)>

## Prérequis

Pour rejouer les expérimentations du projet, vous devez disposer de Python 3.8.0 ou supérieur.\
Selon votre version de python, exécutez l'une des commandes suivantes pour installer toutes les librairies Python requises.
* `python -m pip install -r requirements.txt`
* `python3 -m pip install -r requirements.txt`

## Expérimentations
### 1- Exécution
Le [code](commitsWithCLI.py) produit a pour but d'analyser un projet passé en paramètre sur un échantillon de premiers commits d'un contributeur également passé en paramètre.\
La commande qui exécute le script prend en argument les options suivantes :
* `'-o' ou '--owner' : Nom de l'organisation Github du projet`
* `'-r' ou '--repo' : Nom du dépôt Github du projet`
* `'-n' ou '--name' : Nom du contributeur passé en paramètre`
* Exemple de commande : `python3 commitsWithCLI.py -o microsoft -r vscode -n mjbvz`

PS : Afin de pouvoir reproduire l'expérience partout, le projet est analysé sur un échantillon de ? premiers commits du contributeur passé en paramètre car Github impose une limite de 5000 requêtes par heure (ou 80 appels par minute) à l'API.\
Ce script peut donc épuiser le nombre de requêtes disponibles en une seule exécution.\
Toutefois, ce problème peut être contourné par l'utilisation d'un VPN.\
Lorsque la limite est atteinte, toute requête vers l'API Github renvoie le code Json suivant :
```
{
    "message": "API rate limit exceeded for <<your_ip_address>>. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)",
    "documentation_url": "https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting"
}
```
Comme le précise le message, une authentification Github via un token permet d'augmenter la limite du nombre de requêtes pouvant être exécutées en une heure.\
Mais si l'on dispose d'un VPN, il suffit de changer de localisation pour pouvoir exécuter à nouveau le script.

### 2- Résultats
Une fois exécuté, le résultat du script est enregistré dans un fichier json contenu dans le répertoire [results](results) et ayant pour nom : `nom_organisation_github`-`nom_depot_github`.`json`.\
On y retrouve les attributs suivants :
* `"infosCommits"` qui contient les informations suivantes sur les commits analysés :
    * `"nombreTotalDeCommitsAnalyses"` : c'est le nombre total de commits analysés.
    * `"nombreDeCommitsEtiquettesAnalyses"` : c'est le nombre de commits analysés qui référencent des tickets.
    * `"nombreDeCommitsNonEtiquettesAnalyses"` : c'est le nombre de commits analysés qui ne référencent pas de tickets.
    

* `"infosIssues"` qui contient les informations suivantes sur les tickets analysés :
    * `"nombreTotalIssuesAnalysees"` : c'est le nombre total de tickets analysés.
    * `"nombreIssuesLabelisees"` : c'est le nombre total de tickets analysés qui référencent des labels.
    * `"nombreIssuesNonLabelisees"` : c'est le nombre total de tickets analysés qui ne référencent pas de labels.
    * `"nombreIssuesNonLabeliseesQuiReference"` : c'est le nombre total de tickets analysés qui ne référencent pas de labels mais d'autres tickets.


* `"labels"` qui contient les informations sur les différents labels répertoriés et leur nombre.

Ces attributs sont ensuite utilisés pour générer des graphes explicatifs des résultats obtenus.\
Ces graphes sont contenus dans le répertoire [results](../charts) sous format image.\
Pour générer ces graphes, nous utilisons les scripts suivants : [bartChart.py](bartChart.py) et [pieChart.py](pieChart.py).\
Il est configurable manuellement en passant en entrée le bon fichier json.

