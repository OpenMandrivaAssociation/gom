%define api	1.0
%define major	0
%define libname	%mklibname gom %{api} %{major}
%define devname	%mklibname gom %{api} -d
%define girname	%mklibname gom-gir %{api}

%define url_ver	%(echo %{version} | cut -d. -f1,2)

Name:           gom
Version:         0.3.1
Release:        3
Summary:        GObject to SQLite object mapper library
Group:		System/Libraries
License:	LGPLv2+
URL:            https://wiki.gnome.org/Projects/Gom
Source0:        https://download.gnome.org/sources/gom/%{url_ver}/gom-%{version}.tar.xz
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libpng16)

%description
Gom provides an object mapper from GObjects to SQLite. It helps you write
applications that need to store structured data as well as make complex queries
upon that data.

%package -n %{libname}
Summary:	GObject to SQLite object mapper library
Group:		System/Libraries

%description -n %{libname}
Gom provides an object mapper from GObjects to SQLite. It helps you write
applications that need to store structured data as well as make complex queries
upon that data.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:        Development files for %{name}
Group:		Development/Other
Requires:       %{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files for developing applications
that use %{name}.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name '*.la' -delete

%find_lang gom

%files -f gom.lang

%files -n %{libname}
%{_libdir}/libgom-%{api}.so.%{major}
%{_libdir}/libgom-%{api}.so.%{major}.*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gom-%{api}.typelib

%files -n %{devname}
%doc %{_datadir}/gtk-doc
%{_includedir}/gom-%{api}
%{_libdir}/libgom-%{api}.so
%{_libdir}/pkgconfig/gom-%{api}.pc
%{_datadir}/gir-1.0/Gom-%{api}.gir

