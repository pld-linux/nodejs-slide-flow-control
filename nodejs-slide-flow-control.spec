%define		git_hash 53a6c97
%define		pkg	slide-flow-control
Summary:	A flow control library that fits in a slideshow
Name:		nodejs-%{pkg}
Version:	1.1.3
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/slide-flow-control
# download from https://github.com/isaacs/slide-flow-control/tarball/%{version}
Source0:	isaacs-%{pkg}-%{version}-0-g%{git_hash}.tar.gz
# Source0-md5:	03d66fb16e99c26b472d96b48572bf47
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides simple, easy callbacks for node.js.

%prep
%setup -q -n isaacs-%{pkg}-e6ca2aa

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}
cp -p lib/*.js $RPM_BUILD_ROOT%{nodejs_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md nodejs-controlling-flow.pdf
%{nodejs_libdir}/*.js
