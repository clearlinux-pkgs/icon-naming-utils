#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : icon-naming-utils
Version  : 0.8.90
Release  : 6
URL      : http://tango.freedesktop.org/releases/icon-naming-utils-0.8.90.tar.bz2
Source0  : http://tango.freedesktop.org/releases/icon-naming-utils-0.8.90.tar.bz2
Summary  : Utilities for mapping legacy GNOME and KDE icon names to the new Icon Naming Specification
Group    : Development/Tools
License  : GPL-2.0
Requires: icon-naming-utils-bin
Requires: icon-naming-utils-data
BuildRequires : perl(XML::Simple)

%description
icon-naming-utils is a script for maintaining backwards compatibility with
current desktop icon themes, while migrating to the names specified in the
Icon Naming Specification [1].

%package bin
Summary: bin components for the icon-naming-utils package.
Group: Binaries
Requires: icon-naming-utils-data

%description bin
bin components for the icon-naming-utils package.


%package data
Summary: data components for the icon-naming-utils package.
Group: Data

%description data
data components for the icon-naming-utils package.


%package dev
Summary: dev components for the icon-naming-utils package.
Group: Development
Requires: icon-naming-utils-bin
Requires: icon-naming-utils-data

%description dev
dev components for the icon-naming-utils package.


%prep
%setup -q -n icon-naming-utils-0.8.90

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/icon-name-mapping

%files data
%defattr(-,root,root,-)
/usr/share/dtds/legacy-icon-mapping.dtd
/usr/share/icon-naming-utils/legacy-icon-mapping.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/*.pc
