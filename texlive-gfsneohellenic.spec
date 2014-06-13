# revision 31979
# category Package
# catalog-ctan /fonts/greek/gfs/gfsneohellenic
# catalog-date 2013-10-23 14:10:10 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-gfsneohellenic
Version:	1.0
Release:	8
Summary:	A Greek font in the Neo-Hellenic style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/gfs/gfsneohellenic
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsneohellenic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsneohellenic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The NeoHellenic style evolved in academic circles in the 19th
and 20th century; the present font follows a cut commissioned
from Monotype in 1927. The present version was provided by the
Greek Font Society. The font supports both Greek and Latin
characters, and has been adjusted to work well with the
cmbright fonts for mathematics support. LaTeX support of the
fonts is provided, offering OT1, T1 and LGR encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/gfsneohellenic/GFSNeohellenic-Bold.afm
%{_texmfdistdir}/fonts/afm/public/gfsneohellenic/GFSNeohellenic-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/gfsneohellenic/GFSNeohellenic-Italic.afm
%{_texmfdistdir}/fonts/afm/public/gfsneohellenic/GFSNeohellenic-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenic.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicdenomnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicec.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicecsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicel.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicelsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicmath.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicnumnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenictabnums.enc
%{_texmfdistdir}/fonts/map/dvips/gfsneohellenic/gfsneohellenic.map
%{_texmfdistdir}/fonts/opentype/public/gfsneohellenic/GFSNeohellenic.otf
%{_texmfdistdir}/fonts/opentype/public/gfsneohellenic/GFSNeohellenicBold.otf
%{_texmfdistdir}/fonts/opentype/public/gfsneohellenic/GFSNeohellenicBoldIt.otf
%{_texmfdistdir}/fonts/opentype/public/gfsneohellenic/GFSNeohellenicIt.otf
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gfsneohellenicmath8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gfsneohellenicmath8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicb6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicb6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicbi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicbi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicbo6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicbo6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenici6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenici6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenico6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenico6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicrg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicrg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicsc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicsc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicsco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicsco6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicb9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicb9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbi9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbi9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbo9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbo9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicdenomnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicdenomnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenici8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenici8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenici9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenici9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicnumnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicnumnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenico8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenico8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenico9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenico9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicrg8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicrg8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicrg9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicrg9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsc9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsc9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsco9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsco9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenictabnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenictabnums8r.tfm
%{_texmfdistdir}/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/gfsneohellenic/GFSNeohellenic-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gfsneohellenicmath8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicb6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicbi6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicbo6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenici6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenico6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicrg6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicsc6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicsco6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicb8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicb9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicbi8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicbi9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicbo8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicbo9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicdenomnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenici8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenici9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicnumnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenico8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenico9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicrg8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicrg9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicsc8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicsc9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicsco8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicsco9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenictabnums8a.vf
%{_texmfdistdir}/tex/latex/gfsneohellenic/gfsneohellenic.sty
%{_texmfdistdir}/tex/latex/gfsneohellenic/lgrneohellenic.fd
%{_texmfdistdir}/tex/latex/gfsneohellenic/omlneohellenic.fd
%{_texmfdistdir}/tex/latex/gfsneohellenic/ot1neohellenic.fd
%{_texmfdistdir}/tex/latex/gfsneohellenic/t1neohellenic.fd
%{_texmfdistdir}/tex/latex/gfsneohellenic/uneohellenicnums.fd
%doc %{_texmfdistdir}/doc/fonts/gfsneohellenic/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gfsneohellenic/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gfsneohellenic/README
%doc %{_texmfdistdir}/doc/fonts/gfsneohellenic/README.TEXLIVE
%doc %{_texmfdistdir}/doc/fonts/gfsneohellenic/VERSION

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
