%define version	20060712
%define release	%mkrel 1

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

%description
IPAMona fonts are modified IPA fonts.

Most Japanese web sites and MS Office templates are
designed for MSPGothic, so Mr. Kobayashi changed the width of 
IPAPGothic to fit against MSPGothic.

Also he changed IPAPMincho for MSPMincho,
and added a "0x301c" character (= "〜") to IPAGothic/IPAMincho.


%prep
%setup -q
cp %SOURCE1 .

%install
rm -rf $RPM_BUILD_ROOT

install -d %{buildroot}/%{_datadir}/fonts/ttf/japanese
install -m 644 fonts/*.ttf %{buildroot}/%{_datadir}/fonts/ttf/japanese/

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_datadir}/fonts/ttf/japanese/
fc-cache -f .

# Install modified fonts.dir for Macromedia Flash.
# (It loads old Kochi fonts)
# Don't run mkfontscale or ttmkfdir.
cd %{_datadir}/fonts/ttf/japanese/
cp -f fonts.dir fonts.dir.bak
cp -f fonts.scale fonts.scale.bak

cd %{_datadir}/doc/fonts-ttf-japanese-ipamona-%{version}
cp -f fonts-ttf-japanese-ipamona_fonts.dir %{_datadir}/fonts/ttf/japanese/fonts.dir
cp -f fonts-ttf-japanese-ipamona_fonts.dir %{_datadir}/fonts/ttf/japanese/fonts.scale
/sbin/service xfs restart

%postun
cd %{_datadir}/fonts/ttf/japanese/
fc-cache -f .

# Restore fonts.dir
cd %{_datadir}/fonts/ttf/japanese/
mv -f fonts.dir.bak fonts.dir
mv -f fonts.scale.bak fonts.scale
/sbin/service xfs restart


%files
%defattr(-,root,root)
%doc fonts/COPYING.font.ja fonts/README_ipamona.txt
%doc fonts/doc/*
%doc opfc-ModuleHP-1.1.1.tar.bz2
%doc fonts-ttf-japanese-ipamona_fonts.dir
%{_datadir}/fonts/ttf/japanese/*.ttf


