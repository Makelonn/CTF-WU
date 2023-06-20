# Forensics - Pêche aux livres

## Challenge description

![Challenge description](./imgs/peche_aux_livres.png)

## Resolution

On ouvre le fichier `peche_au_livre.pcapng` avec *Wireshark*.

On regarde un peu les paquets, et on voit des paquets *HTTP* qui contiennent des images.

On extrait ces images avec *File > Export Objects > HTTP*.

On sauvegarde ces images, et l'image "hegel-sensei-uwu.png" contient le flag.

<img src="./imgs/peche_aux_livres/karlmarx_fancam.jpg" alt="img 1" width="200"> <img src="./imgs/peche_aux_livres/karl_marx.jpg" alt="img 2" width="200"> <img src="./imgs/peche_aux_livres/Hegel-sensei-uwu.png" alt="img 3" width="200">

Flag : `404CTF{345Y_W1r35h4rK}`