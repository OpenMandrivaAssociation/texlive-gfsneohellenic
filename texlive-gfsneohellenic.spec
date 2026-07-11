%global tl_name gfsneohellenic
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	A font in the Neo-Hellenic style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfsneohellenic
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsneohellenic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsneohellenic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The NeoHellenic style evolved in academic circles in the 19th and 20th
century; the present font follows a cut commissioned from Monotype in
1927. The present version was provided by the Greek Font Society. The
font supports both Greek and Latin characters, and has been adjusted to
work well with the cmbright fonts for mathematics support. LaTeX support
of the fonts is provided, offering OT1, T1 and LGR encodings.

