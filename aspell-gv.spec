Summary:	Manx Gaelic dictionary for aspell
Summary(pl.UTF-8):	Słownik manx dla aspella
Name:		aspell-gv
Version:	0.50
%define	subv	0
Release:	3
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/gv/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	139b5aa1f5ea85fb7a4be0338039e959
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manx Gaelic dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik manx (lista słów) dla aspella.

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
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
