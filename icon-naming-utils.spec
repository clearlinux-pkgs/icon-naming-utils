#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : icon-naming-utils
Version  : 0.8.90
Release  : 11
URL      : http://tango.freedesktop.org/releases/icon-naming-utils-0.8.90.tar.bz2
Source0  : http://tango.freedesktop.org/releases/icon-naming-utils-0.8.90.tar.bz2
Summary  : Utilities for mapping legacy GNOME and KDE icon names to the new Icon Naming Specification
Group    : Development/Tools
License  : GPL-2.0
Requires: icon-naming-utils-data = %{version}-%{release}
Requires: icon-naming-utils-libexec = %{version}-%{release}
Requires: icon-naming-utils-license = %{version}-%{release}
BuildRequires : perl(XML::Simple)

%description
icon-naming-utils is a script for maintaining backwards compatibility with
current desktop icon themes, while migrating to the names specified in the
Icon Naming Specification [1].

%package data
Summary: data components for the icon-naming-utils package.
Group: Data

%description data
data components for the icon-naming-utils package.


%package dev
Summary: dev components for the icon-naming-utils package.
Group: Development
Requires: icon-naming-utils-data = %{version}-%{release}
Provides: icon-naming-utils-devel = %{version}-%{release}
Requires: icon-naming-utils = %{version}-%{release}

%description dev
dev components for the icon-naming-utils package.


%package libexec
Summary: libexec components for the icon-naming-utils package.
Group: Default
Requires: icon-naming-utils-license = %{version}-%{release}

%description libexec
libexec components for the icon-naming-utils package.


%package license
Summary: license components for the icon-naming-utils package.
Group: Default

%description license
license components for the icon-naming-utils package.


%prep
%setup -q -n icon-naming-utils-0.8.90
cd %{_builddir}/icon-naming-utils-0.8.90

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604096840
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604096840
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/icon-naming-utils
cp %{_builddir}/icon-naming-utils-0.8.90/COPYING %{buildroot}/usr/share/package-licenses/icon-naming-utils/dfac199a7539a404407098a2541b9482279f690d
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dtds/legacy-icon-mapping.dtd
/usr/share/icon-naming-utils/legacy-icon-mapping.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/icon-naming-utils.pc

%files libexec
%defattr(-,root,root,-)
/usr/libexec/icon-name-mapping

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/icon-naming-utils/dfac199a7539a404407098a2541b9482279f690d
