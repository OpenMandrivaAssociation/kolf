%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		kolf
Version:	22.12.1
Release:	1
Epoch:		1
Summary:	A golf game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kolf/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)

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

%prep
%autosetup -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

# We don't need this for now
rm -f %{buildroot}%{_kde_libdir}/libkolfprivate.so

%find_lang %{name} --all-name --with-html
