%define upstream_name    MooseX-Types-Set-Object%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Set::Object type with coercions and stuff
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(Set::Object)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(Test::Fatal)
BuildArch:	noarch

%description
This module provides Moose type constraints (see the
Moose::Util::TypeConstraints manpage, the MooseX::Types manpage).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 656946
- rebuild for updated spec-helper

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 612326
- update to new version 0.03

* Fri Jul 30 2010 Shlomi Fish <shlomif@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 563370
- import perl-MooseX-Types-Set-Object


* Fri Feb 05 2010 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

