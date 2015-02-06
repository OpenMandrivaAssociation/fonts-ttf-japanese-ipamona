%define version	20060712
%define release	11
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


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 20060712-10mdv2011.0
+ Revision: 675572
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 20060712-9mdv2011.0
+ Revision: 610732
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 20060712-8mdv2010.1
+ Revision: 494145
- fc-cache is now called by an rpm filetrigger

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 20060712-7mdv2010.0
+ Revision: 428847
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 20060712-6mdv2009.0
+ Revision: 245260
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 20060712-5mdv2009.0
+ Revision: 239584
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20060712-3mdv2008.1
+ Revision: 125134
- kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Funda Wang <fwang@mandriva.org> 20060712-3mdv2008.0
+ Revision: 68093
- Adapt to new fonts policy

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 20060712-2mdv2008.0
+ Revision: 67832
- rebuild


* Mon Jul 24 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20060712-1mdv2007.0
- new release

* Sat Feb 18 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20060210-3mdk
- fix post and postun

* Tue Feb 14 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20060210-2mdk
- add modified fonts.dir (source1) to show Flash with IPA fonts

* Sat Feb 11 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20060210-1mdk
- first spec for Mandriva Linux

