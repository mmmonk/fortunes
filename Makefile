#.SILENT : mysli_zebrane.dat sync

all: pull mysli_zebrane.dat sync

pull:
	git pull

mysli_zebrane.dat: mysli_zebrane
	strfile -s mysli_zebrane mysli_zebrane.dat; chmod 644 mysli_zebrane mysli_zebrane.dat

sync: mysli_zebrane.dat 
	git commit -a -m "`date`"
	git push
	touch sync
