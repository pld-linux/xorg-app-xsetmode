Summary:	xsetmode application
Summary(pl):	Aplikacja xsetmode
Name:		xorg-app-xsetmode
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xsetmode-%{version}.tar.bz2
# Source0-md5:	a6caff0660e88120570a53804004f174
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xsetmode application.

%description -l pl
Aplikacja xsetmode.

%prep
%setup -q -n xsetmode-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
