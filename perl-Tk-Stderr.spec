#
# Conditional build:
%bcond_with	tests		# perform "make test". requires DISPLAY=:0 being available
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tk
%define	pnam	Stderr
Summary:	Tk::Stderr - capture standard error output, display in separate window
Summary(pl):	Tk::Stderr - przechwytywanie standardowego wyj�cia b��d�w, wy�wietlanie w innym oknie
Name:		perl-Tk-Stderr
Version:	1.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	86f0f85d24d2c1e72e1e5a039b0f0d72
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Tk
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module captures that standard error of a program and redirects it
to a read only text widget, which doesn't appear until necessary. When
it does appear, the user can close it; it'll appear again when there
is more output.

%description -l pl
Ten modu� przechwytuje standardowe wyj�cie b��d�w z programu i
przekierowuje je do widgetu tekstowego tylko do odczytu, kt�ry nie
pojawia si� dop�ki nie jest potrzebny. Kiedy si� pojawi, u�ytkownik
mo�e go zamkn��; pojawi si� znowu, kiedy b�dzie wi�cej wyj�cia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tk/*.pm
%{_mandir}/man3/*