Name:           clear-containers-image
Version:        9810
Release:        3
License:        Artistic-1.0 BSD-3-Clause BSD-3-Clause-Clear BSD-4-Clause-UC GFDL-1.3 GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0+ MIT MPL-2.0 Public-Domain
Summary:        Clear Containers Image
Url:            https://download.clearlinux.org/
Group:          image
Source0:        https://download.clearlinux.org/releases/9810/clear/clear-9810-containers.img.xz
Source1:        LICENSE

%description
Clear Containers Image

%prep
cd %{_builddir} 
cp %{_sourcedir}/clear-%{version}-containers.img.xz %{_builddir}
xz -d %{_builddir}/clear-%{version}-containers.img.xz

%install
mkdir -p %{buildroot}/usr/share/clear-containers/
install -p clear-%{version}-containers.img %{buildroot}/usr/share/clear-containers/clear-containers.img

%files
/usr/share/clear-containers/clear-containers.img
