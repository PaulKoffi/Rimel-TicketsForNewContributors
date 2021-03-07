---
layout: default
title : Etude des éléments associés à un ticket qui influent les premiers commits d’un nouveau contributeur.
date:   2021-01-03 22:00:00 +0100
---

## Auteurs

Nous sommes quatre étudiants en dernière année d'ingénierie informatique à Polytech Nice-Sophia, spécialisés en architecture logicielle :

* Paul-Marie DJEKINNOU <[paul-marie.djekinnou@etu.univ-cotedazur.fr](paul-marie.djekinnou@etu.univ-cotedazur.fr)>
* Paul KOFFI <[merveille.koffi@etu.univ-cotedazur.fr](merveille.koffi@etu.univ-cotedazur.fr)>
* Florian AINADOU <[florian.ainadou@etu.univ-cotedazur.fr](florian.ainadou@etu.univ-cotedazur.fr)>
* Djotiham NABAGOU <[djotiham.nabagou@etu.univ-cotedazur.fr](djotiham.nabagou@etu.univ-cotedazur.fr)>

## I. Contexte du projet

Les tickets permettent-ils une meilleure compréhension de l’architecture d’un système ?\
Tel est le sujet qui nous a intéressé parmi ceux qui étaient proposés.

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

Le contexte du projet étant choisi, il nous fallait une question générale pour tenter d'y répondre.\
Nous avons essayé de remonter à la source en se disant qu'il n'existe pas d'architecture sans contributeurs pour la concevoir.\
Nous nous sommes donc recentrés sur les contributeurs en se posant les questions suivantes :
En quoi consistent les premiers commits d'un nouveau contributeur de projet ? Appréhende-t-il toute l'architecture du système avant de commencer à contribuer ? Utilise-t-il les tickets dès sa première contribution et si oui, comment les utilise-t-il ?\
Ces pistes nous ont permis de nous mettre d'accord sur une question générale qu'est :

**Quels sont les éléments d'un ticket qui permettent à un nouveau contributeur d'intégrer le développement d'un projet ?**

Pour répondre à cette question, nous avons énuméré deux sous-questions :
* Les premiers commits d'un contributeur sont ils toujours associés à des tickets existants ?
* Quelles sont les caractéristiques communes à ces tickets (types de labels, format du titre, description) ?

## III. Collecte d'informations

Pour répondre aux questions posées, il nous fallait des projets à analyser sur lesquels poser nos hypothèses et y répondre.\
Nous nous sommes encore une fois recentrés sur Github car nous étions familiers à son utilisation d'une part et nous avions à notre disposition l'API Github qui permet de faire des tests à grande échelle.\
Nous avons ainsi choisi les projets open source suivants :

* [Flutter](https://github.com/flutter/flutter)
* [Vscode](https://github.com/microsoft/vscode)
* [Facebook-React-Native](https://github.com/facebook/react-native)
* [Kubernetes](https://github.com/kubernetes/kubernetes)
* [Tensorflow](https://github.com/tensorflow/tensorflow)
* [Ansible](https://github.com/ansible/ansible)
* [OhmyZsh](https://github.com/ohmyzsh/ohmyzsh)
* [Linux](https://github.com/torvalds/linux)

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

 
## IV. Hypothèses et expérimentations
```
1. Il s'agit ici d'énoncer sous forme d' hypothèses ce que vous allez chercher à démontrer. Vous devez définir vos hypothèses de façon à pouvoir les _mesurer facilement._ Bien sûr, votre hypothèse devrait être construite de manière à v_ous aider à répondre à votre question initiale_.Explicitez ces différents points.
2. Test de l’hypothèse par l’expérimentation. 1. Vos tests d’expérimentations permettent de vérifier si vos hypothèses sont vraies ou fausses. 2. Il est possible que vous deviez répéter vos expérimentations pour vous assurer que les premiers résultats ne sont pas seulement un accident.
3. Explicitez bien les outils utilisés et comment.
4. Justifiez vos choix
```

### 1. Outils utilisés

Pour effectuer nos expérimentations et répondre à nos questions, nous avons décidé d'utiliser : 

* l'`API Github` qui nous permet de récupérer les informations liées aux projets tels que les `commits`, les `issues` ou encore les différents contributeurs, etc.
* Des scripts `Python` pour effectuer des requêtes vers l'API avec la librairie `Requests` et `Pyplot` pour la mise en forme des différents résultats obtenus par nos scripts.

### 2. Démarche
Pour tenter de répondre à notre question, il nous fallait répondre aux deux sous-questions. Nous avons donc émis une hypothèse tout d'abord pour la première sous-question :

<div style="text-align: justify">

> * Sous-question 1 : Les premiers commits d'un contributeur sont ils toujours associés à des tickets existants ?

Notre hypothèse consiste en celle-ci : **Le premier commit d'un contributeur est associé à un ticket existant.**

Pour répondre à cette question, nous avons eu besoin des premiers commits des différents contributeurs de plusieurs projets. Puisque nous parlons d'intégration dans un projets, cette intégration est représentée par les premiers commits. Nous analyserons ces commits afin de savoir s'ils sont associés à des tickets existants ce qui les définirait comme des `commits étiquetés`.

Pour obtenir notre réponse, nous avons dans un premier temps recherché dans l'API Github l'url nous permettant de récupérer les commits d'un contributeur sur un projet particulier.
Suite à cela on se retrouvait dans une première impasse : l'API ne renvoyait que trente(30) éléments d'une requête.
Pour une requête qui doit récupérer les commits d'un contributeur par exemple, la requête ne renvoie que les trente derniers commits du contributeur.
Ceci est dû au système de pagination que Github a mis en place pour éviter de renvoyer toutes les données (données qui peuvent être très volumineuses selon la requête) d'une requête et ainsi éviter de surcharger l'API.
Une des contraintes liées à notre analyse a d'ailleurs été la limitation du nombre de requêtes pouvant être effectuées en 1h : 5000 requêtes en 1h. Dépassé ce seuil, il faut attendre patiemment que les 1h soient écoulées.

Il nous fallait donc se déplacer dans les différentes pages, la difficulté étant de trouver la dernière page, celle qui contient les premiers commits du contributeur.
Nous avons manuellement cherché la dernière page puis à partir de ce point de repère, nous avons analysé les trois dernières pages de commits.
Mais cette méthode ne convenait pas car on manœuvrait par tâtonnement pour trouver la dernière page. Nous nous sommes donc mis à chercher une information nous permettant de récupérer la dernière page de n'importe quelle requête.
Notre script analysait alors les informations récupérées dans les en-têtes des réponses retournées par le serveur pour tenter de retrouver les informations sur la pagination et indirectement sur la dernière page.
Une fois trouvée nous nous sommes replongés dans l'avancée de notre expérience. Cette fois-ci, nous parcourions tous les commits des 3 dernières pages et pour chacun d'entre eux nous effectuons une analyse sur le message du commit ( qui se trouve dans à cet endroit dans le corps de la réponse d'un commit). L'analyse sur le message du commit était de savoir si ce dernier comprenait un hashtag car c'était la condition pour reconnaître un commit étiquetté.
</div>

<div style="text-align: justify">

> * Sous-question 2 : Quelles sont les caractéristiques communes à ces tickets (types de labels, format du titre, description) ?

Ici nous avons le choix entre les labels, le format du titre du ticket ou encore sa description. Pour la description nous avons supposé qu'elle ne pouvait être vraiment mesurable car celle-ci donnait juste des détails sur ce qui était attendu par rapport au ticket concerné et donc faisait plus appel à la compréhension du language humain de la part du contributeur qui pourrait choisir ou pas cet ticket. Donc concrètement c'était une caractéristique qui ne nous aurait pas permis de répondre à notre sous question.

Le titre du ticket est dans le même cas que la description mais nous avons pensé que contrairement à la description le titre pouvait avoir un certain format d'écriture qui pourrait nous permettre de répondre à notre question. En effet suite à la lecture d'un projet de rétro l'année dernière ***[Comment les bibliothèques de codes de Machine Learning évoluent-elles ?](https://github.com/RIMEL-UCA/RIMEL-UCA.github.io/blob/master/chapters/2020/MLAndEvolution/model2020.md)*** qui disait à un moment que le format du commit pouvait suivre une certaine logique comme par exemple si le contributeur commit sur un bug il écrira dans le message de son commit `[Bug]` suivi de ce qu'il souhaitait dire. Nous avons pensé du coup utilisé cette logique dans le format d'écriture du titre d'un ticket. Mais cette idée n'a pas été retenu car nous nous somme rendus compte après une brève recherches dans les dépots github que cette approche d'écriture n'était pas fortement utilisé et donc nous n'aurions pas eu des résultats convaincants après analyse surtout qu'il y avait plusieurs façon d'écrire comme le stipule le projet de rétro.

Notre dernière caractéristique est donc le label. Cette caractéristique est très fortement utilisée dans les dépôts Github pour les tickets mais aussi pour les pull requests.
Ce dernier apporte une indication assez forte sur le ticket qui est le type c'est-à-dire qu'un ticket avec pour label `bug` sans même lire le titre ou la description le contributeur sait qu'il a à faire à un bug à qui demande à être corrigé ou encore `help wanted` où une aide est souhaitée sur ce ticket. On peut penser qu'un contributeur peut selon son envie se concentrer sur des types de tickets. Ce qui à fortement favoriser une étude sur les labels est aussi le fait que sur beaucoup de projets nous avons remarqué la présence de labels tels que good first issues ou good first contribution. Nous nous sommes alors mis en tête que puisque nous analysons l'intégration dans un projet donc nous récupérons les premiers commits étiquetés de ce fait il pourrait avoir un lien avec ces derniers et les labels cités précédemment. Il nous était assez facile de récupérer les labels associés à une issue, de ce fait nous avons opté pour étudier les labels des premiers commits étiquetés.

Suite à cela nous avons émis l'hyptohèse suivante : les premiers commits étiquetés sont associés à des tickets ayant pour labels good first issues ou good first contribution

Pour vérifier notre hypothèse nous sommes partis sur le fait de recenser tous les labels des premiers commits etiquetés et en sommant tout, ressortir les 5 - 10 labels les plus utilisés. Si dans ces derniers appraît les labels good first issue ou good first contribution alors notre hypothèse sera vraie. Dans le cas contraire elle nous montrera de quelle manière les contributeurs intègrent les projets.

Nous devions recenser tous les labels associés aux différentes issues que nous avons trouvées sur les trois dernières page de commits étiquettés par contributeur qu'on nous avons analysés. Pour cela, comme pour trouver si un commit était étiquetté ou pas nous avions analysé le message de ce dernier. Il suffisait de récupérer le nombre qui se trouve juste après le hashtag. Une fois cela fait, on réeffectuait une requête sur l'api afin de récupérer dans le corps de la réponse de l'issue les labels associés à cette dernière ( qui se trouve à cet endroit). Et pour terminer pour chacun de ces labels nous l'enregistrons dans un fichier json qui avait pour `nom nom_de_l'organisation-nom_du_projet.json` avec le nombre de fois qu'il apparaît. Et si nous faisions un autre contributeur même projet nous mettions à jour les valeurs en cumulant.

Ensuite pour chaque fichier json nous l'avons parcouru pour sommer tous les labels de tous les projets dans un autre fichier json `resultat_final`. A partir de ce fichier nous avons mis dans l'ordre décroissant les labels, donc nous avions du plus utilisé au moins utilisé. Nous avons pris les 5 - 10 premiers labels.
```diff
+ Nous cherchons à identifier les tickets dont les contributeurs se servent pour entrer dans un projet. 
+  Cela suppose qu'ils sont potentiellement catégorisés et qu'ils peuvent être regroupés par catégorie.
+  Notre intuition à ce stade a été de se servir des ``labels`` pour catégoriser les tickets. 
+  Ainsi, en recherchant manuellement dans certains projets, nous remarquons la présence de certains labels tels que ``good firt issue`` ou `good first contribution` qui traduisent la première vraie contribution du contributeur.
+  Nous avons donc décidé de suivre cette intuition pour définir l'hypothèse suivante :\
+  **Un nouveau contributeur de projet commence par des tickets ayant pour label une chaîne de caractères commençant par good first.**\
```
</div>

## V. Analyse des résultats & Conclusion

```
1. Analyse des résultats & construction d’une conclusion : Une fois votre expérience terminée, vous récupérez vos mesures et vous les analysez pour voir si votre hypothèse tient la route.
```

Sousquestion1

Après avoir analysé un bon nombres de premiers commits sur des projets, nous avons remarqué avec les résultats que nous avons obtenu que notre hypothèse était plus vérifiée.
En effet sur l'ensembles des commits analysés comme vous pouvez le voir sur le digramme suivant (photo du diagramme) la majeur des commits sont étiquetés. La présence de commits non étiquetés peut s'expliquer par le fait que nous avons analysés pour chaque contributeurs 3 pages de commits ce qui correspond au minimum à 60 commits ( à part la dernière page les 2 autres pages ont 30 commits ). En 60 commits il peut arriver que certains n'aient pas besoin d'être associé à un ticket existant. En revanche sur des projets comme `OhmyZsh` il faut souligner que nous avions du readapter notre script car la plupart des contributeurs n'avaient un nombre de commits pouvant aller jusqu'à 3 pages. Mais nous avons remarqué que sur les commits analysés, ils n'étaient pas étiquetés. Nous avons pensé que c'était une erreur de notre part donc nous somme allés vérifier manuellement et effectivement nous rencontrions un certains nombres de commits qui ne référençaient pas de tickets existants. ( je ne sais pas ce qu'on pourrait dire sur ça faudra trouver). Ce n'est pas le premiers projets sur lequel nous somme tombés avec des commits non étiquetés. Tensorflow, Kubernetes, Facebook-React-Native aussi sont dans le même cas mais pour une autre raison. Nous avons remarqué après recherche manuelle aussi qu'en réalité ces projets utilisaient un autre système de gestion de tickets que Github. Cette information a été déduite en regardant les messages de commits comme vous le montre les images suivantes.

Ce qui nous fait conclure que hormis le fait d'utiliser un autre système de gestion de ticket ou l'immaturité de l'organisation ou juste le fait que la communauté soumet son apport avec un message très clair sur ce qu'il a ajouté et celui qui intégrera le code accepetera ou pas, sur la plupart des projets Github, les contributeurs intègrent les projets avec des commits étiquetés.

Sousquestion 2

Comme dans la partie précédente les projets tensorflow, Kubernetes, Facebook-React-Native vu qu'ils utilisent un autre système de gestion de ticket ils ne font pas partie de l'analyse sur les labels que nous avons effectuée.

Nous allons parler en détails de certains projets comme vscode et flutter pour voir dans un projet dans un premier temps si ces derniers tendent à valider notre hypothèse puis après nous analyserons le résultats général sur l'ensemble des projets que nous avons analysés.

Pour des soucis de lisibilité, nous avons mis les graphes des labels les plus utilisés en bar chart horizontal.

### **`Vscode`**

Pour faire un état des lieux, nous avons analysés 744 commits dont 327 sont étiquetés. Nous ne reviendrons pas sur les raisons pour lesquelles il y a des commits non étiquetés. Et sur les 327 issues, 307 d'entre elles étaient labélisées. 
(image du fichier json)

Voici les dix(10) labels utilisés dans le projet : 
image

On peut remarquer très rapidement l'absence de labels good first issue ou good first contribution. On peut voir que les labels `bug` et `verified` sont extrêmement utilisés dans ce projet. On pourrait expliquer cela par la maturité et la complexité croissante du projet où beaucoup de bugs sont détectés et mises dans issues. Croissante car le label `feature-request`est juste derrière les 2 premiers et montre donc qu'il y a un certain nombre de fonctionnalités qui sont et seront intégrées. Ceci est tout à fait compréhensible vu le nombre mise à jour et les ajouts d'extension par des contributeurs. Ce qui pourrait aussi expliquer le fait que le label `verified` soit le plus utilisé car cela veut dire qu'un membre apte à regarder le code qui sera intégré dans le projet principal rempli les conditions et fini par donner son approbation au travers de pull request.


### **Flutter**

Pour faire un état des lieux, nous avons analysés 802 commits dont 721 sont étiquetés. Et sur les 721 issues, 592 d'entre elles étaient labélisées.
(image du fichier json)

Voici les dix(10) labels utilisés dans le projet :
image

Comme le projet vscode, on retrouve de très loin les labels `bug` et `verified` suivi par `feature-request`. Là encore on note l'absence des labels good first issue ou good first contribution. Il rejoint vscode dans le fait que sa complexité est croissante avec l'ajout fréquents de fonctionnalités ou de plugins de la part de contributeurs externes comme internes à l'équipe du projet. Ce qui justifierait ces 3 labels car avec un ajout de fonctionnalités et/ou de plugins il faut que ces ajouts soient validés par les personnes chargées de cela et aussi cela ajoute des bug qui doivent être corrigés. 

L'analyse de ces 2 projets nous mène à croire que notre hypothèse est faussée et que ce sont plutôt des labels tels que `bug` `verified`et `feature-request` qui sont pris par les contributeurs pour intégrer un projet.

Nous allons à prsént passer à l'analyse générale qui prend en compte tous les projets analysés. 

## **Général**

## VI. Outils

```
Précisez votre utilisation des outils ou les développements \(e.g. scripts\) réalisés pour atteindre vos objectifs. Ce chapitre doit viser à \(1\) pouvoir reproduire vos expérimentations, \(2\) partager/expliquer à d'autres l'usage des outils.
```
* Postman
* Github API
* Python

## VI. References

1. [Flutter](https://github.com/flutter/flutter)
2. [Vscode](https://github.com/microsoft/vscode)
3. [Facebook-React-Native](https://github.com/facebook/react-native)
4. [Kubernetes](https://github.com/kubernetes/kubernetes)
5. [Tensorflow](https://github.com/tensorflow/tensorflow)
6. [How to improve contributors onboarding](https://rimel-uca.github.io/chapters/2019/code-quality-in-open-source-projects-xwiki-2019/contents)
7. [Scripts d'exécution des expérimentations](https://github.com/wak-nda/Rimel-TicketsForNewContributors)
