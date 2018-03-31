%define	modname	PerlIO-utf8_strict
%define	modver	0.007

Summary:	Perl module for fast and correct UTF-8 I/O
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/PerlIO-utf8_strict-%{modver}.tar.gz
BuildRequires:	perl-devel

%description
Perl module for fast and correct UTF-8 I/O

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/auto/PerlIO
%{perl_vendorarch}/PerlIO/*.pm
%{_mandir}/man3*/*
