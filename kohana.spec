# TODO
# - userguide to subpkg?
# - find-lang.sh script to automate i18n
# - each README.md as %doc?
%define		php_min_version 5.2.4
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
BuildRequires:	unzip
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(dom)
Requires:	php(filter)
Requires:	php(gd)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(mysql)
Requires:	php(pcre)
Requires:	php(session)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php(xml)
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
%dir %{_appdir}/system
%{_appdir}/system/base.php
%{_appdir}/system/classes
%{_appdir}/system/config
%{_appdir}/system/messages
%{_appdir}/system/utf8
%{_appdir}/system/views

%dir %{_appdir}/system/i18n
%lang(en) %{_appdir}/system/i18n/en.php
%lang(es) %{_appdir}/system/i18n/es.php
%lang(fr) %{_appdir}/system/i18n/fr.php

%dir %{_appdir}/modules
%{_appdir}/modules/auth
%{_appdir}/modules/cache
%{_appdir}/modules/codebench
%{_appdir}/modules/database
%{_appdir}/modules/image
%{_appdir}/modules/oauth
%{_appdir}/modules/orm
%{_appdir}/modules/pagination
%{_appdir}/modules/unittest

%dir %{_appdir}/modules/userguide
%{_appdir}/modules/userguide/README.md
%{_appdir}/modules/userguide/init.php
%{_appdir}/modules/userguide/classes
%{_appdir}/modules/userguide/config
%{_appdir}/modules/userguide/media
%{_appdir}/modules/userguide/messages
%{_appdir}/modules/userguide/vendor
%{_appdir}/modules/userguide/views
%{_appdir}/modules/userguide/guide/*.md
%dir %{_appdir}/modules/userguide/guide
%lang(de) %{_appdir}/modules/userguide/guide/de-de
%lang(es) %{_appdir}/modules/userguide/guide/es-es
%lang(fr) %{_appdir}/modules/userguide/guide/fr-fr
%lang(he) %{_appdir}/modules/userguide/guide/he-il
%lang(nl) %{_appdir}/modules/userguide/guide/nl
%lang(ru) %{_appdir}/modules/userguide/guide/ru-ru
%lang(zh_CN) %{_appdir}/modules/userguide/guide/zh-cn

%dir %{_appdir}/modules/userguide/i18n
%lang(de) %{_appdir}/modules/userguide/i18n/de.php
%lang(es) %{_appdir}/modules/userguide/i18n/es.php
%lang(fr) %{_appdir}/modules/userguide/i18n/fr.php
%lang(he) %{_appdir}/modules/userguide/i18n/he.php
%lang(nl) %{_appdir}/modules/userguide/i18n/nl.php
%lang(ru) %{_appdir}/modules/userguide/i18n/ru.php
%lang(zh_CN) %{_appdir}/modules/userguide/i18n/zh.php

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
