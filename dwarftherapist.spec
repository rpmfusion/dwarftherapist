%undefine __cmake_in_source_build

Name:           dwarftherapist
Version:        41.1.7
Release:        12%{?dist}
Summary:        Management tool designed to run side-by-side with Dwarf Fortress

License:        MIT
URL:            https://github.com/Dwarf-Therapist/Dwarf-Therapist
Source0:        https://github.com/Dwarf-Therapist/Dwarf-Therapist/archive/v%{version}/dwarftherapist-%{version}.tar.gz

# Need cmake.
BuildRequires:  cmake3

# Qt5 dependencies.
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

# Desktop file utils.
BuildRequires:  desktop-file-utils

# dos2unix, for fixing a file.
BuildRequires:  dos2unix

# Required for post step.
Requires(post): /usr/sbin/setcap

# We need Dwarf Fortress for Therapist to be useful! Therefore
# we should only build on x86_64 and i686 as these are the only
# arches DF exists on.
Requires:       dwarffortress
ExclusiveArch:  x86_64 i686

Requires:       hicolor-icon-theme

# Require the noarch data package.
Requires:       dwarftherapist-data = %{version}-%{release}

%description
Management tool designed to run side-by-side with Dwarf Fortress.
Offers several views and interface improvements to Dwarf Fortress.
Some features include:

Persistent custom professions - import and manage any number of custom
professions across all your forts.

Assign multiple dwarves to a custom profession at once to unify active labors.

Manage labors and professions much more easily than in-game using a flexible
UI, allowing quick review of all dwarves at-a-glance.

Display all pending changes before they're written to the game.

Sort labor columns by associated skill level.

Persistent and customizable display; change colors, reposition/hide
information screens.

Group your dwarves by several criteria.

This is a heavily modified version of the original Dwarf Therapist that
is still maintained for new versions of Dwarf Fortress.

%package data

BuildArch:      noarch
Summary:        Architecture independent data files for Dwarf Therapist

%description data

This package contains architecture independent data files for Dwarf Therapist,
a management tool designed to run side-by-side with the video game Dwarf
Fortress. For more information, see the description of the main dwarftherapist
package.

%prep
%setup -qn Dwarf-Therapist-%{version}
dos2unix CHANGELOG.txt

%build
%cmake3
%cmake3_build

%install
%cmake3_install

# Check the desktop file.
desktop-file-validate %{buildroot}/%{_datadir}/applications/dwarftherapist.desktop

# Install the resources?
cp -rp resources/* %{buildroot}%{_datadir}/dwarftherapist/
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p resources/img/*.xpm %{buildroot}%{_datadir}/pixmaps/

# Remove an extra copy of the license.
rm %{buildroot}%{_docdir}/dwarftherapist/LICENSE.txt

# Post install script; set cap permissions.
%post
sudo setcap cap_sys_ptrace=eip %{_bindir}/dwarftherapist

%files
%{_bindir}/dwarftherapist
%{_datadir}/applications/dwarftherapist.desktop
%{_datadir}/pixmaps/dwarftherapist.*
%{_datadir}/icons/hicolor/*/apps/dwarftherapist.png
%doc README.rst CHANGELOG.txt
%license LICENSE.txt

%files data
%{_datadir}/dwarftherapist
%license LICENSE.txt

%changelog
* Mon Feb 02 2026 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 41.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 41.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 41.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 41.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 41.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 41.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 41.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 41.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 41.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 41.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 41.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Ben Rosser <rosser.bjr@gmail.com> - 41.1.7-1
- Update to latest upstream release.

* Mon Apr 20 2020 Ben Rosser <rosser.bjr@gmail.com> - 41.1.6-1
- Update to latest upstream release.

* Fri Feb 28 2020 Ben Rosser <rosser.bjr@gmail.com> - 41.1.4-1
- Updated to latest upstream release for df 0.47.03

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 41.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 41.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 41.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Ben Rosser <rosser.bjr@gmail.com> - 41.0.3-1
- Update to latest release and fix setcap post script.

* Fri Aug 10 2018 Ben Rosser <rosser.bjr@gmail.com> - 41.0.2-1
- Updated to latest upstream release for 0.44.12.

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 40.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 04 2018 Ben Rosser <rosser.bjr@gmail.com> - 40.0.0-1
- Updated to latest upstream release for DF 0.44.10.

* Mon Apr 09 2018 Ben Rosser <rosser.bjr@gmail.com> - 39.3.1-1
- Update to latest upstream release, with support for DF 0.44.09.

* Wed Feb 21 2018 Ben Rosser <rosser.bjr@gmail.com> - 39.2.1-1
- Update to new upstream release.
- Split out /usr/share/dwarftherapist into noarch data subpackage.
- Make setcap a Requires(post), rather than just Requires.
- Add requires on hicolor-icon-theme.

* Tue Jan 30 2018 Ben Rosser <rosser.bjr@gmail.com> - 39.2.0-1
- Update to new upstream, with new release supporting new DF releases.

* Sat Jul 16 2016 Ben Rosser <rosser.bjr@gmail.com> - 37.0.0-4
- Add newer memory layouts from git for 0.43.02, 0.43.03.
- Compatibility with EL7; this just requires disabling compiling the documentation.

* Fri Jun 17 2016 Ben Rosser <rosser.bjr@gmail.com> - 37.0.0-3
- Arched dependency on dwarffortress is unnecessary.

* Thu May 19 2016 Ben Rosser <rosser.bjr@gmail.com> - 37.0.0-2
- Fix line endings on the changelog file.
- Slightly reword description.
- Build latex documentation multiple times to get cross-references correct.

* Wed May 18 2016 Ben Rosser <rosser.bjr@gmail.com> - 37.0.0-1
- Initial package.
