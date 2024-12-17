#!/bin/bash

if [ ! -d "./backup" ]; then
    echo 'creation du dossier en cours...'
    mkdir backup
    
    echo 'dossier creer'
fi

echo 'copie des fichier texte dans le dossier backup...'

cp *.txt backup/

echo 'souvegare terminee.'