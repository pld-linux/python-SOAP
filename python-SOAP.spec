%include	/usr/lib/rpm/macros.python
Summary:	A SOAP library for Python
Summary(pl):	Biblioteka SOAP dla Pythona
Name:		python-SOAP
Version:	0.9.7
Release:	7
License:	Python
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pywebsvcs/SOAPpy097.tgz
# Source0-md5:	1bbd42ce353a5e1ce6bc6ad181719bf6
URL:		http://sourceforge.net/projects/pywebsvcs/
%pyrequires_eq	python
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web services for Python programmers, both client and servers. This
includes SOAP, WSDL, UDDI, etc.

%description -l pl
Serwisy WWW dla programistów Pythona, zarówno klient i serwery. W tym
SOAP, WSDL, UDDI itp.

%prep
%setup -q -n SOAPpy097

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

install SOAP.py $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG docs/*.txt validate tests tools contrib bid *.py
%{py_sitedir}/*.py?
