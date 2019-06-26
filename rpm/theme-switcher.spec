%global commit      b985a36c0def9f857930f4641de81e19536db80c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190627

Name:           theme-switcher
Version:        0
Release:        3.%{date}git%{shortcommit}%{?dist}
Summary:        Switch dark/light GTK theme automatically during day/night

License:        GPLv3+
URL:            https://github.com/tim77/theme-switcher
Source0:        %{url}/tarball/%{commit}#/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

%description
%{summary}.

You need to setup your light/dark profiles in gnome-terminal in order to switch
terminal themes automatically. Configure them by edit:

sudoedit /usr/bin/theme-switcher-auto.sh

%prep
%autosetup -n tim77-%{name}-%{shortcommit}

%install
mkdir -p %{buildroot}%{_bindir}
mv theme-switcher-auto.sh   %{buildroot}%{_bindir}
mv theme-switcher-manual.sh %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_userunitdir}
mv theme-switcher-auto.service  %{buildroot}%{_userunitdir}
mv theme-switcher-auto.timer    %{buildroot}%{_userunitdir}
mkdir -p %{buildroot}%{_datadir}/applications
mv theme-switcher.desktop %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/512x512
mv light-dark-icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
%systemd_user_post %{name}-auto.timer

%preun
%systemd_user_preun %{name}-auto.timer

%postun
%systemd_user_postun_with_restart %{name}-auto.timer

%files
%doc README.md CREDITS
%license LICENSE
%{_bindir}/%{name}-auto.sh
%{_bindir}/%{name}-manual.sh
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/512x512/light-dark-icon.png
%{_userunitdir}/%{name}-auto.service
%{_userunitdir}/%{name}-auto.timer

%changelog
* Wed Jun 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-3.20190612gitceb42e5
- Initial package
