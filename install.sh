#/bin/sh
#Actual date Folder =  create timestamp dir or text file  with optional name linux/windows
#web: http://safrm.net/projects/af
#author:  Miroslav Safr <miroslav.safr@gmail.com>
. appver-installer

appver_basic_scripts_test

$MKDIR_755 $BINDIR
$INSTALL_755 ./af $BINDIR
$INSTALL_755 ./aff $BINDIR
$INSTALL_755 ./ax $BINDIR
appver_update_version_and_date $BINDIR/af
appver_update_version_and_date $BINDIR/aff
appver_update_version_and_date $BINDIR/ax


