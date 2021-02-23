---
layout: default
title : Etude des éléments associés à un ticket qui influent les premiers commits d’un nouveau contributeur.
date:   2021-01-03 22:00:00 +0100
---

---

> **Date de rendu finale : Mars 2021 au plus tard**
> - Respecter la structure pour que les chapitres soient bien indépendants
> - Remarques :
>>    - Les titres peuvent changer pour être en adéquation avec votre étude.
>>    - De même il est possible de modifier la structure, celle qui est proposée ici est là pour vous aider.
>>    - Utiliser des références pour justifier votre argumentaire, vos choix etc.

---

**_janvier 2021_**

## Auteurs

Nous sommes quatre étudiants en dernière année d'ingénierie informatique à Polytech Nice-Sophia, spécialisés en architecture logicielle :

* Paul-Marie DJEKINNOU <[paul-marie.djekinnou@etu.univ-cotedazur.fr](paul-marie.djekinnou@etu.univ-cotedazur.fr)>
* Paul KOFFI <[merveille.koffi@etu.univ-cotedazur.fr](merveille.koffi@etu.univ-cotedazur.fr)>
* Florian AINADOU <[florian.ainadou@etu.univ-cotedazur.fr](florian.ainadou@etu.univ-cotedazur.fr)>
* Djotiham NABAGOU <[djotiham.nabagou@etu.univ-cotedazur.fr](djotiham.nabagou@etu.univ-cotedazur.fr)>

## I. Contexte du projet

```
(Préciser ici votre contexte.)
```
Les tickets permettent-ils une meilleure compréhension de l’architecture d’un système ?\
Tel est le sujet qui nous a intéressé parmi ceux qui étaient proposés.

```
(Pourquoi c'est intéressant.)
```
A Polytech Nice-Sophia, nous avons appris à développer de façon AGILE ces trois dernières années en utilisant des outils de VCS adéquats tel que Git dont la plateforme en ligne Github n'est plus à présenter.
Pour organiser au mieux notre développement, nous avons appris à utiliser les nombreuses fonctionnalités que Github mettait à notre disposition.\
Parmi ces fonctionnalités, l'une d'entre elle devenue incontournable aujourd'hui est l'utilisation des tickets.\
Ils permettent de documenter le code publié tout le long du projet et d'établir ainsi une traçabilité des fonctionnalités implémentées dans le temps.\
Pour une entité qui décide d'utiliser Github comme son outil de VCS, les tickets peuvent alors fournir une description de l'architecture de leur système.\
Mais est-elle complète ? Sous quelle forme se présente-t-elle ? Est-elle facile à comprendre et surtout comment procéder pour la mettre en oeuvre ?\
Telles sont les raisons qui nous ont tout de suite incité à nous intéresser à ce sujet.

De plus, en effectuant des recherches, nous avons remarqué qu'il n'y a pas que Github qui utilise ce système de tickets.\
De grandes firmes telles que Mozilla, Google ou encore MongoDB possèdent leurs propres gestionnaires de tickets (Bugzilla, IssueTracker, Jira...) et ils ont également l'avantage d'être Open Source pour la plupart.\
Ayant donc à disposition un catalogue de projets que nous pouvions étudier, le choix du sujet était devenu définitif.


![Figure 1: Logo UCA, exemple, vous pouvez l'enlever](../assets/model/UCAlogoQlarge.png){:height="25px" }


## II. Observations - Question générale

```
(1. Commencez par formuler une question sur quelque chose que vous observez ou constatez ou encore une idée émergente. Attention pour répondre à cette question vous devrez être capable de quantifier vos réponses.)
(2. Préciser bien pourquoi cette question est intéressante de votre point de vue et éventuellement en quoi la question est plus générale que le contexte de votre projet \(ex: Choisir une libraire de code est un problème récurrent qui se pose très différemment cependant en fonction des objectifs)\ Cette première étape nécessite beaucoup de réflexion pour se définir la bonne question afin de poser les bonnes bases pour la suit.
```
Le contexte du projet étant choisi, il nous fallait une question générale pour tenter d'y répondre.\
Nous avons essayé de remonter à la source en se disant qu'il n'existe pas d'architecture sans contributeurs pour la concevoir.\
Nous nous sommes donc recentrés sur les contributeurs en se posant les questions suivantes :
En quoi consistent les premiers commits d'un nouveau contributeur de projet ? Appréhende-t-il toute l'architecture du système avant de commencer à contribuer ? Utilise-t-il les tickets dès sa première contribution et si oui, comment les utilise-t-il ?\
Ces pistes nous ont permis de nous mettre d'accord sur une question générale qu'est :\
**Quels sont les éléments d'un ticket, qui influent les premiers commits d'un nouveau contributeur ?**\
Pour répondre à cette question, nous avons énuméré deux sous-questions :\
* Quelles issues sont prises par les contributeurs pour rentrer dans un projet open source ?
* Quelles sont les caractéristiques communes à ces tickets (patrons de conception, éléments plus spécifiques sur les tickets) ?

## III. Collecte d'informations
```
Préciser vos zones de recherches en fonction de votre projet,

1. les articles ou documents utiles à votre projet
2. les outils
```
Pour répondre aux questions posées, il nous fallait des projets à analyser sur lesquels poser nos hypothèses et y répondre.\
Nous nous sommes encore une fois recentrés sur Github car nous étions familiers à son utilisation d'une part et nous avions à notre disposition l'API Github qui permet de faire des tests à grande échelle.\
Nous avons ainsi choisi les projets open source suivants :

* [Flutter](https://github.com/flutter/flutter)
* [Vscode](https://github.com/microsoft/vscode)
* [Facebook-React-Native](https://github.com/facebook/react-native)
* [Kubernetes](https://github.com/kubernetes/kubernetes)
* [Tensorflow](https://github.com/tensorflow/tensorflow)

Pourquoi ceux-là et pas d'autres ? Tout d'abord parce qu'ils sont open source ce qui nous permet un libre accès pour nos analyses.\
Ensuite parce que ce sont de gros projets qui regorgent de beaucoup de contributeurs, de quoi faire une analyse exhaustive.
Nous avons également consulté l'article d'un groupe de la promotion 2019 qui portait sur l'amélioration des intégrations des contributeurs et la pérennité de la communauté :

**[How to improve contributors onboarding](https://rimel-uca.github.io/chapters/2019/code-quality-in-open-source-projects-xwiki-2019/contents)**

Dans cet article, les auteurs étudient les facteurs qui attirent les contributeurs dans un projet open source pour tenter d'introduire une dynamique de contribution et pérenniser la communauté de contributeurs.\
L'analyse de grands projets tels JUnit5, Mockito, Hibernate, Apache Log4j2 et XWiki leur a permis de réaliser un sondage autour de la complexité des projets open source, l'investissement des mainteneurs de ces projets et la communication au sein de la communauté.

Parallèlement à notre étude qui traite des tickets comme points d'entrée d'un contributeur dans un projet open source, cet article traite plutôt des raisons ou motivations qui poussent les contributeurs à rejoindre un projet et propose des moyens d'amélioration des intégrations qu'ils effectuent sur les projets.\
Un contributeur peut très bien être payé pour contribuer sur un projet mais ses contributions seront-elles aussi efficaces ou innovantes que s'il appartenait à une communauté étroitement soudée sur laquelle il peut compter et si ses contributions représentaient pour lui un objectif personnel, un moyen de démontrer ses capacités et performances ?\
Et pour les mainteneurs, la complexité de leurs projets est-elle si importante qu'elle nécessite de recourir à des contributeurs externes ?\
Voici entre autres les principales questions auxquelles les auteurs de cet article ont tenté de répondre. 

S'intéresser à leur étude nous a permis d'avoir une approche différente mais semblable de notre problème.\
En effet le choix des `KPI` utilisés pour corroborer ou infirmer les différentes hypothèses émises pour leur étude peut nous aider ou influer sur nos propres choix.\
Ayant décidé d'analyser les `labels`, `issues` et `commits` liés aux contributeurs pour répondre à nos hypothèses, le fait de retrouver ces `KPI` également au sein de leur article nous confirme d'une certaine façon que nous analysons les bonnes données. Les résultats des expérimentations nous en dirons plus.

 
## IV. Hypothesis & Experiences

### Outils utilisés

Pour effectuer nos expériementation et répondre à nos questions, nous avons décidé d'utiliser l'api **`github`** qui nous permet de récupérer des diverses informations comme les commits d'un projets, les issues d'un dépôt ou encore les différents contributeurs, etc... Des scripts `Python` pour effectuer des requêtes vers l'api avec la librairie `Requests` et `Pyplot`  pour la mise en forme des différents résultats obtenus par nos scripts.

### Démarches

Pour répondre à la question suivante: quels sont les labels des premiers commits étiquettés ?

Pour répondre à cette problématique nous avons dans un premiers temps recherché dans l'api github l'url nous permettant de récupérer les commits sur un projet particulier d'un contributeur. Suite à cela on se retrouvait dans une première impasse qui était le fait que l'api github ne renvoie que 30 éléments par requête et donc il fallait se déplacer dans les pages. Nous avons manuellement cherché la dernière page puis à partir de cette dernière pour analyser les trois dernières pages de commits. Mais cette méthode ne convenait pas et nous sommes mis à chercher une information nous permettant de récupérer la dernière page de n'importe quelle requête. Une fois trouvé nous nous sommes replongés dans l'avancée de notre expérience. Cette fois-ci, nous parcourions tous les commits des 3 dernières pages et pour chacun d'entre eux nous effectuons une analyse sur le message du commit ( qui se trouve dans à cet endroit dans le corps de la réponse d'un commit). L'analyse sur le message du commit étati de savoir si ce dernier comprenait un hashtag car c'était la condition pour reconnaître un commit étiquetté. (Est ce qu'on parle ici du fait qu'on ait tombé sur des projets qui utilisait un autre système de gestions de tickets)

Ensuite nous devions recenser tous les labels associés aux différentes issues que nous avons trouvées sur les trois dernières page de commits étiquettés par contributeur qu'on nous avons analysés. Pour cela, comme pour trouver si un commit était étiquetté ou pas nous avions analysé le message de ce dernier. Il suffisait de récupérer le nombre qui se trouve juste après le hashtag. Une fois cela fait, on réeffectuait une requête sur l'api afin de récupérer dans le corps de la réponse de l'issue les labels associés à cette dernière ( qui se trouve à cet endroit). Et pour terminer pour chacun de ces labels nous l'enregistrons dans un fichier json qui avait pour `nom nom_de_l'organisation-nom_du_projet.json` avec le nombre de fois qu'il apparaît. Et si nous faisions un autre contributeur même projet nous mettions à jour les valeurs en cumulant.

Question 2 ...les plus fréquents ? C'est - à - dire sur l'ensembles des premiers commits des contributeurs quels sont les labales qui ressortent le plus ?

1. Il s'agit ici d'énoncer sous forme d' hypothèses ce que vous allez chercher à démontrer. Vous devez définir vos hypothèses de façon à pouvoir les _mesurer facilement._ Bien sûr, votre hypothèse devrait être construite de manière à v_ous aider à répondre à votre question initiale_.Explicitez ces différents points.
2. Test de l’hypothèse par l’expérimentation. 1. Vos tests d’expérimentations permettent de vérifier si vos hypothèses sont vraies ou fausses. 2. Il est possible que vous deviez répéter vos expérimentations pour vous assurer que les premiers résultats ne sont pas seulement un accident.
3. Explicitez bien les outils utilisés et comment.
4. Justifiez vos choix

## V. Analyse des résultats & Conclusion

1. Analyse des résultats & construction d’une conclusion : Une fois votre expérience terminée, vous récupérez vos mesures et vous les analysez pour voir si votre hypothèse tient la route. 

## VI. Outils

Précisez votre utilisation des outils ou les développements \(e.g. scripts\) réalisés pour atteindre vos objectifs. Ce chapitre doit viser à \(1\) pouvoir reproduire vos expérimentations, \(2\) partager/expliquer à d'autres l'usage des outils.

## VI. References

1. [Flutter](https://github.com/flutter/flutter)
2. [Vscode](https://github.com/microsoft/vscode)
3. [Facebook-React-Native](https://github.com/facebook/react-native)
4. [Kubernetes](https://github.com/kubernetes/kubernetes)
5. [Tensorflow](https://github.com/tensorflow/tensorflow)