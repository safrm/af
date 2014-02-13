%define APP_BUILD_DATE %(date +'%%Y%%m%%d_%%H%%M')

Name:       af
Summary:    Actual date Folder 
Version:    1.0.0
Release:    1
Group:      Development/Tools
License:    LGPL v2.1
BuildArch:  noarch
URL:        http://safrm.net/projects/af/
Vendor:     Miroslav Safr <miroslav.safr@gmail.com>
Source0:    %{name}-%{version}.tar.bz2
Autoreq:    on
Autoreqprov: on
#BuildRequires:  xsltproc
BuildRequires:  libxslt
#BuildRequires:  docbook-xsl
BuildRequires: docbook-xsl-stylesheets
BuildRequires:  appver >= 1.1.1

%description
Actual date Folder =  create timestamp dir with optional name on linux/windows by 3 keyboard hits


%prep
%setup -c -n ./%{name}-%{version}

%build
cd doc && ./update_docs.sh %{version} && cd -

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 ./af %{buildroot}%{_bindir}
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}%{_bindir}/af && rm -f %{buildroot}%{_bindir}/af.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}%{_bindir}/af && rm -f %{buildroot}%{_bindir}/af.bkp
install -m 755 ./ax %{buildroot}%{_bindir}
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}%{_bindir}/ax && rm -f %{buildroot}%{_bindir}/ax.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}%{_bindir}/ax && rm -f %{buildroot}%{_bindir}/ax.bkp

#documentation
MANPAGES=`find ./doc/manpages -type f`
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 $MANPAGES %{buildroot}%{_mandir}/man1
DOCS="./README ./LICENSE.LGPL"
install -d -m 755 %{buildroot}%{_datadir}/doc/af
install -m 644 $DOCS %{buildroot}%{_datadir}/doc//af


%check
for TEST in $(  grep -r -l -h "#\!/bin/bash" . )
do
	sh -n $TEST
	if  [ $? != 0 ]; then
		echo "syntax error in $TEST, exiting.." 
		exit 1
	fi
done 

%files
%defattr(-,root,root,-)
%{_bindir}/af
%{_bindir}/ax

#man pages
%{_mandir}/man1/af.1*
%{_mandir}/man1/ax.1*

#other docs
%{_datadir}/doc/af/README
%{_datadir}/doc/af/LICENSE.LGPL


