%undefine _debugsource_packages
%define	modname	PerlIO-utf8_strict

Summary:	Perl module for fast and correct UTF-8 I/O
Name:		perl-%{modname}
Version:	0.010
Release:	4
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		https://metacpan.org/pod/PerlIO::utf8_strict
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/PerlIO-utf8_strict-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Exception)
Obsoletes:	%{name} = 0.9.0-1

%description
Perl module for fast and correct UTF-8 I/O

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorarch}/auto/PerlIO
%{perl_vendorarch}/PerlIO/*.pm
%{_mandir}/man3*/*
