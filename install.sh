#/bin/sh
#Actual date Folder =  create timestamp dir or text file  with optional name linux/windows - http://safrm.net/projects/af
#author:  Miroslav Safr miroslav.safr@gmail.com
BINDIR=/usr/local/bin/
MANDIR=/usr/share/man

#root check
USERID=`id -u`
[ $USERID -eq "0" ] || {
    echo "I cannot continue, you should be root or run it with sudo!"
    exit 0
}

#automatic version
if command -v appver 1>/dev/null 2>&1 ; then . appver; else APP_SHORT_VERSION=NA ; APP_FULL_VERSION_TAG=NA ; APP_BUILD_DATE=`date +'%Y%m%d_%H%M'`; fi

#test
for TEST in $(  grep -r -l -h --exclude-dir=test --exclude-dir=.git  "#\!/bin/sh" . )
do
		sh -n $TEST
		if  [ $? != 0 ]; then
			echo "syntax error in $TEST, exiting.." 
			exit 1
		fi
done

#update documentation
jss-docs-update ./doc 


mkdir -p -m 0755 $BINDIR
install -m 0777 -v ./af  $BINDIR
install -m 0777 -v ./ax  $BINDIR

MANPAGES=`find ./doc/manpages -type f`
sudo install -d -m 755 $MANDIR/man1
sudo install -m 644 $MANPAGES $MANDIR/man1

