Name:		texlive-nl-interval
Version:	58328
Release:	2
Summary:	Represent intervals on the number line
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nl-interval
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nl-interval.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nl-interval.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros to simplify the process of
representing intervals on the number line. It depends on
tkz-fct, ifthen, and xparse.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/nl-interval
%doc %{_texmfdistdir}/doc/latex/nl-interval

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
