Summary:	Tool for transport of asynchronous serial devices over UDP/IP
Name:		serialoverip
Version:	1.0
Release:	%mkrel 7
License:	GPL
Group:		Networking/Other
URL:		http://sourceforge.net/projects/serialoverip
Source0:	%{name}-%{version}.tar.bz2
Patch0:		serialoverip-1.0-gcc3x.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Serial Over IP is a tool for the transport of serial interfaces over UDP/IP.
It is useful for connecting distant equipment that run via a serial interfaces
to a local computer. It requires two computers that are running Linux and are
connected via IP. 

%prep

%setup -q 
%patch0 -p0

%build

gcc %{optflags} -o serialoverip serialoverip.c

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 serialoverip %{buildroot}%{_bindir}/

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/serialoverip




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-7mdv2010.0
+ Revision: 433705
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-6mdv2009.0
+ Revision: 260627
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-5mdv2009.0
+ Revision: 252336
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0-3mdv2008.1
+ Revision: 140792
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot


* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdv2007.0
+ Revision: 113792
- Import serialoverip

* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdv2007.1
- use the mkrel macro

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-2mdk
- rebuild

* Tue Nov 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-1mdk
- initial mandrake package

