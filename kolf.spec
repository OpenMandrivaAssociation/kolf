Name:		kolf
Version:	4.10.4
Release:	1
Epoch:		1
Summary:	A golf game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kolf/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
Kolf is a miniature golf game. The game is played from an overhead view, with
a short bar representing the golf club. Kolf features many different types of
objects, such as water hazards, slopes, sand traps, and black holes (warps),
among others.

Features :
- Single and Multi-player (up to ten players) modes
- High scores table
- Dynamic courses
- Third-party courses
- Course editor

%files
%{_kde_bindir}/kolf
%{_kde_applicationsdir}/kolf.desktop
%{_kde_appsdir}/kolf
%{_kde_docdir}/*/*/kolf
%{_kde_iconsdir}/hicolor/*/apps/kolf.png

#------------------------------------------------------------------------------

%define libkolfprivate_private 4
%define libkolfprivate %mklibname kolfprivate %{libkolfprivate_private}

%package -n %{libkolfprivate}
Summary:	Runtime library for Kolf
Group:		System/Libraries

%description -n %{libkolfprivate}
Runtime library for Kolf.

%files -n %{libkolfprivate}
%{_kde_libdir}/libkolfprivate.so.%{libkolfprivate_private}*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# We don't need this for now
rm -f %{buildroot}%{_kde_libdir}/libkolfprivate.so

%changelog
* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

