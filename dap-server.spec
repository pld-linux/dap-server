# NOTE: for versions >= 4.2.3 see bes.spec
#
# Conditional build:
%bcond_without	tests	# make check
#
Summary:	Basic request handling for OPeNDAP servers
Summary(pl.UTF-8):	Podstawowa obsługa żądań dla serwerów OPeNDAP
Name:		dap-server
Version:	4.1.6
Release:	1
License:	LGPL v2.1+
Group:		Daemons
Source0:	http://www.opendap.org/pub/source/%{name}-%{version}.tar.gz
# Source0-md5:	871bf62d2d7f184dcabc7645ed013158
URL:		http://opendap.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.10
BuildRequires:	bes-devel >= 3.9.0
BuildRequires:	bes-devel < 3.14
%{?with_tests:BuildRequires:	cppunit-devel >= 1.12.0}
BuildRequires:	libdap-devel >= 3.11.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Requires:	bes >= 3.9.0
Requires:	libdap >= 3.11.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains general purpose handlers for use with the new
Hyrax data server. These are the Usage, ASCII and HTML form handlers.
Each takes input from a 'data handler' and returns a HTML or plain
text response - something other than a DAP response object.

%description -l pl.UTF-8
Ten pakiet zawiera kilka procedur obsługi ogólnego przeznaczenia dla
nowego serwera danych Hyrax. Są to procedury obsługi Usage, ASCII oraz
formularzy HTML. Każdy z nich pobiera wejście z procedury obsługi
danych i zwraca odpowiedź w formacie HTML lub czystego tekstu - czegoś
innego, niż obiekt odpowiedzi DAP.

%prep
%setup -q

%build
# rebuild autotools for -as-needed to work
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/bes/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT_* ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/dap-server.conf
%attr(755,root,root) %{_libdir}/bes/libascii_module.so
%attr(755,root,root) %{_libdir}/bes/libusage_module.so
%attr(755,root,root) %{_libdir}/bes/libwww_module.so
%{_datadir}/bes/dap-server_help.*
