%global commit      ceb42e570b33830a8d0375ce68249434d35e47a7
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
systemctl --user enable --now theme-switcher-auto.timer

%preun
systemctl --user disable theme-switcher-auto.timer

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}-auto.sh
%{_bindir}/%{name}-manual.sh
%{_prefix}/lib/systemd/user/%{name}-auto.service
%{_prefix}/lib/systemd/user/%{name}-auto.timer

%changelog
* Wed Jun 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20190612gitceb42e5
- Initial Package