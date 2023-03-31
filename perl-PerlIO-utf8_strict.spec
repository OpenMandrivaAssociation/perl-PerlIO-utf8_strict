%define	modname	PerlIO-utf8_strict
%define	modver	0.009
%ifarch %{x86_64}
# FIXME bug
%global _debugsource_template %{nil}
%endif

Summary:	Perl module for fast and correct UTF-8 I/O
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		http://metacpan.org/pod/PerlIO::utf8_strict
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/PerlIO-utf8_strict-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Exception)

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
