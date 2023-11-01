%global debug_package %{nil}

%global __python %{__python3}

Name: gtk-doc
Version: 1.28
Release: 4%{?dist}
Summary: API documentation generation tool for GTK+ and GNOME

License: GPLv2+ and GFDL
URL: http://www.gtk.org/gtk-doc
Source0: http://download.gnome.org/sources/gtk-doc/1.28/gtk-doc-%{version}.tar.xz

# Backported from upstream
# https://bugzilla.redhat.com/show_bug.cgi?id=1634770
Patch0: 0001-Please-make-the-output-reproducible.patch

# Backported from upstream
# https://bugzilla.redhat.com/show_bug.cgi?id=1853142
Patch1: 0001-scangobj-Make-G_MAXINT-appear-as-such-on-32-bit.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2052721
Patch2: gtk-doc-1.28-fix-opaque-class.patch

BuildRequires: dblatex
BuildRequires: docbook-utils
BuildRequires: /usr/bin/xsltproc
BuildRequires: docbook-style-xsl
BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: python3-six
BuildRequires: source-highlight
BuildRequires: yelp-tools

# Following are not automatically installed
Requires: docbook-utils /usr/bin/xsltproc docbook-style-xsl
Requires: python3-six
Requires: source-highlight

%description
gtk-doc is a tool for generating API reference documentation.
It is used for generating the documentation for GTK+, GLib
and GNOME.

%prep
%autosetup -p1

# Move this doc file to avoid name collisions
mv doc/README doc/README.docs

%build
export PYTHON=%{__python3}
%configure
make %{?_smp_mflags}

%install
%make_install

%check
# For reasons unknown first make check fails with texlive debug spew in log
# files. Just run it twice to work this around.
make check || make check

%files
%license COPYING COPYING-DOCS
%doc AUTHORS README doc/* examples
%{_bindir}/*
%{_datadir}/aclocal/
%{_datadir}/gtk-doc/
%{_datadir}/pkgconfig/gtk-doc.pc
%{_datadir}/help/*/gtk-doc-manual/
%{_libdir}/cmake/

%changelog
* Thu Apr 07 2022 David King <dking@redhat.com> - 1.28-4
- Generate documentation for forward declarations (#2052721)

* Mon Feb 01 2021 Kalev Lember <klember@redhat.com> - 1.28-3
- Backport an upstream patch to fix G_MAXINT appearing as G_MAXLONG on 32 bit
- Related: #1853142

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 1.28-2
- Backport a patch to fix x86_64/i686 differences in generated documentation
- Resolves: #1634770

* Sat Mar 24 2018 Kalev Lember <klember@redhat.com> - 1.28-1
- Update to 1.28
- Switch to Python 3 (#1509660)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Kalev Lember <klember@redhat.com> - 1.27-1
- Update to 1.27

* Fri Oct 06 2017 Kalev Lember <klember@redhat.com> - 1.26-2
- Add missing pkgconfig(glib-2.0) dep

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 1.26-1
- Update to 1.26
- Don't own /usr/share/gtk-doc/html/ -- packages that drop files in there need
  to co-own the directory, instead of depending on gtk-doc

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.25-6
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 18 2016 Kalev Lember <klember@redhat.com> - 1.25-2
- Use make_install macro
- Don't set group tags
- Run self tests
- Drop unused build deps

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 1.25-1
- Update to 1.25
- Make the package not noarch as it is now putting files in archful directories

* Thu Feb 04 2016 David King <amigadave@amigadave.com> - 1.24-4
- Require xsltproc, not libxslt

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Kalev Lember <kalevlember@gmail.com> - 1.24-1
- Update to 1.24

* Sun May 17 2015 Kalev Lember <kalevlember@gmail.com> - 1.23-1
- Update to 1.23

* Sun May 10 2015 Kalev Lember <kalevlember@gmail.com> - 1.22-1
- Update to 1.22
- Use license macro for the COPYING files

* Thu Jul 17 2014 Kalev Lember <kalevlember@gmail.com> - 1.21-1
- Update to 1.21

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 17 2014 Richard Hughes <rhughes@redhat.com> - 1.20-1
- Update to 1.20

* Tue Oct 29 2013 Matthias Clasen <mclasen@redhat.com> - 1.19-4
- Fix sorting of the annotation glossary 

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.19-2
- Perl 5.18 rebuild

* Wed Jun  5 2013 Matthias Clasen <mclasen@redhat.com> - 1.19-1
- Update to 1.19

* Thu Apr 25 2013 Colin Walters <walters@verbum.org> - 1.18-5.20130425gitdf075f
- New git snapshot; attempting to fix for #910830

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Matthias Clasen <mclasen@redhat.com> - 1.18-1
- Update to 1.18

* Mon Mar  7 2011 Matthias Clasen <mclasen@redhat.com> - 1.17-1
- Update to 1.17

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Matthias Clasen <mclasen@redhat.com> - 1.16-1
- Update to 1.16

* Fri Sep 24 2010 Parag Nemade <paragn AT fedoraproject.org> - 1.15-2
- Merge-review cleanup (#225870)

* Sun May 23 2010 Matthias Clasen <mclasen@redhat.com> - 1.15-1
- Update to 1.15

* Sun Mar 28 2010 Matthias Clasen <mclasen@redhat.com> - 1.14-1
- Update to 1.14

* Wed Jan  6 2010 Matthias Clasen <mclasen@redhat.com> - 1.13-2
- Fix issues with gtkdoc-fixxref

* Tue Dec 22 2009 Matthias Clasen <mclasen@redhat.com> - 1.13-1
- Update to 1.13

* Thu Dec  3 2009 Matthias Clasen <mclasen@redhat.com> - 1.11-6
- Drop unnecessary BRs

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Matthias Clasen <mclasen@redhat.com> - 1.11-3
- Fix an index generation problem

* Fri Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 1.11-2
- Update to 1.11

* Fri Jul 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.10-2
- fix license tag

* Thu Apr 24 2008 Matthias Clasen <mclasen@redhat.com> - 1.10-1
- Update to 1.10

* Tue Jan  8 2008 Matthias Clasen <mclasen@redhat.com> - 1.9-4
- Try again 

* Mon Jan  7 2008 Matthias Clasen <mclasen@redhat.com> - 1.9-3
- Improve the fix 

* Tue Dec 18 2007 Matthias Clasen <mclasen@redhat.com> - 1.9-2
- Fix a problem in gtk-doc.make

* Sun Nov 18 2007 Matthias Clasen <mclasen@redhat.com> - 1.9-1
- Update to 1.9

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 1.8-3
- Update the license field

* Thu Mar 29 2007 Matthias Clasen <mclasen@redhat.com> - 1.8-2
- Drop a no longer needed patch

* Wed Feb 21 2007 Matthias Clasen <mclasen@redhat.com> - 1.8-1
- Update to 1.8
- Fix some directory ownership issues

* Fri Feb  2 2007 Matthias Clasen <mclasen@redhat.com> - 1.7-3
- Fix the omf file (#223684)

* Wed Dec 20 2006 Matthias Clasen <mclasen@redhat.com> - 1.7-2
- Own the /usr/share/gtk-doc/html directory (#220230)

* Wed Aug  2 2006 Matthias Clasen <mclasen@redhat.com> - 1.7-1.fc6
- Update to 1.7

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.6-3.1
- rebuild

* Mon May 22 2006 Matthias Clasen <mclasen@redhat.com> 1.6-3
- Make it build in mock

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> 1.6-2
- Update to 1.6

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Jul  6 2005 Matthias Clasen <mclasen@redhat.com> 1.4-1
- update to 1.4

* Thu May  5 2005 Matthias Clasen <mclasen@redhat.com> 1.3-1
- accept ':' in ids

* Wed Jan 26 2005 Matthias Clasen <mclasen@redhat.com> 1.3-1
- update to 1.3

* Tue Sep 21 2004 Matthias Clasen <mclasen@redhat.com> 1.2-2
- rebuild 

* Fri Mar 12 2004 Alex Larsson <alexl@redhat.com> 1.2-1
- update to 1.2

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Aug 28 2003 Owen Taylor <otaylor@redhat.com> 1.1-3.0
- Move gtk-doc.pc file to %%{_datadir}/pkgconfig (#98595)
- Require: /usr/bin/cmp (#88763, Thomas Vander Stichele)
- Added libxslt docbook-style-xsl to Require: and BuildPrereq
  (#99143, Ken MacFarlane)

* Tue Jul  8 2003 Owen Taylor <otaylor@redhat.com> 1.1-2.0
- Bump for rebuild

* Thu Jun 12 2003 Owen Taylor <otaylor@redhat.com> 1.1-1
- Version 1.1

* Wed Apr 30 2003 Elliot Lee <sopwith@redhat.com> 0.10-6
- Patch to s/head -1/head -n 1/ for ppc64 etc.

* Wed Feb 12 2003 Elliot Lee <sopwith@redhat.com> 0.10-5
- BuildRequires: libxslt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan 13 2003 Owen Taylor <otaylor@redhat.com> 0.10-3
- Clean up some spec file mess

* Mon Jan 13 2003 Tim Powers <timp@redhat.com> 0.10-2
- fiter out the broken perl dep

* Sun Jan 12 2003 Havoc Pennington <hp@redhat.com>
- 0.10

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 0.9-6
- rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 30 2002 Chip Turner <cturner@redhat.com>
- add dependency filter for bogus perl dependencies

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Apr 25 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu Apr  4 2002 Jeremy Katz <katzj@redhat.com>
- update to 0.9

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- new cvs snap 0.7.90

* Mon Sep 17 2001 Matt Wilson <msw@redhat.com>
- version 0.7

* Thu May 17 2001 Havoc Pennington <hp@redhat.com>
- upgrade to a CVS snapshot
- remove patches applied upstream

* Tue Jan 16 2001 Tim Waugh <twaugh@redhat.com>
- Replace docbook, sgml-common, and stylesheets requirements with
  docbook-utils requirement.
- Use public identifier in custom stylesheets.

* Thu Dec 14 2000 Bill Nottingham <notting@redhat.com>
- rebuild because of broken fileutils

* Mon Nov 13 2000 Owen Taylor <otaylor@redhat.com>
- Version 0.4b1 (CVS snapshot)

* Fri Apr 23 1999 Owen Taylor <otaylor@redhat.com>
- added Requires

* Fri Apr 23 1999 Owen Taylor <otaylor@redhat.com>
- Initial RPM, version 0.2

