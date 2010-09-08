%define		php_min_version 5.2.4
%include	/usr/lib/rpm/macros.php
Summary:	Swift PHP framework
Summary(pl.UTF-8):	Szybki framework dla PHP
Name:		kohana
Version:	3.0.7.1
Release:	0.1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://dev.kohanaframework.org/attachments/download/1596/%{name}-%{version}.zip
# Source0-md5:	d317c1fdcbe649d2862a3f602b1f6cd6
URL:		http://www.kohanaframework.org/
BuildRequires:	rpm-php-pearprov >= 4.3
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-ctype
Requires:	php-date
Requires:	php-dom
Requires:	php-filter
Requires:	php-gd
Requires:	php-hash
Requires:	php-json
Requires:	php-mbstring
Requires:	php-mysql
Requires:	php-pcre
Requires:	php-session
Requires:	php-simplexml
Requires:	php-spl
Requires:	php-xml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{php_data_dir}/kohana

# want no pear deps
%define		_noautopear	pear

# exclude optional php dependencies
%define		_noautophp	%{nil}

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
Kohana is a PHP5 framework that uses the Model View Controller
architectural pattern. It aims to be secure, lightweight and easy to
use.

%description -l pl.UTF-8
Kohana to framework dla PHP5 używający wzorzec Modelu, Widoku i
Kontrolera. W zamierzeniu ma być bezpieczny, lekki i prosty w użyciu.

%package examples
Summary:	Example empty application
Summary(pl.UTF-8):	Przykładowa pusta aplikacja
Group:		Development/Languages/PHP
Requires:	kohana

%description examples
This package contains basic application structure.

%description examples -l pl.UTF-8
Pakiet zawiera podstawową strukturę aplikacji.

%prep
%setup -qc
mv kohana/* .; rmdir kohana

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a system modules $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -a application index.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_appdir}
%{_appdir}/system
%{_appdir}/modules

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
