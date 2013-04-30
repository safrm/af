%define buildroot %{_topdir}/%{name}-%{version}-root
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
BuildRoot: %{buildroot}

%description
Actual date Folder =  create timestamp dir with optional name on linux/windows by 3 keyboard hits


%prep
%setup -c -n ./%{name}-%{version}
# >> setup
# << setup

%build
# >> build post
# << build post

%install
rm -fr $RPM_BUILD_ROOT
# >> install pre
export INSTALL_ROOT=$RPM_BUILD_ROOT
# << install pre 
mkdir -p %{buildroot}/usr/bin
install -m 755 ./af %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/af && rm -f %{buildroot}/usr/bin/af.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/af && rm -f %{buildroot}/usr/bin/af.bkp
install -m 755 ./ax %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}/usr/bin/ax && rm -f %{buildroot}/usr/bin/ax.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}/usr/bin/ax && rm -f %{buildroot}/usr/bin/ax.bkp
# >> install post
# << install post





%files
%defattr(-,root,root,-)
# >> files
%{_bindir}/af
%{_bindir}/ax
# << files


