#
# Conditional build:
%bcond_with	tests		# build without tests

%define pkgname uuidtools
Summary:	UUID generation library for Ruby
Name:		ruby-%{pkgname}
Version:	2.1.5
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/uuidtools-%{version}.gem
# Source0-md5:	13de7689edf1f1628d4a14daa764bf5a
URL:		https://github.com/sporkmonger/uuidtools
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-launchy >= 2.0.0
BuildRequires:	ruby-rake >= 0.7.3
BuildRequires:	ruby-rspec >= 2.9.0
BuildRequires:	ruby-yard >= 0.8.2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UUIDTools was designed to be a simple library for generating any of
the various types of UUIDs (or GUIDs if you prefer to call them that).
It conforms to RFC 4122 whenever possible.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%prep
%setup -q

%build
# write .gemspec
%__gem_helper spec

rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}/%{name}-%{version},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}
cp -a rdoc/* $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/uuidtools.rb
%{ruby_vendorlibdir}/uuidtools
%dir %{ruby_vendorlibdir}/compat
%{ruby_vendorlibdir}/compat/securerandom.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
