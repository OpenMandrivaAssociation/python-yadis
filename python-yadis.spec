%define module yadis
Name: 		python-%module
Version: 	1.1.0
Release:	2
License: 	GPL
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-%{version}-build
BuildRequires: 	python-devel
Requires: 	python-urljr
Url: 		https://www.openidenabled.com/yadis/libraries/python
Source: 	http://www.openidenabled.com/resources/downloads/python-openid/python-yadis-%{version}.tar.gz
Summary: Python library for yadis service discovery
Buildarch:	noarch

%description
Yadis is a protocol for discovering services applicable to a URL.
This package provides a client implementation of the Yadis protocol.

%prep
%setup -q -n python-%{module}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*



%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 1.1.0-1mdv2011.0
+ Revision: 683276
- import python-yadis


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 1.1.0
- first release for Mandriva 

