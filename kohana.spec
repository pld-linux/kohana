%define		rel 1690
%define		kohanadir	%{_datadir}/php/kohana

%include	/usr/lib/rpm/macros.php
Summary:	Swift PHP framework
Summary(pl.UTF-8):	Szybki framework dla PHP
Name:		kohana
Version:	2.1
Release:	0.%{rel}.1
License:	Kohana License (http://kohanaphp.com/license.html)
Group:		Development/Languages/PHP
Source0:	%{name}-trunk-r%{rel}.zip
# Source0-md5:	4a491482ed5ed6e345fb80aeba3a0f50
URL:		http://kohanaphp.com
BuildRequires:	rpm-php-pearprov >= 4.3
Requires:	php-common >= 5.1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package examples
Summary:	Example empty application
Summary(pl.UTF-8):	Przykładowa pusta aplikacja
Group:		Development/Languages/PHP

%description examples

%description examples -l pl.UTF-8

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

sed -i -e "s,$kohana_system = 'system',$kohana_system = '/usr/share/php/kohana/system'," trunk/index.php

install -d $RPM_BUILD_ROOT%{kohanadir}
cp -r trunk/{system,modules} $RPM_BUILD_ROOT%{kohanadir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -r trunk/application trunk/index.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{kohanadir}
%dir %{kohanadir}/system
%dir %{kohanadir}/modules
%{kohanadir}/system/*
%{kohanadir}/modules/*

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}
%dir %{_examplesdir}/%{name}/application
%{_examplesdir}/%{name}/application/*
%{_examplesdir}/%{name}/index.php
