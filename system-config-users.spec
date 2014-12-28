Summary:	A graphical interface for administering users and groups
Name:		system-config-users
Version:	1.2.113
Release:	2
License:	GPL v2+
Group:		Applications/System
URL:		http://fedoraproject.org/wiki/SystemConfig/users
Source0:	http://fedorahosted.org/released/system-config-users/%{name}-%{version}.tar.bz2
# Source0-md5:	eca1beb0c9792077af265596f26f2286
BuildRequires:	/bin/bash
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	python >= 2.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	/usr/bin/pgrep
Requires:	python >= 2.0
Requires:	python-cracklib
Requires:	python-libuser >= 0.56
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk >= 2.6
Requires:	python-rhpl
Requires:	python-rpm
Requires:	usermode-gtk >= 1.94
Requires:	xdg-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
system-config-users is a graphical utility for administrating users
and groups. It depends on the libuser library.

%prep
%setup -q

%build
%{__make} \
	SHELL=/bin/bash \
	CONSOLE_USE_CONFIG_UTIL=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	SHELL=/bin/bash \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_postclean %{_datadir}/%{name}

cat <<'EOF' > $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}
#!/bin/sh
export PYTHONPATH=%{_datadir}/%{name}
exec %{__python} %{_datadir}/%{name}/%{name}.pyc
EOF

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.apps/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py[co]
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.glade
%{_mandir}/man8/%{name}*
#%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_desktopdir}/%{name}.desktop
