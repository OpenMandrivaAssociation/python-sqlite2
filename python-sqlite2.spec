%define realname pysqlite

Name:		python-sqlite2
Version:	2.4.1
Release:	%mkrel 1
License:	zlib
Group:		Development/Python
Summary:	Python bindings for sqlite3
Source0:	http://initd.org/pub/software/pysqlite/releases/2.3/%version/%{realname}-%{version}.tar.bz2
Url:		http://pysqlite.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel sqlite3-devel 

%description
This packages allows you to use sqlite3 with python.
sqliite is a simple database engine.

%prep
%setup -q -n %{realname}-%{version}

%build

%install
python ./setup.py install --root=%buildroot
mv %{buildroot}%{_prefix}/pysqlite2-doc/ installed-docs

%check
cd %{buildroot}%{py_platsitedir}
python -c "from pysqlite2 import test; test.test()"

%files
%defattr(-,root,root)
%doc installed-docs/*
%py_platsitedir/*
