Summary:	A graphical interface for administering users and groups
Name:		system-config-users
Version:	1.2.80
Release:	2
License:	GPL v2+
Group:		Applications/System
URL:		http://fedoraproject.org/wiki/SystemConfig/users
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	07067f69f3b09e8d411ad81d872ad265
BuildRequires:	/bin/bash
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	python >= 2.0
BuildRequires:	rarian-compat
Requires(post,postun):	hicolor-icon-theme
Requires:	/usr/bin/pgrep
Requires:	hicolor-icon-theme
Requires:	python >= 2.0
Requires:	python-cracklib
Requires:	python-libuser >= 0.56
Requires:	python-pygtk-gtk >= 2.6
Requires:	python-pygtk-glade
Requires:	python-rhpl
Requires:	python-rpm
Requires:	xdg-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
system-config-users is a graphical utility for administrating users
and groups. It depends on the libuser library.

%prep
%setup -q
# this doc generation is broken on PLD
echo "doc-all:\ndoc-install:" > doc_rules.mk

%build
%{__make} \
	SHELL=/bin/bash

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	SHELL=/bin/bash \
	DESTDIR=$RPM_BUILD_ROOT

# we don't have and we don't want consolehelper
ln -s -f %{_datadir}/system-config-users/system-config-users $RPM_BUILD_ROOT%{_bindir}/system-config-users

%find_lang %{name}
find $RPM_BUILD_ROOT%{_datadir} -name "*.mo" | xargs ./utf8ify-mo

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/system-config-users
%{_datadir}/system-config-users
%{_mandir}/man8/system-config-users*
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%config(noreplace) /etc/security/console.apps/system-config-users
%config(noreplace) /etc/pam.d/system-config-users
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/system-config-users
