%include	/usr/lib/rpm/macros.python
Summary:	A SOAP library for Python
Summary(pl):	Biblioteka SOAP dla Pythona
Name:		python-SOAP
Version:	0.10.3
Release:	0.1
License:	Python
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pywebsvcs/SOAPpy-%{version}.tar.gz
# Source0-md5:	b679a02ea99bb7a6a0652461b341556d
URL:		http://sourceforge.net/projects/pywebsvcs/
%pyrequires_eq	python
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	python-fpconst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web services for Python programmers, both client and servers. This
includes SOAP, WSDL, UDDI, etc.

%description -l pl
Serwisy WWW dla programistów Pythona, zarówno klient i serwery. W tym
SOAP, WSDL, UDDI itp.

%prep
%setup -q -n SOAPpy-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.* docs/*.txt validate tests tools contrib bid
%dir %{py_sitedir}/SOAPpy
%{py_sitedir}/SOAPpy/*.py?
%dir %{py_sitedir}/SOAPpy/wstools
%{py_sitedir}/SOAPpy/wstools/*.py?
