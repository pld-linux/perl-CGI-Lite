%include	/usr/lib/rpm/macros.perl
Summary:	CGI_Lite perl module
Summary(pl):	Modu³ perla CGI_Lite
Name:		perl-CGI-Lite
Version:	1.9
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/authors/id/B/BE/BENL//CGI_Lite-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-make.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI_Lite perl module to process and decode WWW forms and cookies.

%description -l pl
Modu³ perla CGI_Lite do przetwarzania i dekodowania formularzy WWW i
cookies.

%prep
%setup -q -n CGI_Lite-%{version}
%patch0 -p1
%patch1 -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CGI_Lite
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO}.gz

%{perl_sitelib}/CGI_Lite.pm
%{perl_sitearch}/auto/CGI_Lite

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}-%{version}
