%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		ktp-call-ui
Summary:	ktp-call-ui
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e733163a2cb826e350db4f8c9d36cde3
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-ktp-common-internals-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.7.0
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-gstreamer-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-qt5-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ktp-call-ui is interacting with telepathy and farstream.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktp-dialout-ui
%attr(755,root,root) %{_libexecdir}/ktp-call-ui
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.CallUi.service
%{_datadir}/ktp-call-ui
%{_datadir}/kxmlgui5/ktp-call-ui
%{_datadir}/telepathy/clients/KTp.CallUi.client
