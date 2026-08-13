%global tl_name gfsneohellenic
%global tl_revision 79618
%global tl_version 1.02

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A font in the Neo-Hellenic style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfsneohellenic
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsneohellenic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsneohellenic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The NeoHellenic style evolved in academic circles in the 19th and 20th
century; the present font follows a cut commissioned from Monotype in
1927. The present version was provided by the Greek Font Society. The
font supports both Greek and Latin characters, and has been adjusted to
work well with the cmbright fonts for mathematics support. LaTeX support
of the fonts is provided, offering OT1, T1 and LGR encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from gfsneohellenic:
Map gfsneohellenic.map
TL_DROPIN_EOF
