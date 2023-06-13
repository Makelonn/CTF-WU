# Category - Challenge name

## Challenge description

![Challenge description](./imgs/desc_img .PNG)

## Resolution

On ouvre le lien https://academie.challenges.404ctf.fr/. 

![Page d'accueil](./imgs/chall2_1.PNG)

On voit qu'il y a possibilité de se connecter en haut, ce qui correspond au fait que seuls les académiciens ont le droit de voir le nouveau membre.

On va donc tenter de se connecter. Avec n'importe quel identifiant, on peut se connecter, sauf avec "admin", qui renvoie une erreur de mot de passe.

Avec *Burp Suite*, on va intercepter la requête de connexion, pour avoir plus d'infos. 

TODO : ajouter image

On voit alors que la requête contient un jeton JWT.

    Cookie: access-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlB1eWxwYSIsImV4cCI6MTY4NjY5MzU5Mn0.qIk8W3wVtkTaIR2NxzMTFzQ7mke0SJ5MYev78iVM4H4

On va donc le décoder avec [jwt.io](https://jwt.io/).

![Décodage du JWT](./imgs/chall2_2.PNG)

On voit alors que le JWT contient un nom d'utilisateur. En tentant de simplement changer le nom d'utilisateur dans le JWT, on voit que ça ne fonctionne pas. En effet, le JWT est signé, et donc si on le modifie, la signature ne correspond plus.

On va donc utiliser cet outil : [jwt_tool](https://www.gavinjl.me/edit-jwt-online-alg-none/)

On change le nom d'utilisateur en admin, et on met l'algorithme de signature à "none".

On obtient alors `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjg2NjkzNTkyfQ.` comme cookie.

Avec burp, on modifie la requête de connexion, et on remplace le cookie par celui-ci. On voit qu'on a alors accès à un nouvel onglet "Liste des membres". On y accède, en prenant soin de remettre le bon cookie, et on arrive sur la page suivante :

![Liste des membres](./imgs/chall2_3.PNG)

Le flag est donc `404CTF{JWT_M41_1MP13M3N73_=L35_Pr0813M35}`.