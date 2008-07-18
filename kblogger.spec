%define betaver alpha2

Name:		kblogger
Version:	1.0
Release:	%mkrel -c %betaver 1
License:	GPLv2+
Url:	        http://kblogger.pwsp.net/
Group:		Graphical desktop/KDE
Source0:	http://kblogger.pwsp.net/files/%name-%version-%betaver.tar.bz2
Summary:        Blogging application
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  kdelibs4-devel
BuildRequires:  kdepimlibs4-devel
BuildRequires:  kdebase4-devel
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

%post
%{update_desktop_database}
%update_icon_cache crystalsvg

%postun
%{clean_desktop_database}
%clean_icon_cache crystalsvg

%files
%defattr(-,root,root)
%{_kde_bindir}/kblogger
%{_kde_datadir}/applications/kde4/kblogger.desktop
%{_kde_appsdir}/kblogger/kbloggerui.rc
%{_kde_appsdir}/kblogger/pics/kbloggerWelcome.jpg
%{_kde_datadir}/config.kcfg/kblogger.kcfg
%{_kde_iconsdir}/crystalsvg/*/*/*.png

#------------------------------------------------

%prep
%setup -q -n %name

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}

%clean
rm -rf %buildroot
