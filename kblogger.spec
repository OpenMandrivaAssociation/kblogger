%define betaver alpha3

Name:		kblogger
Version:	1.0
Release:	%mkrel -c %betaver 2
License:	GPLv2+
Url:	        http://kblogger.pwsp.net/
Group:		Graphical desktop/KDE
Source0:	http://kblogger.pwsp.net/files/%name-%version-%betaver.tar.bz2
Summary:        Blogging application
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  kdelibs4-devel
BuildRequires:  kdepimlibs4-devel
Requires:       kdebase4-runtime
Obsoletes:      kde4-%name <= %version-%release

%description
KBlogger is a simple to use blogging application for the K Destkop
Environment. It integrates in KDE Kicker for easy and fast blogging.
The Interface is very minimalstic and tries to provide maximal
usability for your enjoymnet. Just push to the blog button and start
writing.
By now KBlogger supports two API's which are the MetaWeblog and the
Google Blogger.

%files
%defattr(-,root,root)
%{_kde_bindir}/kblogger
%{_kde_datadir}/applications/kde4/kblogger.desktop
%{_kde_appsdir}/kblogger/kbloggerui.rc
%{_kde_appsdir}/kblogger/pics/kbloggerWelcome.jpg
%{_kde_datadir}/config.kcfg/kblogger.kcfg
%{_kde_iconsdir}/*/*/*/*

#------------------------------------------------

%prep
%setup -q -n %name

%build
%cmake_kde4 
%make

%install
rm -rf %buildroot
%{makeinstall_std} -C build

%clean
rm -rf %buildroot


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.alpha3.2mdv2011.0
+ Revision: 612525
- the mass rebuild of 2010.1 packages

* Thu Feb 18 2010 Funda Wang <fwang@mandriva.org> 1.0-0.alpha3.1mdv2010.1
+ Revision: 507545
- 1.0 alpha3

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove unneeded macros

* Fri Jul 18 2008 Funda Wang <fwang@mandriva.org> 1.0-0.alpha2.1mdv2009.0
+ Revision: 238366
- New version 1.0 alpha2

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix provides // Obsoletes
    - Rename spec file and fix spec file
    - Use kde4 app by default now

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.8-0.741164.3mdv2008.1
+ Revision: 139285
- Rebuild against new kde4

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.8-0.741164.2mdv2008.1
+ Revision: 117229
- Rebuild for new kdebase

* Sun Nov 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.8-0.741164.1mdv2008.1
+ Revision: 111827
- import kde4-kblogger


* Fri Dec 29 2006 Emmanuel Blindauer <blindauer@mandriva.org> 0.6.2-1mdv2007.0
+ Revision: 102689
- fix automake
- Import kblogger

* Fri Dec 29 2006 Emmanuel Blindauer <blindauer@mandriva.org> 0.6.2-1mdv2007.1
- first package

