#/bin/sh
#Actual date Folder =  create timestamp dir or text file  with optional name linux/windows - http://safrm.net/projects/af
#author:  Miroslav Safr miroslav.safr@gmail.com
BINDIR=/usr/local/bin/
MANDIR=/usr/share/man

sudo mkdir -p -m 0755 $BINDIR
sudo install -m 0777 -v ./af  $BINDIR
sudo install -m 0777 -v ./ax  $BINDIR

MANPAGES=`find ./doc/manpages -type f`
sudo install -d -m 755 $MANDIR/man1
sudo install -m 644 $MANPAGES $MANDIR/man1

