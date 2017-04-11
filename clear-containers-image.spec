Name:           clear-containers-image
Version:        11630
Release:        11
License:        Artistic-1.0 BSD-3-Clause BSD-3-Clause-Clear BSD-4-Clause-UC GFDL-1.3 GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0+ MIT MPL-2.0 Public-Domain
Summary:        Clear Containers Image
Url:            https://download.clearlinux.org/
Group:          image
Source0:        https://download.clearlinux.org/releases/11630/clear/clear-11630-containers.img.xz
Source1:        LICENSE

%description
Clear Containers Image

%prep
cd %{_builddir} 
cp %{_sourcedir}/clear-%{version}-containers.img.xz %{_builddir}
xz -d %{_builddir}/clear-%{version}-containers.img.xz

%install
ImageDir=%{buildroot}/usr/share/clear-containers

mkdir -p ${ImageDir}
install -p clear-%{version}-containers.img ${ImageDir}/clear-%{version}-containers.img
ln -sf clear-%{version}-containers.img ${ImageDir}/clear-containers.img

%files
/usr/share/clear-containers/clear-containers.img
/usr/share/clear-containers/clear-%{version}-containers.img
