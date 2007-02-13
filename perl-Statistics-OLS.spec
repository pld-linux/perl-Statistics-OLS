#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Statistics
%define		pnam	OLS
Summary:	Statistics::OLS - perform ordinary least squares and associated statistics
Summary(pl.UTF-8):	Statistics::OLS - metoda najmniejszych kwadratów i inne związane z nią statystyki
Name:		perl-Statistics-OLS
Version:	0.07
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7bd135125aecdbf523c00714e381eeaa
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I wrote Statistics::OLS to perform Ordinary Least Squares (linear
curve fitting) on two dimensional data: y = a + bx. The other simple
statistical module I found on CPAN (Statistics::Descriptive) is
designed for univariate analysis. It accommodates OLS, but somewhat
inflexibly and without rich bivariate statistics. Nevertheless, it
might make sense to fold OLS into that module or a supermodule
someday.

%description -l pl.UTF-8
Moduł Statistics::OLS został napisany, aby przeprowadzać liniowe
dopasowanie zwykłą metodą najmniejszych kwadratów na dwuwymiarowych
danych (y = a + bx). Inny prosty moduł, Statistics::Descriptive,
służy do analizy jednej zmiennej. Używa on zwykłej metody
najmniejszych kwadratów, ale jest mało elastyczny i pozbawiony bogatej
analizy dwóch zmiennych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Statistics/OLS.pm
%{_mandir}/man3/*
