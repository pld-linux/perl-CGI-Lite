%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Lite
Summary:	CGI_Lite perl module
Summary(pl):	Modu³ perla CGI_Lite
Name:		perl-CGI-Lite
Version:	2.0
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-make.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI_Lite perl module to process and decode WWW forms and cookies.

%description -l pl
Modu³ perla CGI_Lite do przetwarzania i dekodowania formularzy WWW i
cookies.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
perl Makefile.PL
%{__make}
find examples -type f | xargs -r perl -pi -e 's|/local/bin/perl\d*|/bin/perl|g'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/CGI/Lite.pm
%{_mandir}/man3/*

%{_examplesdir}/%{name}-%{version}
