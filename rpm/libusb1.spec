Name:       libusb1
Summary:    A library which allows userspace access to USB devices
Version:    1.0.24
Release:    1
License:    LGPLv2+
URL:        https://github.com/sailfishos/libusb1
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: pkgconfig(udev)
BuildRequires: libtool

%description
This package provides a way for applications to access USB devices. Note that
this library is not compatible with the original libusb-0.1 series.

%package devel
Summary:    Development files for libusb
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb1.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%autogen
%configure
# Parallel build fails, thus %{?jobs:-j%jobs} not here.
make

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc AUTHORS README NEWS ChangeLog
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libusb-1.0.pc
%dir %{_includedir}/libusb-1.0
%{_includedir}/libusb-1.0/libusb.h
%{_libdir}/*.so
