%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	OLS
Summary:	Statistics::OLS - perform ordinary least squares and associated statistics, v 0.07.
Name:		perl-Statistics-OLS
Version:	0.07
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I wrote B<Statistics::OLS> to perform Ordinary Least Squares (linear
curve fitting) on two dimensional data: y = a + bx. The other simple
statistical module I found on CPAN (Statistics::Descriptive) is designed
for univariate analysis. It accomodates OLS, but somewhat inflexibly and
without rich bivariate statistics. Nevertheless, it might make sense to
fold OLS into that module or a supermodule someday.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Statistics/OLS.pm
%{_mandir}/man3/*
