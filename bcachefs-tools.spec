#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v20
# autospec commit: 4d029647d79e
#
Name     : bcachefs-tools
Version  : 1.13.0
Release  : 5
URL      : https://evilpiepirate.org/bcachefs-tools/bcachefs-tools-vendored-1.13.0.tar.zst
Source0  : https://evilpiepirate.org/bcachefs-tools/bcachefs-tools-vendored-1.13.0.tar.zst
Summary  : Userspace tools for bcachefs
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause CC0-1.0 GPL-2.0 HPND ICU LGPL-2.1 MIT Unicode-DFS-2016 Unlicense
Requires: bcachefs-tools-bin = %{version}-%{release}
Requires: bcachefs-tools-config = %{version}-%{release}
Requires: bcachefs-tools-data = %{version}-%{release}
Requires: bcachefs-tools-libexec = %{version}-%{release}
Requires: bcachefs-tools-license = %{version}-%{release}
Requires: bcachefs-tools-man = %{version}-%{release}
Requires: bcachefs-tools-services = %{version}-%{release}
BuildRequires : libaio-dev
BuildRequires : llvm-dev
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(libkeyutils)
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(libsodium)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(liburcu)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(zlib)
BuildRequires : rustc
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The bcachefs tool, which has a number of subcommands for formatting and managing bcachefs filesystems. Run bcachefs --help for full list of commands.

%package bin
Summary: bin components for the bcachefs-tools package.
Group: Binaries
Requires: bcachefs-tools-data = %{version}-%{release}
Requires: bcachefs-tools-libexec = %{version}-%{release}
Requires: bcachefs-tools-config = %{version}-%{release}
Requires: bcachefs-tools-license = %{version}-%{release}
Requires: bcachefs-tools-services = %{version}-%{release}

%description bin
bin components for the bcachefs-tools package.


%package config
Summary: config components for the bcachefs-tools package.
Group: Default

%description config
config components for the bcachefs-tools package.


%package data
Summary: data components for the bcachefs-tools package.
Group: Data

%description data
data components for the bcachefs-tools package.


%package libexec
Summary: libexec components for the bcachefs-tools package.
Group: Default
Requires: bcachefs-tools-config = %{version}-%{release}
Requires: bcachefs-tools-license = %{version}-%{release}

%description libexec
libexec components for the bcachefs-tools package.


%package license
Summary: license components for the bcachefs-tools package.
Group: Default

%description license
license components for the bcachefs-tools package.


%package man
Summary: man components for the bcachefs-tools package.
Group: Default

%description man
man components for the bcachefs-tools package.


%package services
Summary: services components for the bcachefs-tools package.
Group: Systemd services
Requires: systemd

%description services
services components for the bcachefs-tools package.


%prep
%setup -q -n bcachefs-tools-1.13.0
cd %{_builddir}/bcachefs-tools-1.13.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728602474
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
## make_prepend content
export CFLAGS="${CFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
export CXXFLAGS="${CXXFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
## make_prepend end
make  %{?_smp_mflags}  PREFIX=/usr


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728602474
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bcachefs-tools
cp %{_builddir}/bcachefs-tools-%{version}/COPYING %{buildroot}/usr/share/package-licenses/bcachefs-tools/b47456e2c1f38c40346ff00db976a2badf36b5e3 || :
cp %{_builddir}/bcachefs-tools-%{version}/ccan/array_size/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/bcachefs-tools-%{version}/ccan/build_assert/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/bcachefs-tools-%{version}/ccan/compiler/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/bcachefs-tools-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/bcachefs-tools/005231b4c5545f919f40352621666a5c9c846314 || :
cp %{_builddir}/bcachefs-tools-%{version}/raid/COPYING %{buildroot}/usr/share/package-licenses/bcachefs-tools/075d599585584bb0e4b526f5c40cb6b17e0da35a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/aho-corasick/COPYING %{buildroot}/usr/share/package-licenses/bcachefs-tools/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/aho-corasick/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/aho-corasick/UNLICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anstream/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anstream/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/4dbe8833d0189c691b308c3dd40fab84ef2e9630 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anstyle-parse/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anstyle-parse/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/64a8c11fd0f3068e743bfc681bcbef4f50a6b779 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anstyle-query/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anstyle-query/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/4dbe8833d0189c691b308c3dd40fab84ef2e9630 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anstyle-wincon/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anstyle-wincon/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/33dbd2d99ad231460bbb01812a52c85e577bd9ba || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anstyle/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anstyle/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/f911b0506e6ba6a56b4edac717b461799f380ef0 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anyhow/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/anyhow/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/bindgen/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/8690c5c1d27c8829def121744e5bcd86f48788ef || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/bitfield/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/bitfield/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/5c76111988cd0d808a2278b5e0114099896bb032 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/bitflags-1.3.2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/bitflags-1.3.2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/bitflags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/bitflags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/cc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/cc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/cexpr/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/cexpr/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/cd821ffa80099abbc31c22fe770022f3349e0918 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/cfg-if/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/cfg-if/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/clang-sys/LICENSE.txt %{buildroot}/usr/share/package-licenses/bcachefs-tools/47b573e3824cd5e02a1a3ae99e2735b49e0256e4 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/clap/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/clap/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/4dbe8833d0189c691b308c3dd40fab84ef2e9630 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/clap_builder/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/clap_builder/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/8fe88f09d35c6054e0a780a793833c16fb888168 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/clap_complete/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/clap_complete/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/8fe88f09d35c6054e0a780a793833c16fb888168 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/clap_derive/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/clap_derive/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/8fe88f09d35c6054e0a780a793833c16fb888168 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/clap_lex/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/clap_lex/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/8fe88f09d35c6054e0a780a793833c16fb888168 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/colorchoice/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/colorchoice/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/4dbe8833d0189c691b308c3dd40fab84ef2e9630 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/either/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/either/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/3a86cfdfa553511b381388859c9e94ce9e1f916b || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/env_logger/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/env_logger/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/4dbe8833d0189c691b308c3dd40fab84ef2e9630 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/errno-0.2.8/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/errno-0.2.8/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/7a842f34e127456338641b14c7a00ec246d89fb6 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/errno-dragonfly/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/73724f22eb580e208c5af2e3d089be349209e847 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/errno/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/errno/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/7a842f34e127456338641b14c7a00ec246d89fb6 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/glob/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/glob/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/heck/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/heck/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/60c3522081bf15d7ac1d4c5a63de425ef253e87a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/home/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/1d47c63586fe3be7f228cff1ab0c029b53741875 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/home/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/is_terminal_polyfill/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/is_terminal_polyfill/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/4dbe8833d0189c691b308c3dd40fab84ef2e9630 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/itertools/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/itertools/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/3a86cfdfa553511b381388859c9e94ce9e1f916b || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/lazy_static/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/lazy_static/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/2bf5cac862d5a0480b5d5bcd3a1852d68bfeee84 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/lazycell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/lazycell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/bce2ed71de8bb33db2d29a5fcadd7407824e9248 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/36d69bcb88153a640740000efe933b009420ce7e || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/libloading/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/4ad37fc99fecc5cda018043361f5b12e350e4052 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/libudev-sys/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/cc17a68a18e4a5992a1f67a57c49855b9cfd444c || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/linux-raw-sys/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/linux-raw-sys/LICENSE-Apache-2.0_WITH_LLVM-exception %{buildroot}/usr/share/package-licenses/bcachefs-tools/f137043e018f2024e0414a9153ea728c203ae8e5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/linux-raw-sys/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/log/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/log/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/memchr/COPYING %{buildroot}/usr/share/package-licenses/bcachefs-tools/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/memchr/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/memchr/UNLICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/minimal-lexical/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/minimal-lexical/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/minimal-lexical/LICENSE.md %{buildroot}/usr/share/package-licenses/bcachefs-tools/cd3fe820606ed34ac2591caf068c7cabd3ab3509 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/nom/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/27ea6989d4f34b7b944eb884410a31ae20d11686 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/once_cell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/once_cell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/owo-colors/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/d678d723983cdba8c0182749676fe0ac87e74173 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/paste/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/paste/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/pkg-config/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/pkg-config/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/prettyplease/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/prettyplease/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/regex-automata/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/regex-automata/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/regex-syntax/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/regex-syntax/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/regex-syntax/src/unicode_tables/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/bcachefs-tools/68d12a03b339648117165b9c021b93f26974d6f6 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/regex/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/regex/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/rustc-hash/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/rustc-hash/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/rustix/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/rustix/LICENSE-Apache-2.0_WITH_LLVM-exception %{buildroot}/usr/share/package-licenses/bcachefs-tools/f137043e018f2024e0414a9153ea728c203ae8e5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/rustix/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/rustversion/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/rustversion/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/shlex/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/a97a2888bca904918b3b9ec008fde1d6e9905a6d || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/shlex/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/64e8197cb5ae680fcf996cc0ac8760e9f1e2e3a6 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/strsim/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/f5feee4154156527645a9b18ef29da23fc859ca9 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/strum/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/967573fc64a706430e19b4942fe728870c8182f8 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/strum_macros/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/967573fc64a706430e19b4942fe728870c8182f8 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/terminal_size/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/terminal_size/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/e08d1736c80198e1adec92ff27482e7abbc42d86 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/udev/LICENSE %{buildroot}/usr/share/package-licenses/bcachefs-tools/cc17a68a18e4a5992a1f67a57c49855b9cfd444c || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/unicode-ident/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/unicode-ident/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/unicode-ident/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/bcachefs-tools/583a5eebcf6119730bd96922e8a0faecf7faf720 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/utf8parse/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/utf8parse/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/93074692b8a28bef1743c44a9e5b97b1401c0d09 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/uuid/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/uuid/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/459ceba57b368122a3cb1fd48edea59d1363cad7 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/which/LICENSE.txt %{buildroot}/usr/share/package-licenses/bcachefs-tools/a8ced9a6c206a0e47fac6c6d0d0ce839e85b2eb7 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/winapi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/winapi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/2243f7a86daaa727d34d92e987a741036f288464 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows-sys-0.52.0/license-apache-2.0 %{buildroot}/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows-sys-0.52.0/license-mit %{buildroot}/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows-sys/license-apache-2.0 %{buildroot}/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows-sys/license-mit %{buildroot}/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows-targets/license-apache-2.0 %{buildroot}/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows-targets/license-mit %{buildroot}/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_aarch64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_aarch64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_aarch64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_aarch64_msvc/license-mit %{buildroot}/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_i686_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_i686_gnu/license-mit %{buildroot}/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_i686_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_i686_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_i686_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_i686_msvc/license-mit %{buildroot}/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_x86_64_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_x86_64_gnu/license-mit %{buildroot}/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_x86_64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_x86_64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_x86_64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/windows_x86_64_msvc/license-mit %{buildroot}/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/zeroize/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/zeroize/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/f24fdeaeee4c59532e32b7c6517d34c8927526fe || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/zeroize_derive/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/bcachefs-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/bcachefs-tools-%{version}/vendor/zeroize_derive/LICENSE-MIT %{buildroot}/usr/share/package-licenses/bcachefs-tools/5b17ee15d39ce2dbccc9fd9d4175552e14073e38 || :
export GOAMD64=v2
GOAMD64=v2
%make_install PREFIX=/usr
## install_append content
# Generate the shell completions
mkdir -p %{buildroot}/usr/share/bash-completion/completions
mkdir -p %{buildroot}/usr/share/zsh/site-functions
%{buildroot}/usr/bin/bcachefs completions bash > %{buildroot}/usr/share/bash-completion/completions/bcachefs
%{buildroot}/usr/bin/bcachefs completions zsh  > %{buildroot}/usr/share/zsh/site-functions/_bcachefs
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bcachefs
/usr/bin/fsck.bcachefs
/usr/bin/fsck.fuse.bcachefs
/usr/bin/mkfs.bcachefs
/usr/bin/mkfs.fuse.bcachefs
/usr/bin/mount.bcachefs
/usr/bin/mount.fuse.bcachefs

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/64-bcachefs.rules

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/bcachefs
/usr/share/initramfs-tools/hooks/bcachefs
/usr/share/initramfs-tools/scripts/local-premount/bcachefs
/usr/share/zsh/site-functions/_bcachefs

%files libexec
%defattr(-,root,root,-)
/usr/libexec/bcachefsck_all
/usr/libexec/bcachefsck_fail

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bcachefs-tools/005231b4c5545f919f40352621666a5c9c846314
/usr/share/package-licenses/bcachefs-tools/075d599585584bb0e4b526f5c40cb6b17e0da35a
/usr/share/package-licenses/bcachefs-tools/1d47c63586fe3be7f228cff1ab0c029b53741875
/usr/share/package-licenses/bcachefs-tools/2243f7a86daaa727d34d92e987a741036f288464
/usr/share/package-licenses/bcachefs-tools/27ea6989d4f34b7b944eb884410a31ae20d11686
/usr/share/package-licenses/bcachefs-tools/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/bcachefs-tools/2bf5cac862d5a0480b5d5bcd3a1852d68bfeee84
/usr/share/package-licenses/bcachefs-tools/33dbd2d99ad231460bbb01812a52c85e577bd9ba
/usr/share/package-licenses/bcachefs-tools/36d69bcb88153a640740000efe933b009420ce7e
/usr/share/package-licenses/bcachefs-tools/3a86cfdfa553511b381388859c9e94ce9e1f916b
/usr/share/package-licenses/bcachefs-tools/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/bcachefs-tools/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
/usr/share/package-licenses/bcachefs-tools/459ceba57b368122a3cb1fd48edea59d1363cad7
/usr/share/package-licenses/bcachefs-tools/47b573e3824cd5e02a1a3ae99e2735b49e0256e4
/usr/share/package-licenses/bcachefs-tools/4ad37fc99fecc5cda018043361f5b12e350e4052
/usr/share/package-licenses/bcachefs-tools/4c8990add9180fc59efa5b0d8faf643c9709501e
/usr/share/package-licenses/bcachefs-tools/4dbe8833d0189c691b308c3dd40fab84ef2e9630
/usr/share/package-licenses/bcachefs-tools/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/bcachefs-tools/583a5eebcf6119730bd96922e8a0faecf7faf720
/usr/share/package-licenses/bcachefs-tools/5b17ee15d39ce2dbccc9fd9d4175552e14073e38
/usr/share/package-licenses/bcachefs-tools/5c76111988cd0d808a2278b5e0114099896bb032
/usr/share/package-licenses/bcachefs-tools/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c
/usr/share/package-licenses/bcachefs-tools/60c3522081bf15d7ac1d4c5a63de425ef253e87a
/usr/share/package-licenses/bcachefs-tools/64a8c11fd0f3068e743bfc681bcbef4f50a6b779
/usr/share/package-licenses/bcachefs-tools/64e8197cb5ae680fcf996cc0ac8760e9f1e2e3a6
/usr/share/package-licenses/bcachefs-tools/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/bcachefs-tools/689ec0681815ecc32bee639c68e7740add7bd301
/usr/share/package-licenses/bcachefs-tools/68d12a03b339648117165b9c021b93f26974d6f6
/usr/share/package-licenses/bcachefs-tools/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a
/usr/share/package-licenses/bcachefs-tools/73724f22eb580e208c5af2e3d089be349209e847
/usr/share/package-licenses/bcachefs-tools/7a842f34e127456338641b14c7a00ec246d89fb6
/usr/share/package-licenses/bcachefs-tools/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/bcachefs-tools/8690c5c1d27c8829def121744e5bcd86f48788ef
/usr/share/package-licenses/bcachefs-tools/8fe88f09d35c6054e0a780a793833c16fb888168
/usr/share/package-licenses/bcachefs-tools/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/bcachefs-tools/93074692b8a28bef1743c44a9e5b97b1401c0d09
/usr/share/package-licenses/bcachefs-tools/967573fc64a706430e19b4942fe728870c8182f8
/usr/share/package-licenses/bcachefs-tools/9f3c36d2b7d381d9cf382a00166f3fbd06783636
/usr/share/package-licenses/bcachefs-tools/a3b3a65335e78bde163f84d599fa899776552994
/usr/share/package-licenses/bcachefs-tools/a8ced9a6c206a0e47fac6c6d0d0ce839e85b2eb7
/usr/share/package-licenses/bcachefs-tools/a97a2888bca904918b3b9ec008fde1d6e9905a6d
/usr/share/package-licenses/bcachefs-tools/b47456e2c1f38c40346ff00db976a2badf36b5e3
/usr/share/package-licenses/bcachefs-tools/bce2ed71de8bb33db2d29a5fcadd7407824e9248
/usr/share/package-licenses/bcachefs-tools/cc17a68a18e4a5992a1f67a57c49855b9cfd444c
/usr/share/package-licenses/bcachefs-tools/cd3fe820606ed34ac2591caf068c7cabd3ab3509
/usr/share/package-licenses/bcachefs-tools/cd821ffa80099abbc31c22fe770022f3349e0918
/usr/share/package-licenses/bcachefs-tools/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/bcachefs-tools/d678d723983cdba8c0182749676fe0ac87e74173
/usr/share/package-licenses/bcachefs-tools/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
/usr/share/package-licenses/bcachefs-tools/e08d1736c80198e1adec92ff27482e7abbc42d86
/usr/share/package-licenses/bcachefs-tools/f137043e018f2024e0414a9153ea728c203ae8e5
/usr/share/package-licenses/bcachefs-tools/f24fdeaeee4c59532e32b7c6517d34c8927526fe
/usr/share/package-licenses/bcachefs-tools/f5feee4154156527645a9b18ef29da23fc859ca9
/usr/share/package-licenses/bcachefs-tools/f911b0506e6ba6a56b4edac717b461799f380ef0
/usr/share/package-licenses/bcachefs-tools/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/bcachefs.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/bcachefsck@.service
/usr/lib/systemd/system/bcachefsck_all.service
/usr/lib/systemd/system/bcachefsck_all.timer
/usr/lib/systemd/system/bcachefsck_all_fail.service
/usr/lib/systemd/system/bcachefsck_fail@.service
/usr/lib/systemd/system/system-bcachefsck.slice
