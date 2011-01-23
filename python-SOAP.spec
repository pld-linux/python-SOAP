Summary:	A SOAP library for Python
Summary(pl.UTF-8):	Biblioteka SOAP dla Pythona
Name:		python-SOAP
Version:	0.12.0
Release:	5
License:	Python
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pywebsvcs/SOAPpy-%{version}.tar.gz
# Source0-md5:	d0d29f9b6fb27bfadc69b64a36321e20
Patch0:		%{name}-urltry.patch
Patch1:		%{name}-future.patch
URL:		http://sourceforge.net/projects/pywebsvcs/
%pyrequires_eq	python
BuildRequires:	python-PyXML
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-fpconst
BuildRequires:	rpm-pythonprov
Requires:	python-fpconst
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
%patch0 -p1
%patch1 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/*.txt validate tests tools contrib bid
%dir %{py_sitescriptdir}/SOAPpy
%{py_sitescriptdir}/SOAPpy/*.py?
%dir %{py_sitescriptdir}/SOAPpy/wstools
%{py_sitescriptdir}/SOAPpy/wstools/*.py?
