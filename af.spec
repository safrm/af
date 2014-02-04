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
Autoreq: on
Autoreqprov: on

%description
Actual date Folder =  create timestamp dir with optional name on linux/windows by 3 keyboard hits


%prep
%setup -c -n ./%{name}-%{version}

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/usr/bin
install -m 755 ./af %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/af && rm -f %{buildroot}/usr/bin/af.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/af && rm -f %{buildroot}/usr/bin/af.bkp
install -m 755 ./ax %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/ax && rm -f %{buildroot}/usr/bin/ax.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/ax && rm -f %{buildroot}/usr/bin/ax.bkp

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



