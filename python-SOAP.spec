Summary:	A SOAP library for Python
Name:		python-SOAP
Version:	0.9.7
Release:	1
License:	Python License
Source0:	http://prdownloads.sourceforge.net/pywebsvcs/SOAPpy097.tgz
URL:		http://sourceforge.net/projects/pywebsvcs/
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/J�zyki/Python
Requires:	python >= 2.1
BuildRequires:	python-devel >= 2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%include /usr/lib/rpm/macros.python

%description
Web services for Python programmers, both client and servers. 
This includes SOAP, WSDL, UDDI, etc.

%prep
%setup -q -n SOAPpy097

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

install SOAP.py $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

gzip -9nf README CHANGELOG docs/*.txt 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.gz validate tests tools contrib bid *.py
%{py_sitedir}/*.py?
