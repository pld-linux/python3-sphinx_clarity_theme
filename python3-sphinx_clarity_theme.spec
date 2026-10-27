Summary:	Clarity Theme for Sphinx
Name:		python3-sphinx_clarity_theme
Version:	2.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-clarity-theme/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-clarity-theme/sphinx_clarity_theme-%{version}.tar.gz
# Source0-md5:	50be96d8eeaf2f56274efcc7bb194c81
URL:		https://pypi.org/project/sphinx-clarity-theme/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A clean and professional documentation theme for Sphinx. Modern design
with light/dark mode, responsive layout, and beautiful typography.

%prep
%setup -q -n sphinx_clarity_theme-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/sphinx_clarity_theme
%{py3_sitescriptdir}/sphinx_clarity_theme-%{version}.dist-info
