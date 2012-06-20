#.SILENT : mysli_zebrane.dat sync

all: mysli_zebrane.dat sync

mysli_zebrane.dat: mysli_zebrane
	strfile -s mysli_zebrane mysli_zebrane.dat; chmod 644 mysli_zebrane mysli_zebrane.dat

sync: mysli_zebrane.dat 
	
	touch sync
