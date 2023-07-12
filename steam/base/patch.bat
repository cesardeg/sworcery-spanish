@echo off
ren sworcery.dat sworcery.zip
7za u -pGdHGhd4yuNF sworcery.zip @list.txt
ren sworcery.zip sworcery.dat
del sworcery.dat.cat
rebuild_cat.exe
pause
