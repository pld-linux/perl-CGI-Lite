%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Lite
Summary:	CGI_Lite perl module
Summary(pl):	Modu³ perla CGI_Lite
Name:		perl-CGI-Lite
Version:	2.001
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}-emergencyrelease.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI_Lite perl module to process and decode WWW forms and cookies.

%description -l pl
Modu³ perla CGI_Lite do przetwarzania i dekodowania formularzy WWW i
cookies.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}-emergencyrelease

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
find examples -type f | xargs -r perl -pi -e 's|/local/bin/perl\d*|/bin/perl|g'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README TODO
%{perl_vendorlib}/CGI/Lite.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
