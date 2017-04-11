%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global commit b1d37696469921f1025395201864842427fc32fb
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif


Name:           python-openid
Version:        2.2.5
Release:        11%{?dist}
Summary:        Python OpenID libraries

Group:          Development/Languages
License:        ASL 2.0
URL:            http://github.com/openid/python-openid
Source0:	    https://github.com/openid/%{name}/archive/%{commit}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-lxml
#BuildRequires:  Django
Requires:       python-lxml

%description
The OpenID library with batteries included.

Features of the 2.x.x series include:

 * Refined and easy-to-use API.
 * Extensive documentation.
 * Many storage implemetations including file-based, sqlite,
   postgresql, and mysql.
 * Simple examples to help you get started.
 * Licensed under the Apache Software License.
 * Includes a Simple Registration API
 * Versions 1.x.x supports protocol version 1; versions 2.x.x support
   both major OpenID protocol versions transparently

%prep
%setup -qn %{name}-%{commit}
find . -type f | xargs chmod a-x

%build
%{__python2} setup.py build

# temporarily disable tests to allow to build with Python 2.6
# https://bugzilla.redhat.com/show_bug.cgi?id=477947
#check
#{__python} admin/runtests

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES-2.2.0 LICENSE NEWS NOTICE README.md background-associations.txt
%{python2_sitelib}/openid
%{python2_sitelib}/python_openid-*.egg-info

%changelog
* Tue Oct 06 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.2.5-11
- Remove privacy patch since lots of RPs dont follow spec

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.2.5-9
- Make it more privacy friendly by using POST

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.2.5-7
- Update to the latest git revision
- Fixes lots of bugs

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug  9 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.5-1
- Update to 2.2.5

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Feb 14 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.4-1
- Update to 2.2.4

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 26 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.2.1-3
- Temporarily disable tests to fix broken deps (#477947)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.2.1-2
- Rebuild for Python 2.6

* Mon Jul  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.1-1
- Update to 2.2.1

* Fri Jun  6 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.0-1
- Update to 2.2.0

* Sat Dec 15 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.1.1-2
- Ensure that python-lxml is present for ElementTree API support.

* Sat Dec 15 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.1.1-1
- Update to 2.1.1

* Thu Apr 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.0-1
- Update to 1.2.0

* Tue Dec  5 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.1-1
- First version for Fedora Extras

