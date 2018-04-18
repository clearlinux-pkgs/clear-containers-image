Name:           clear-containers-image
Version:        20640
Release:        32
License:        Artistic-1.0 BSD-3-Clause BSD-3-Clause-Clear BSD-4-Clause-UC GFDL-1.3 GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0+ MIT MPL-2.0 Public-Domain
Summary:        Clear Containers Image
Url:            https://github.com/clearcontainers/osbuilder
Group:          image
Source0:        https://github.com/clearcontainers/osbuilder/releases/download/cc-20640-agent-6f6e9e/image-cc-20640-agent-6f6e9e-binaries.tar.gz
Source1:        LICENSE

%description
Clear Containers Image

%prep
cd %{_builddir} 
cp %{_sourcedir}/image-cc-%{version}-agent-6f6e9e-binaries.tar.gz %{_builddir}
tar xf %{_builddir}/image-cc-%{version}-agent-6f6e9e-binaries.tar.gz --strip-components=1

%install
ImageDir=%{buildroot}/usr/share/clear-containers

mkdir -p ${ImageDir}
install -p cc-%{version}-agent-6f6e9e.img ${ImageDir}/cc-%{version}-agent-6f6e9e.img
ln -sf cc-%{version}-agent-6f6e9e.img ${ImageDir}/clear-containers.img

%files
/usr/share/clear-containers/clear-containers.img
/usr/share/clear-containers/cc-%{version}-agent-6f6e9e.img
