%global release_prefix          1000

Name:                           tree-sitter
Version:                        0.20.6
Release:                        %{release_prefix}%{?dist}
Summary:                        An incremental parsing system for programming tools
License:                        MIT
URL:                            https://tree-sitter.github.io

Source0:                        %{name}-%{version}.tar.xz

BuildRequires:                  gcc
BuildRequires:                  make

%description
Tree-sitter is a parser generator tool and an incremental parsing
library. It can build a concrete syntax tree for a source file
and efficiently update the syntax tree as the source file is
edited. Tree-sitter aims to be:

 * General enough to parse any programming language
 * Fast enough to parse on every keystroke in a text editor
 * Robust enough to provide useful results even in the presence
   of syntax errors
 * Dependency-free so that the runtime library (which is written
   in pure C) can be embedded in any application

# -------------------------------------------------------------------------------------------------------------------- #
# Package: libtree-sitter
# -------------------------------------------------------------------------------------------------------------------- #

%package -n lib%{name}
Summary:                        Incremental parsing library for programming tools

%description -n lib%{name}
Tree-sitter is a parser generator tool and an incremental parsing
library. It can build a concrete syntax tree for a source file
and efficiently update the syntax tree as the source file is
edited. This is the package with the dynamically linked C library.

# -------------------------------------------------------------------------------------------------------------------- #
# Package: libtree-sitter-devel
# -------------------------------------------------------------------------------------------------------------------- #

%package -n lib%{name}-devel
Summary:                        Development files for %{name}
Requires:                       lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep
%autosetup -p1


%build
%{set_build_flags}
export PREFIX='%{_prefix}' LIBDIR='%{_libdir}'
%{make_build}


%install
export PREFIX='%{_prefix}' LIBDIR='%{_libdir}' INCLUDEDIR='%{_includedir}'
%{make_install}

find %{buildroot}%{_libdir} -type f \( -name "*.la" -o -name "*.a" \) -delete -print


%files -n lib%{name}
%license LICENSE
%doc README.md
%{_libdir}/libtree-sitter.so.0*


%files -n lib%{name}-devel
%{_includedir}/tree_sitter
%{_libdir}/libtree-sitter.so
%{_libdir}/pkgconfig/tree-sitter.pc


%changelog
* Thu Mar 31 2022 Package Store <pkgstore@mail.ru> - 0.20.6-1000
- UPD: Rebuild by Package Store.
- UPD: File "tree-sitter.spec".

* Mon Mar 28 2022 Package Store <pkgstore@mail.ru> - 0.20.6-100
- NEW: Tree-sitter v0.20.6.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 01 2021 Andreas Schneider <asn@redhat.com> - 0.20.1-1
- Update to version 0.20.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Andreas Schneider <asn@redhat.com> - 0.20.0-2
- Fixed libtree-sitter Require of devel package

* Fri Jul 02 2021 Andreas Schneider <asn@redhat.com> - 0.20.0-1
- Initial package
