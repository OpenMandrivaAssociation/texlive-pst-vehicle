Name:		texlive-pst-vehicle
Version:	61438
Release:	2
Summary:	A PSTricks package for rolling vehicles on graphs of mathematical functions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pst-vehicle
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vehicle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vehicle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package permits to represent vehicles rolling without
slipping on mathematical curves. Different types of vehicles
are proposed, the shape of the curve is to be defined by its
equation "y=f(x)" in algebraic notation.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-vehicle
%{_texmfdistdir}/tex/generic/pst-vehicle
%doc %{_texmfdistdir}/doc/generic/pst-vehicle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
