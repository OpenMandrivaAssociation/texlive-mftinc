%global tl_name mftinc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	Pretty-print Metafont source
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mftinc
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The mft program pretty-prints Metafont source code into a TeX file. The
mftinc package facilitates incorporating such files into a LaTeX2e
document. In addition, mftinc provides routines for improved comment
formatting and for typesetting font tables.

