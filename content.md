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

## Authors

Nous sommes quatre étudiants en dernière année d'ingénierie informatique à Polytech Nice-Sophia, spécialisés en architecture logicielle :

* Paul-Marie DJEKINNOU <paul-marie.djekinnou@etu.univ-cotedazur.fr>
* Paul KOFFI <merveille.koffi@etu.univ-cotedazur.fr>
* Florian AINADOU <florian.ainadou@etu.univ-cotedazur.fr>
* Djotiham NABAGOU <djotiham.nabagou@etu.univ-cotedazur.fr>

## I. Research context /Project

Préciser ici votre contexte.
Nous sommes partis de la question générale qui interroge sur la meilleure compréhension d'un système que

Pourquoi c'est intéressant.


![Figure 1: Logo UCA, exemple, vous pouvez l'enlever](../assets/model/UCAlogoQlarge.png){:height="25px" }


## II. Observations/General question

1. Commencez par formuler une question sur quelque chose que vous observez ou constatez ou encore une idée émergente. Attention pour répondre à cette question vous devrez être capable de quantifier vos réponses.
2. Préciser bien pourquoi cette question est intéressante de votre point de vue et éventuellement en quoi la question est plus générale que le contexte de votre projet \(ex: Choisir une libraire de code est un problème récurrent qui se pose très différemment cependant en fonction des objectifs\)

Cette première étape nécessite beaucoup de réflexion pour se définir la bonne question afin de poser les bonnes bases pour la suit.

## III. information gathering

Préciser vos zones de recherches en fonction de votre projet,

1. les articles ou documents utiles à votre projet
2. les outils
 
## IV. Hypothesis & Experiences

### Outils utilisés

Pour effectuer nos expériementation et répondre à nos questions, nous avons décidé d'utiliser l'api **`github`** qui nous permet de récupérer des diverses informations comme les commits d'un projets, les issues d'un dépôt ou encore les différents contributeurs, etc... Des scripts `Python` pour effectuer des requêtes vers l'api avec la librairie `Requests` et `Pyplot`  pour la mise en forme des différents résultats obtenus par nos scripts.

### Démarches

Pour répondre à la question suivante: quels sont les labels des premiers commits étiquettés ?

Pour répondre à cette problématique nous avons dans un premiers temps recherché dans l'api github l'url nous permettant de récupérer les commits sur un projet particulier d'un contributeur. Suite à cela on se retrouvait dans une première impasse qui était le fait que l'api github ne renvoie que 30 éléments par requête et donc il fallait se déplacer dans les pages. Nous avons manuellement cherché la dernière page puis partir de cette dernière pour analyser les trois dernières pages de commits. Mais cette méthode ne convenait pas et nous sommes mis à chercher une information nous permettant de récupérer la dernière page de n'importe quelle requête. Une fois trouvé nous nous sommes replongés dans l'avancée de notre expérience. Cette fois-ci, nous parcourions tous les commits des 3 dernières pages et pour chacun d'entre eux nous effectuons une analyse sur le message du commit ( qui se trouve dans à cet endroit dans le corps de la réponse d'un commit). L'analyse sur le message du commit était de récupérer le numéro de l'issue associée puis après de reéffectuer une requête à l'api afin de récupérer dans le corps de la réponse de l'issue les labels associés à cette dernière ( qui se trouve à cet endroit). Et pour terminer pour chacun de ces labels nous l'enregistrons dans un fichier json qui avait pour `nom nom_de_l'organisation-nom_du_projet.json` avec le nombre de fois qu'il apparaît. Et si nous faisions un autre contributeur même projet nous mettions à jour les valeurs en cumulant.

Question 2 ...les plus fréquents ? C'est - à - dire sur l'ensembles des premiers commits des contributeurs quels sont les labales qui ressortent le plus ?

1. Il s'agit ici d'énoncer sous forme d' hypothèses ce que vous allez chercher à démontrer. Vous devez définir vos hypothèses de façon à pouvoir les _mesurer facilement._ Bien sûr, votre hypothèse devrait être construite de manière à v_ous aider à répondre à votre question initiale_.Explicitez ces différents points.
2. Test de l’hypothèse par l’expérimentation. 1. Vos tests d’expérimentations permettent de vérifier si vos hypothèses sont vraies ou fausses. 2. Il est possible que vous deviez répéter vos expérimentations pour vous assurer que les premiers résultats ne sont pas seulement un accident.
3. Explicitez bien les outils utilisés et comment.
4. Justifiez vos choix

## V. Result Analysis and Conclusion

1. Analyse des résultats & construction d’une conclusion : Une fois votre expérience terminée, vous récupérez vos mesures et vous les analysez pour voir si votre hypothèse tient la route. 

## VI. Tools \(facultatif\)

Précisez votre utilisation des outils ou les développements \(e.g. scripts\) réalisés pour atteindre vos objectifs. Ce chapitre doit viser à \(1\) pouvoir reproduire vos expérimentations, \(2\) partager/expliquer à d'autres l'usage des outils.

## VI. References

1. ref1
1. ref2
