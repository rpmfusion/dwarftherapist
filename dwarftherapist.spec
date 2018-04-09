Name:           dwarftherapist
Version:        39.3.1
Release:        1%{?dist}
Summary:        Management tool designed to run side-by-side with Dwarf Fortress

License:        MIT
URL:            https://github.com/Dwarf-Therapist/Dwarf-Therapist
Source0:        https://github.com/Dwarf-Therapist/Dwarf-Therapist/archive/v%{version}/dwarftherapist-%{version}.tar.gz

# Need cmake.
BuildRequires:  cmake

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
%cmake
%make_build

%install
%make_install

# Check the desktop file.
desktop-file-validate %{buildroot}/%{_datadir}/applications/dwarftherapist.desktop

# Install the resources?
cp -rp resources/* %{buildroot}%{_datadir}/dwarftherapist/
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p resources/img/*.xpm %{buildroot}%{_datadir}/pixmaps/

# Remove an extra copy of the license.
rm %{buildroot}%{_docdir}/dwarftherapist/LICENSE.txt

# There used to be a link from /usr/bin/dwarftherapist -> /usr/bin/DwarfTherapist
# (or a wrapper script or something). Create one manually.
ln -s %{_bindir}/DwarfTherapist %{buildroot}%{_bindir}/dwarftherapist

# Post install script; set cap permissions.
%post
sudo setcap cap_sys_ptrace=eip %{_bindir}/DwarfTherapist

%files
%{_bindir}/DwarfTherapist
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
