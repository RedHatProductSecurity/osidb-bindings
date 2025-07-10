%define name osidb_bindings
%define version 4.12.0
%define release 0%{?dist}

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        OSIDB Python Bindings

URL:            https://github.com/RedHatProductSecurity/osdib-bindings
Source0:        {{{ git_dir_pack }}}
VCS:            {{{ git_dir_vcs }}}
License: MIT

BuildArch:      noarch
AutoReqProv: no
BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  tox
BuildRequires:  python3-tox-current-env
Requires:       python3-aiohttp
Requires:       python3-attrs
Requires:       python3-dateutil
Requires:       python3-requests
Requires:       python3-requests-gssapi


%description
Python Client bindings for OSIDB

%prep
{{{ git_dir_setup_macro }}}

%generate_buildrequires

%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{name}

%check
%tox

%files -n %{name} -f %{pyproject_files}
%ghost %{python3_sitelib}/tests/*

%changelog
* Wed May 22 2024 Jason <jshepher@redhat.com> - 3.6.0
- RPM packing for osidb_bindings added



