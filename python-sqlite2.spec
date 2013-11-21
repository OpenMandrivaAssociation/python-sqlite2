%define realname pysqlite

Summary:	Python bindings for sqlite3
Name:		python-sqlite2
Version:	2.6.3
Release:	1
License:	zlib
Group:		Development/Python
Url:		http://pysqlite.org
Source0:	http://oss.itsystementwicklung.de/trac/pysqlite/%{realname}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(sqlite3)

%description
This packages allows you to use sqlite3 with python.
sqliite is a simple database engine.

%prep
%setup -qn %{realname}-%{version}

%build

%install
python ./setup.py install --root=%{buildroot}
mv %{buildroot}%{_prefix}/pysqlite2-doc/ installed-docs

%check
cd %{buildroot}%{py_platsitedir}
python -c "from pysqlite2 import test; test.test()"

%files
%doc installed-docs/*
%{py_platsitedir}/*

