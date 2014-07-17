%define pkgname uuidtools
Summary:	UUID generation library for Ruby
Name:		ruby-%{pkgname}
Version:	1.0.3
Release:	2
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/uuidtools-%{version}.gem
# Source0-md5:	d362d1286ce3b805f0e8286474120bd3
URL:		http://sporkmonger.com/projects/uuidtools/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	setup.rb >= 3.3.1
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
cp %{_datadir}/setup.rb .

%build
%{__ruby} setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

%{__ruby} setup.rb setup

rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}
%{__ruby} setup.rb install \
	--prefix=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -a rdoc/* $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_libdir}/uuidtools.rb
%{ruby_libdir}/uuidtools

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
