%define version	20060712
%define release	%mkrel 10
%define fontdir %_datadir/fonts/TTF/japanese-ipamona

Name:		fonts-ttf-japanese-ipamona
Summary:	IPAMona fonts for Japanese
Version:	%{version}
Release:	%{release}
Group:		System/Fonts/True type
License:	Distributable
URL:		http://www.geocities.jp/ipa_mona/
Source0:	%{name}-%{version}.tar.bz2
Source1:	fonts-ttf-japanese-ipamona_fonts.dir
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
BuildRequires: fontconfig

%description
IPAMona fonts are modified IPA fonts.

Most Japanese web sites and MS Office templates are
designed for MSPGothic, so Mr. Kobayashi changed the width of 
IPAPGothic to fit against MSPGothic.

Also he changed IPAPMincho for MSPMincho,
and added a "0x301c" character (= "〜") to IPAGothic/IPAMincho.


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d %buildroot/%fontdir
install -m 644 fonts/*.ttf %{buildroot}/%fontdir/
install %SOURCE1 %buildroot/%fontdir/fonts.dir
install %SOURCE1 %buildroot/%fontdir/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%fontdir \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-japanese-ipamona:pri=50

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc fonts/COPYING.font.ja fonts/README_ipamona.txt
%doc fonts/doc/*
%doc opfc-ModuleHP-1.1.1.tar.bz2
%{fontdir}/*
%_sysconfdir/X11/fontpath.d/*
