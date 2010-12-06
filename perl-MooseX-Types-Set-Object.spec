%define upstream_name    MooseX-Types-Set-Object
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Set::Object type with coercions and stuff
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(Set::Object)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::use::ok)
BuildRequires: perl(Test::Fatal)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides Moose type constraints (see the
Moose::Util::TypeConstraints manpage, the MooseX::Types manpage).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)

%{_mandir}/man3/*
%perl_vendorlib/*


