%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Lite
Summary:	CGI::Lite - process and decode WWW forms and cookies
Summary(pl):	CGI::Lite - przetwarzanie i dekodowanie forumularzy WWW i cookies
Name:		perl-CGI-Lite
Version:	2.02
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fa91873a24a9c8ac78a204e49a7f367f
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You can use this module to decode form and query information, including
file uploads, as well as cookies in a very simple manner; you need not
concern yourself with the actual details behind the decoding process.

%description -l pl
Modu³ ten s³u¿y modu³u do dekodowania informacji z formularzy i
zapytañ, w³±cznie z uploadem plików, a tak¿e cookies, w bardzo prosty
sposób; nie trzeba siê przejmowaæ detalami samego procesu dekodowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
find examples -type f | xargs -r perl -pi -e 's|/local/bin/perl\d*|/bin/perl|g'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{perl_vendorlib}/CGI/Lite.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
