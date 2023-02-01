Projet Bot_discord
 Le but de ce projet est de créer un bot discord pouvant être déployé sur un serveur et permettant de jouer une chasse au trésor sur le net. Le joueur voulant essayer la chasse pourra lancer le jeu via une commande. Une série d’énigmes lui sera ensuite posée. Chaque énigme lui demandera de chercher sur le web la réponse (soyez créatif). Il pourra à tout moment demander un indice pour l’aider dans sa recherche. Chaque question rapportera des points. S’il demande un indice, il marquera cependant moins de points. A la fin du quizz, un message lui donnant son nombre de points total sera affiché.
 Lien du fichier bot pour commencer : https://colab.research.google.com/drive/1-AMejin61rWc7O1iPEoE_lDlKWqKw13J?usp=sharing
 Fonctionnalités du projet
 Le bot doit pouvoir :
	Être lancé via une commande à tout moment:
	 $ make pour lancer le programme
	 /start pour lancer le quizz
	Pouvoir poser une série de questions à l’utilisateur (au moins 5): ok !
	Récupérer ses réponses et lui donner des points si la réponse est bonne : ok !
	Afficher un indice sur l’énigme courante si l’utilisateur le demande :
	 /astuce pour obtenir un indice
	Afficher son score total lorsque toutes les énigmes ont été réalisées : ok !
	Faire une commande pour afficher son score actuel:
	 /score pour afficher le score
	Faire une commande pour relancer le quizz depuis le début
	 /reset pour relancer le quizz (equivalent de start)
	 Modalités de rendu
	 Le projet est à m’envoyer le « voir la date en cours » à l’adresse suivante :
	 janinloic@gmail.com
	 et non sur mon discord ou via linkedin, facebook, whatsapp, instagram, par courrier ou pigeon voyageur. Si vous me l’envoyez par mail il est possible que les fichiers soient bloqués par votre boite mail, dans ce cas faites-moi un fichier compressé de vos documents.
	 Si vos documents sont hébergé sur un drive ou un cloud donnez moi les droits avant de me l’envoyer !
	 PAS DE WETRANSFERT s’il vous plait.
	 Notation
	 Le projet est à faire par équipe de 4 maximum et 2 minimum. Il sera noté sur 20 points, 14 points sur les commandes demandés ( si il en manque une ou deux vous n’aurez pas 0) et 6 points sur des fonctionnalités supplémentaires non spécifiées. Vous avez carte blanche pour trouver des idées qui permettraient d’améliorer ce jeu (dans les limites du respectable), vous pouvez par exemple essayer de rajouter un timer, des images, du son, des réponses à choix multiples, etc … Les points seront attribués en fonction de la complexité et du nombres de fonctionnalités rajoutées.
	Installation :
	 make install
	Lancement du programme :
	 make run
