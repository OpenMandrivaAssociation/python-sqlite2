%define realname pysqlite

Name:		python-sqlite2
Version:	2.6.3
Release:	1
License:	zlib
Group:		Development/Python
Summary:	Python bindings for sqlite3
Source0:	http://oss.itsystementwicklung.de/trac/pysqlite/%{realname}-%{version}.tar.gz
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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.5-4mdv2011.0
+ Revision: 668037
- mass rebuild

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 2.5.5-3mdv2011.0
+ Revision: 591996
- Rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.5-2mdv2010.1
+ Revision: 523879
- rebuilt for 2010.1

* Fri May 01 2009 Frederik Himpe <fhimpe@mandriva.org> 2.5.5-1mdv2010.0
+ Revision: 370371
- Update to new version 2.5.5
- Update source URL

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 2.4.1-3mdv2009.1
+ Revision: 319667
- rebuild with python 2.6

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.4.1-2mdv2009.0
+ Revision: 225163
- rebuild

* Wed Feb 06 2008 Frederik Himpe <fhimpe@mandriva.org> 2.4.1-1mdv2008.1
+ Revision: 163142
- New upstream version
- Clean up the SPEC file a bit

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 18 2007 Götz Waschk <waschk@mandriva.org> 2.3.5-1mdv2008.0
+ Revision: 53207
- new version
- add tests
- fix build by adding missing setup.cfg

* Wed Apr 25 2007 Götz Waschk <waschk@mandriva.org> 2.3.3-1mdv2008.0
+ Revision: 18341
- new version


* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 2.2.0-3mdv2007.0
+ Revision: 88226
- rebuild

* Wed Nov 15 2006 Lenny Cartier <lenny@mandriva.com> 2.2.0-2mdv2007.1
+ Revision: 84355
- Import python-sqlite2

* Fri Jul 21 2006 Götz Waschk <waschk@mandriva.org> 2.2.0-1mdv2007.0
- Rebuild

* Fri Apr 07 2006 Götz Waschk <waschk@mandriva.org> 2.2.0-1mdk
- fix build
- drop patch
- fix URL
- New release 2.2.0

* Thu Feb 02 2006 Götz Waschk <waschk@mandriva.org> 2.1.3-1mdk
- New release 2.1.3

* Wed Jan 18 2006 Götz Waschk <waschk@mandriva.org> 2.1.0-2mdk
- fix buildrequires

* Mon Jan 16 2006 Götz Waschk <waschk@mandriva.org> 2.1.0-1mdk
- fix build
- New release 2.1.0

* Tue Oct 25 2005 Götz Waschk <waschk@mandriva.org> 2.0.5-1mdk
- New release 2.0.5

* Tue Sep 13 2005 Götz Waschk <waschk@mandriva.org> 2.0.4-1mdk
- add source URL
- new version

* Wed Jul 27 2005 Michael Scherer <misc@mandriva.org> 2.0.3-3mdk
- %%mkrel

* Tue Jul 12 2005 Götz Waschk <waschk@mandriva.org> 2.0.3-2mdk
- fix buildrequires

* Tue Jul 12 2005 Götz Waschk <waschk@mandriva.org> 2.0.3-1mdk
- initial package

* Fri Jan 21 2005 Michael Scherer <misc@mandrake.org> 1.0.1-1mdk
- New release 1.0.1

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 1.0-2mdk
- Rebuild for new python

* Fri Oct 15 2004 Michael Scherer <misc@mandrake.org> 1.0-1mdk
- New release 1.0

* Wed Aug 18 2004 Michael Scherer <misc@mandrake.org> 0.5.1-1mdk
- New release 0.5.1

* Wed Mar 24 2004 Michael Scherer <mscherer@mandrakesoft.com> 0.5.0-1mdk 
- First Mandrakesoft Package

