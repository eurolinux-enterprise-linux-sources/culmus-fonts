%define fontname culmus
%define fontconf 65-%{fontname}

%define common_desc \
The culmus-fonts package contains fonts for the display of\
Hebrew from the Culmus project.


Name:           %{fontname}-fonts
Version:        0.130
Release:        3%{?dist}
Summary:        Fonts for Hebrew from Culmus project

Group:          User Interface/X
License:        GPLv2
URL:            http://culmus.sourceforge.net
Source0:        http://downloads.sourceforge.net/culmus/%{fontname}-%{version}.tar.gz
Source1:        %{fontconf}-aharoni-clm.conf
Source2:        %{fontconf}-caladings-clm.conf
Source3:        %{fontconf}-david-clm.conf
Source4:        %{fontconf}-drugulin-clm.conf
Source5:        %{fontconf}-ellinia-clm.conf
Source6:        %{fontconf}-frank-ruehl-clm.conf
Source7:        %{fontconf}-miriam-clm.conf
Source8:        %{fontconf}-miriam-mono-clm.conf
Source9:        %{fontconf}-nachlieli-clm.conf
Source10:        %{fontconf}-hadasim-clm.conf
Source11:        %{fontconf}-keteryg.conf
Source12:        %{fontconf}-simple-clm.conf
Source13:        %{fontconf}-stamashkenaz-clm.conf
Source14:        %{fontconf}-stamsefarad-clm.conf
Source15:        %{fontconf}-shofar.conf
Source16:        http://downloads.sourceforge.net/culmus/culmus-type1-0.121.tar.gz
Obsoletes:      culmus-fonts < 0.102-1

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%description
%common_desc
Meta-package of Culmus fonts which installs various families of culmus project.

%package common
Summary:        Common files of culmus-fonts
Group:          User Interface/X
Requires:       fontpackages-filesystem
Obsoletes:      culmus-fonts < 0.102-1
%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-aharoni-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-aharoni-clm-fonts
%common_desc

%_font_pkg -n aharoni-clm -f %{fontconf}-aharoni-clm.conf AharoniCLM-*.afm AharoniCLM-*.pfa

%package -n %{fontname}-caladings-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-caladings-clm-fonts
%common_desc

%_font_pkg -n caladings-clm -f %{fontconf}-caladings-clm.conf CaladingsCLM.afm CaladingsCLM.pfa

%package -n %{fontname}-david-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-david-clm-fonts
%common_desc

%_font_pkg -n david-clm -f %{fontconf}-david-clm.conf DavidCLM-*.ttf DavidCLM-*.afm DavidCLM-*.pfa

%package -n %{fontname}-drugulin-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-drugulin-clm-fonts
%common_desc

%_font_pkg -n drugulin-clm -f %{fontconf}-drugulin-clm.conf DrugulinCLM-*.afm DrugulinCLM-*.pfa

%package -n %{fontname}-ellinia-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-ellinia-clm-fonts
%common_desc

%_font_pkg -n ellinia-clm -f %{fontconf}-ellinia-clm.conf ElliniaCLM-*.afm ElliniaCLM-*.pfa

%package -n %{fontname}-frank-ruehl-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-frank-ruehl-clm-fonts
%common_desc

%_font_pkg -n frank-ruehl-clm -f %{fontconf}-frank-ruehl-clm.conf FrankRuehlCLM-*.ttf  FrankRuehlCLM-*.afm FrankRuehlCLM-*.pfa


%package -n %{fontname}-hadasim-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-hadasim-clm-fonts
%common_desc

%_font_pkg -n hadasim-clm -f %{fontconf}-hadasim-clm.conf HadasimCLM-*.ttf

%package -n %{fontname}-keteryg-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-keteryg-fonts
%common_desc

%_font_pkg -n keteryg -f %{fontconf}-keteryg.conf KeterYG-*.ttf


%package -n %{fontname}-miriam-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-miriam-clm-fonts
%common_desc

%_font_pkg -n miriam-clm -f %{fontconf}-miriam-clm.conf MiriamCLM-*.ttf MiriamCLM-*.afm MiriamCLM-*.pfa

%package -n %{fontname}-miriam-mono-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-miriam-mono-clm-fonts
%common_desc

%_font_pkg -n miriam-mono-clm -f %{fontconf}-miriam-mono-clm.conf MiriamMonoCLM-*.ttf MiriamMonoCLM-*.afm MiriamMonoCLM-*.pfa

%package -n %{fontname}-nachlieli-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-nachlieli-clm-fonts
%common_desc

%_font_pkg -n nachlieli-clm -f %{fontconf}-nachlieli-clm.conf NachlieliCLM-*.afm NachlieliCLM-*.pfa


%package -n %{fontname}-simple-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-simple-clm-fonts
%common_desc

%_font_pkg -n simple-clm -f %{fontconf}-simple-clm.conf SimpleCLM-*.ttf

%package -n %{fontname}-stamashkenaz-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-stamashkenaz-clm-fonts
%common_desc

%_font_pkg -n stamashkenaz-clm -f %{fontconf}-stamashkenaz-clm.conf StamAshkenazCLM.ttf

%package -n %{fontname}-stamsefarad-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-stamsefarad-clm-fonts
%common_desc

%_font_pkg -n stamsefarad-clm -f %{fontconf}-stamsefarad-clm.conf StamSefaradCLM.ttf


%package -n %{fontname}-yehuda-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-yehuda-clm-fonts
%common_desc

%_font_pkg -n yehuda-clm YehudaCLM-*.afm YehudaCLM-*.pfa

%package -n %{fontname}-shofar-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}
Provides:       culmus-fonts-compat = %{version}-%{release}
Obsoletes:      culmus-fonts-compat < %{version}-%{release}

%description -n %{fontname}-shofar-fonts
%common_desc

%_font_pkg -n shofar -f %{fontconf}-shofar.conf Shofar*.ttf

%prep
%setup -q -n %{fontname}-%{version}
%setup -c -q -a 16
mv %{fontname}-%{version}/* .
mv %{fontname}-type1-0.121/* .

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0644 -p *.afm %{buildroot}%{_fontdir}
install -m 0644 -p *.pfa %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-aharoni-clm.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-caladings-clm.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-david-clm.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-drugulin-clm.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-ellinia-clm.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-frank-ruehl-clm.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-miriam-clm.conf
install -m 0644 -p %{SOURCE8} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-miriam-mono-clm.conf
install -m 0644 -p %{SOURCE9} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nachlieli-clm.conf
install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-hadasim-clm.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-keteryg.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-simple-clm.conf
install -m 0644 -p %{SOURCE13} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-stamashkenaz-clm.conf
install -m 0644 -p %{SOURCE14} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-stamsefarad-clm.conf
install -m 0644 -p %{SOURCE15} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-shofar.conf

for fconf in %{fontconf}-aharoni-clm.conf \
             %{fontconf}-caladings-clm.conf \
             %{fontconf}-david-clm.conf \
             %{fontconf}-drugulin-clm.conf \
             %{fontconf}-ellinia-clm.conf \
             %{fontconf}-frank-ruehl-clm.conf \
             %{fontconf}-miriam-clm.conf \
             %{fontconf}-miriam-mono-clm.conf \
             %{fontconf}-nachlieli-clm.conf \
             %{fontconf}-hadasim-clm.conf \
             %{fontconf}-keteryg.conf \
             %{fontconf}-simple-clm.conf \
             %{fontconf}-stamashkenaz-clm.conf \
             %{fontconf}-stamsefarad-clm.conf \
             %{fontconf}-shofar.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done


%files common
%doc CHANGES GNU-GPL LICENSE LICENSE-BITSTREAM 

%dir %{_fontdir}


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.130-3
- Mass rebuild 2013-12-27

* Wed Jun 19 2013 Pravin Satpute <psatpute@redhat.com> - 0.130-2
- Resolved #975735 :- Typo in fontconfig file

* Tue Mar 20 2013 Pravin Satpute <psatpute@redhat.com> - 0.130-1
- Upstream release 0.130 new family Shofar
- Resolved #923153

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.121-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Pravin Satpute <psatpute@redhat.com> - 0.121-4
- Spec file cleanup #878538

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.121-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Pravin Satpute <psatpute@redhat.com> - 0.121-2
- Resolves bug 837533

* Mon Jan 30 2012 Pravin Satpute <psatpute@redhat.com> - 0.121-1
- Upstream new release 0.121 with Frank Ruehl OT

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.120-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Pravin Satpute <psatpute@redhat.com> - 0.120-1
- Upstream new release.
- Added new families Hadasim CLM, Keter YG, Simple CLM, Stam Ashkenaz CLM, Stam Sefarad CLM

* Fri Sep 03 2010 Pravin Satpute <psatpute@redhat.com> - 0.105-1
- Upstream new release.
- Miriam Mono family is now OpenType and has diacritics support developed by Yoram Gnat.

* Mon Apr 19 2010 Pravin Satpute <psatpute@redhat.com> - 0.104-3
- fixed bug 578018 .conf file

* Fri Feb 19 2010 Pravin Satpute <psatpute@redhat.com> - 0.104-2
- updated .conf file priorities
- fixed bug 565385

* Fri Feb 12 2010 Pravin Satpute <psatpute@redhat.com> - 0.104-1
- new upstream release

* Tue Jan 19 2010 Pravin Satpute <psatpute@redhat.com> - 0.103-5
- fixed compat package bug 484621

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Pravin Satpute <psatpute@redhat.com> - 0.103-3
- added DavidCLM afm and pfa
- bug 509694

* Wed Jul 08 2009 Pravin Satpute <psatpute@redhat.com> - 0.103-1
- upstream new release 0.103

* Tue Apr 14 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-6.fc11
- Rebuild for bug #491957.

* Thu Mar 19 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-5.fc11
- Corrected Obsoletes for compat.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-3.fc11
- Modified -compat.

* Mon Feb 09 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-2.fc11
- Created -compat for subpackage for smooth upgrade.

* Wed Feb 04 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-1.fc11
- Updated version.
- Following new font packaging guidelines.

* Wed Jul 23 2008 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-5.fc10
- Obsoleted dead package fonts-hebrew

* Mon Oct 15 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-4.fc8
- License change

* Thu Oct 11 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-3.fc8
- Updated according to the review

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-2.fc8
- Using common spec template for font packages

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-1.fc8
- Font directory and package name corrected and updated the version

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.100-1.fc8
- Split package from fonts-hebrew to reflect upstream project name
