%include	/usr/lib/rpm/macros.perl
Summary:	Statistics-OLS perl module
Summary(pl):	Modu³ perla Statistics-OLS
Name:		perl-Statistics-OLS
Version:	0.06
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Statistics/Statistics-OLS-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics-OLS perl module.

%description -l pl
Modu³ perla Statistics-OLS.

%prep
%setup -q -n Statistics-OLS-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Statistics/OLS.pm
%{_mandir}/man3/*
