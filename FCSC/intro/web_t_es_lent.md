# Forensics - La Gazette Windows

## Challenge description

![Challenge description](./imgs/desc_web_tes_lent.PNG)

## Résolution

On a le lien vers le site [T'es lent](https://tes-lent.france-cybersecurity-challenge.fr/)

On arrive sur la page avec une offre de stage :

![Page d'accueil](./imgs/tes_lent_1.PNG)

En utilisant inspecter l'élement, on trouve un bloc de code commenté :

![Code commenté](./imgs/tes_lent_2.PNG)

On voit que ce code fait référenc à une page `/stage-generateur-de-nom-de-challenges.html`. On tente d'accèder à une page "mode brouillon, cette pas prête" :

![Page brouillon](./imgs/tes_lent_3.PNG)

On trouve un autre bloc de code commenté :

![Code commenté](./imgs/tes_lent_4.PNG)

On y accède et paf, un suberbe flag !

![Flag](./imgs/tes_lent_flag.PNG)