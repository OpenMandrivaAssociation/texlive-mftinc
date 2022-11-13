Name:		texlive-mftinc
Version:	15878
Release:	1
Summary:	Pretty-print Metafont source
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mftinc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The mft program pretty-prints Metafont source code into a TeX
file. The mftinc package facilitates incorporating such files
into a LaTeX2e document. In addition, mftinc provides routines
for improved comment formatting and for typesetting font
tables.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mftinc/mftinc.sty
%doc %{_texmfdistdir}/doc/latex/mftinc/README
%doc %{_texmfdistdir}/doc/latex/mftinc/mftinc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mftinc/mftinc.dtx
%doc %{_texmfdistdir}/source/latex/mftinc/mftinc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
