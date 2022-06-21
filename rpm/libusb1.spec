%define keepstatic 1

Name:       libusb1
Summary:    A library which allows userspace access to USB devices
Version:    1.0.20
Release:    1
Group:      System/Libraries
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

%package static
Summary:    Static development files for libusb
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
 
%description static
This package contains static libraries to develop applications that use libusb1.

%package devel
Summary:    Development files for libusb
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb1.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure --enable-static 
# Parallel build fails, thus %{?jobs:-j%jobs} not here.
make

%install
rm -rf %{buildroot}
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%files devel
%doc AUTHORS COPYING README NEWS ChangeLog
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libusb-1.0.pc
%dir %{_includedir}/libusb-1.0
%{_includedir}/libusb-1.0/libusb.h
%{_libdir}/*.so
