#/bin/sh
#Actual date Folder =  create timestamp dir or text file  with optional name linux/windows - https://github.com/safrm/af
#author:  Miroslav Safr miroslav.safr@gmail.com
BINDIR=/usr/local/bin/

sudo mkdir -p -m 0755 $BINDIR
sudo install -m 0777 -v ./af  $BINDIR
sudo install -m 0777 -v ./ax  $BINDIR
