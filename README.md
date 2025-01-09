# Chall_Cryptographie_Moyen

Pour build l'image docker
  docker build -t name_of_image .
Exemple 
  docker build -t cryptographie .
  
Pour lancer l'image
  docker run -d -p <port_local>:<port_container> name_of_image
Exemple
  docker run -d -p 8080:80 cryptographie
