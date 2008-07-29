Summary:	Tool for transport of asynchronous serial devices over UDP/IP
Name:		serialoverip
Version:	1.0
Release:	%mkrel 5
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


