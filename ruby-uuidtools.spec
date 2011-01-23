Summary:	UUID generation library for Ruby
Name:		ruby-uuidtools
Version:	1.0.3
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/uuidtools-%{version}.gem
# Source0-md5:	d362d1286ce3b805f0e8286474120bd3
URL:		http://sporkmonger.com/projects/uuidtools/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.3.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UUIDTools was designed to be a simple library for generating any of the various types of UUIDs (or GUIDs if you prefer to call them that). It conforms to RFC 4122 whenever possible.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/uuidtools*
