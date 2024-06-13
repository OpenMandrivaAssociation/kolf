#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		plasma6-kolf
Version:	24.05.1
Release:	%{?git:0.%{git}.}1
Summary:	A golf game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://www.kde.org/applications/games/kolf/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kolf/-/archive/%{gitbranch}/kolf-%{gitbranchd}.tar.bz2#/kolf-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kolf-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(KF6)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)

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

%prep
%autosetup -p1 -n kolf-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build

# We don't need this for now
rm -f %{buildroot}%{_kde_libdir}/libkolfprivate.so

%find_lang %{name} --all-name --with-html
