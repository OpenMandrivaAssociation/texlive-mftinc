# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mftinc
# catalog-date 2007-01-11 00:21:49 +0100
# catalog-license lppl
# catalog-version 1.0a
Name:		texlive-mftinc
Version:	1.0a
Release:	10
Summary:	Pretty-print Metafont source
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mftinc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mftinc.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-2
+ Revision: 753939
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-1
+ Revision: 719012
- texlive-mftinc
- texlive-mftinc
- texlive-mftinc
- texlive-mftinc

