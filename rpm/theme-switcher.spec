%global commit      3db178c3a9713534cf915590cb6c63204f9b9378
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190612

Name:           theme-switcher
Version:        0
Release:        1.%{date}git%{shortcommit}%{?dist}
Summary:        Switch dark/light GTK theme automatically during day/night

License:        GPLv3+
URL:            https://github.com/tim77/theme-switcher
Source0:        %{url}/tarball/%{commit}#/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

%{?systemd_requires}
BuildRequires:  systemd

# Requires:       hicolor-icon-theme

%description
%{summary}.

You need to setup your light/dark profiles in gnome-terminal in order to switch
themes automatically. Configure them by edit:

sudoedit /usr/bin/theme-switcher-auto.sh

%prep
%autosetup -n tim77-%{name}-%{shortcommit}

%install
mkdir -p %{buildroot}%{_bindir}
mv theme-switcher-auto.sh   %{buildroot}%{_bindir}
mv theme-switcher-manual.sh %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_prefix}/lib/systemd/user
mv theme-switcher-auto.service  %{buildroot}%{_prefix}/lib/systemd/user
mv theme-switcher-auto.timer    %{buildroot}%{_prefix}/lib/systemd/user

%post
%systemd_post theme-switcher-auto.timer

%preun
%systemd_preun theme-switcher-auto.timer

%postun
%systemd_postun_with_restart theme-switcher-auto.timer

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}-auto.sh
%{_bindir}/%{name}-manual.sh
%{_prefix}/lib/systemd/user/%{name}-auto.service
%{_prefix}/lib/systemd/user/%{name}-auto.timer

%changelog
* Wed Jun 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20190612gitceb42e5
- Initial package