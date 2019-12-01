#! /bin/bash

git config --global credential.helper cache;

echo “Git Pull - Atualizando”
git pull
echo “”
echo “”
echo “Git Add * - Adicionando arquivos para commitar”
git add *;
echo “”
echo “”
echo “Digite o Commit: ”
read commit;
git commit -m "$commit";
echo “”
echo “”
echo “Git Pulsh - Subindo para a nuvem”
git push;
echo “”
echo “”
echo “Aperte enter para sair ”
read pause;


