Summary:	Manx Gaelic dictionary for aspell
Summary(pl):	S³ownik manx dla aspella
Name:		aspell-gv
Version:	0.50
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/gv/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	139b5aa1f5ea85fb7a4be0338039e959
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manx Gaelic dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik manx (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/Crawler.txt
%{_libdir}/aspell/*
%{_datadir}/aspell/*
