Summary:	A SOAP library for Python
Name:		python-SOAP
Version:	0.9.7
Release:	1
License:	Python License
Source0:	http://prdownloads.sourceforge.net/pywebsvcs/SOAPpy097.tgz
URL:		http://sourceforge.net/projects/pywebsvcs/
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python >= 2.1
BuildRequires:	python-devel >= 2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define python_prefix      %(echo `python -c "import sys; print sys.prefix"`)
%define python_version     %(echo `python -c "import sys; print sys.version[:3]"`)
%define python_libdir      %{python_prefix}/lib/python%{python_version}
%define python_sitedir     %{python_libdir}/site-packages

%description
Web services for Python programmers, both client and servers. 
This includes SOAP, WSDL, UDDI, etc.

%prep
%setup -q -n SOAPpy097

%build
python -c 'import py_compile; py_compile.compile("SOAP.py");'
python -O -c 'import py_compile; py_compile.compile("SOAP.py");'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{python_sitedir}

install SOAP.py? $RPM_BUILD_ROOT%{python_sitedir}

gzip -9nf README CHANGELOG docs/*.txt 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.gz validate tests tools contrib bid *.py
%{python_sitedir}/*.py?
