Name:		texlive-mftinc
Version:	1.0a
Release:	1
Summary:	Pretty-print Metafont source
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mftinc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The mft program pretty-prints Metafont source code into a TeX
file. The mftinc package facilitates incorporating such files
into a LaTeX2e document. In addition, mftinc provides routines
for improved comment formatting and for typesetting font
tables.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
