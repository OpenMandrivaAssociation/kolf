%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		kolf
Version:	17.11.90
Release:	1
Epoch:		1
Summary:	A golf game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kolf/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:  cmake cmake(ECM) ninja
%define libkolfprivate %mklibname kolfprivate 4
Obsoletes:	%{libkolfprivate}

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

%files -f %{name}.lang
%{_bindir}/kolf
%{_datadir}/applications/org.kde.kolf.desktop
%{_datadir}/metainfo/org.kde.kolf.appdata.xml
%{_datadir}/kolf
%{_datadir}/icons/hicolor/*/apps/kolf.*
%{_datadir}/kxmlgui5/kolf
# There's no need for a libpackage for a "private library"...
%{_libdir}/libkolfprivate.so.*

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

# We don't need this for now
rm -f %{buildroot}%{_kde_libdir}/libkolfprivate.so

%find_lang %{name} --all-name --with-html
