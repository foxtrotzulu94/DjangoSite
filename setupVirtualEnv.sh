#!/bin/bash
EnvName=DEV-ENV-NIX

if [ ! -d "$EnvName" ]; then
	python3 -m virtualenv $EnvName
	if [ $? -eq 0 ]; then
		echo Virtual Env created
	else
		exit $?
	fi
	
	source ./$EnvName/bin/activate
	python3 -m pip install -r requirements.txt
else
	source ./$EnvName/bin/activate
fi

export DEBUG=True
echo Virtual environment is up and ready to use