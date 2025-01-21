#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime-Format-DateParse
Version  : 0.05
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/J/JH/JHOBLITT/DateTime-Format-DateParse-0.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JH/JHOBLITT/DateTime-Format-DateParse-0.05.tar.gz
Summary  : 'Parses Date::Parse compatible formats'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-DateTime-Format-DateParse-license = %{version}-%{release}
Requires: perl-DateTime-Format-DateParse-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Class::Data::Inheritable)
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Class::Singleton)
BuildRequires : perl(Date::Parse)
BuildRequires : perl(DateTime)
BuildRequires : perl(DateTime::Locale)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(Exception::Class)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Time::Zone)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
NAME
DateTime::Format::DateParse - Parses Date::Parse compatible formats
SYNOPSIS
use DateTime::Format::DateParse;

%package dev
Summary: dev components for the perl-DateTime-Format-DateParse package.
Group: Development
Provides: perl-DateTime-Format-DateParse-devel = %{version}-%{release}
Requires: perl-DateTime-Format-DateParse = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-DateParse package.


%package license
Summary: license components for the perl-DateTime-Format-DateParse package.
Group: Default

%description license
license components for the perl-DateTime-Format-DateParse package.


%package perl
Summary: perl components for the perl-DateTime-Format-DateParse package.
Group: Default
Requires: perl-DateTime-Format-DateParse = %{version}-%{release}

%description perl
perl components for the perl-DateTime-Format-DateParse package.


%prep
%setup -q -n DateTime-Format-DateParse-0.05
cd %{_builddir}/DateTime-Format-DateParse-0.05

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-DateParse
cp %{_builddir}/DateTime-Format-DateParse-0.05/LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-DateParse/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::DateParse.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-Format-DateParse/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
