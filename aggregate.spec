Summary:	Aggregate list of prefixes
Name:		aggregate
Version:	1.6
Release:	%mkrel 1
License:	BSD-like
Group:		Networking/Other
Source0:	ftp://ftp.isc.org/isc/aggregate/%{name}-%{version}.tar.gz
Url:		http://freshmeat.net/projects/aggregate

%description
Aggregate takes a list of prefixes in conventional format on stdin,
and performs two optimizations to reduce the length of the prefix
list. It removes any supplied prefixes which are superfluous because
they are already included in another supplied prefix (e.g.,
203.97.2.0/24 would be removed if 203.97.0.0/17 was also supplied),
and identifies adjacent prefixes that can be combined under a single,
shorter-length prefix (e.g., 203.97.2.0/24 and 203.97.3.0/24 can be
combined into the single prefix 203.97.2.0/23).

%prep
%setup -q

#fix rights
chmod 644 LICE*

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

install -d %{buildroot}{%{_bindir},%{_mandir}/man1}

install -Dpm755 aggregate aggregate-ios %{buildroot}%{_bindir}
install -Dpm644 aggregate.1 aggregate-ios.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICEN* HISTORY
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Wed Jun 15 2011 Jani Välimaa <wally@mandriva.org> 1.6-1mdv2011.0
+ Revision: 685433
- import aggregate

