%global tl_name nl-interval
%global tl_revision 58328

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Represent intervals on the number line
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/nl-interval
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nl-interval.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nl-interval.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros to simplify the process of representing
intervals on the number line. It depends on tkz-fct, ifthen, and xparse.

