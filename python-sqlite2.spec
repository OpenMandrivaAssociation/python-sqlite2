%define realname pysqlite

Name:		python-sqlite2
Version: 2.3.5
Release: %mkrel 1
License:	GPL
Group:		Development/Python
Summary:	Python bindings for sqlite3
Source0:    http://initd.org/pub/software/pysqlite/releases/2.3/%version/%{realname}-%{version}.tar.bz2
Url:		http://pysqlite.org
BuildRequires: python-devel sqlite3-devel 

%description
This packages allows you to use sqlite3 with python.
sqliite is a simple database engine.

%prep
%setup -q -n %{realname}-%version
rm -f doc/rest/.*swp
find doc -name CVS -type d | xargs rm -Rf 
#gw don't know why this is missing
cat >> setup.cfg << EOF
[build_ext]
libraries=sqlite3
EOF

%build


%install
rm -rf $RPM_BUILD_ROOT installed-docs
python ./setup.py install --root=%buildroot
mv %buildroot%_prefix/pysqlite2-doc/ installed-docs

%check
cd %buildroot%py_platsitedir
python -c "from pysqlite2 import test; test.test()"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc installed-docs/*
%py_platsitedir/*


