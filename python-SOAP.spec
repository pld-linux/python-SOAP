# TODO: how to run tests in %build?
Summary:	A SOAP library for Python
Summary(pl.UTF-8):	Biblioteka SOAP dla Pythona
Name:		python-SOAP
Version:	0.12.22
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://github.com/kiorky/SOAPpy/releases
Source0:	https://github.com/kiorky/SOAPpy/archive/%{version}/SOAPpy-%{version}.tar.gz
# Source0-md5:	c93de2e7827bcbb6841a8a0ca1de5c59
Patch0:		%{name}-urltry.patch
URL:		https://github.com/kiorky/SOAPpy
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web services for Python programmers, both client and servers. This
includes SOAP, WSDL, UDDI, etc.

%description -l pl.UTF-8
Serwisy WWW dla programistów Pythona, zarówno klient i serwery. W tym
SOAP, WSDL, UDDI itp.

%prep
%setup -q -n SOAPpy-%{version}
%patch -P0 -p1
rm -f src/SOAPpy/*.orig

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr bid contrib tests tools validate $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/*/*.py
%{__sed} -i -e '1s,#!/usr/bin/python\s*$,#!%{__python},' $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/tests/testleak.py

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE README.txt TODO old.Changelog docs/*.txt
%dir %{py_sitescriptdir}/SOAPpy
%{py_sitescriptdir}/SOAPpy/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/SOAPpy-%{version}-py2.7.egg-info
%endif
%{_examplesdir}/%{name}-%{version}
