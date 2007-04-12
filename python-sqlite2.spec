%define realname pysqlite

Name:		python-sqlite2
Version: 2.2.0
Release: %mkrel 3
License:	GPL
Group:		Development/Python
Summary:	Python bindings for sqlite
Source0:    http://initd.org/pub/software/pysqlite/releases/2.2/%version/%{realname}-%{version}.tar.bz2
Url:		http://pysqlite.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel sqlite3-devel 

%description
This packages allows you to use sqlite with python.
sqliite is a simple database engine.

%prep
%setup -q -n %{realname}-%version
rm -f doc/rest/.*swp
for i in examples doc; do
	find $i -name CVS -type d | xargs rm -Rf 
done;

%build


%install
rm -rf $RPM_BUILD_ROOT installed-docs
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%_prefix
mv %buildroot%_prefix/pysqlite2-doc/ installed-docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc installed-docs/*
%py_platsitedir/*


