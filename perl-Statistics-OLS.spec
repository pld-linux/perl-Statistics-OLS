%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	OLS
Summary:	Statistics::OLS - perform ordinary least squares and associated statistics
Summary(pl):	Statistics::OLS - metoda najmniejszych kwadratów i inne zwi±zane z ni± statystyki
Name:		perl-Statistics-OLS
Version:	0.07
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7bd135125aecdbf523c00714e381eeaa
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Modu³ Statistics::OLS zosta³ napisany, aby przeprowadzaæ liniowe
dopasowanie zwyk³± metod± najmniejszych kwadratów na dwuwymiarowych
danych (y = a + bx). Inny prosty modu³, Statistics::Descriptive,
s³u¿y do analizy jednej zmiennej. U¿ywa on zwyk³ej metody
najmniejszych kwadratów, ale jest ma³o elastyczny i pozbawiony bogatej
analizy dwóch zmiennych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Statistics/OLS.pm
%{_mandir}/man3/*
