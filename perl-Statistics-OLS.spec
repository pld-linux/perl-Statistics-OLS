%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Statistics-OLS perl module
Summary(pl):	Modu� perla Statistics-OLS
Name:		perl-Statistics-OLS
Version:	0.04
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Statistics/Statistics-OLS-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Statistics-OLS perl module. 

%description -l pl
Modu� perla Statistics-OLS.

%prep
%setup -q -n Statistics-OLS-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Statistics/OLS
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Statistics/OLS.pm
%{perl_sitearch}/auto/Statistics/OLS

%{_mandir}/man3/*
