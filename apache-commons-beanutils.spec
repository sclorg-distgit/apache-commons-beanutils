%{?scl:%scl_package apache-%{short_name}}
%{!?scl:%global pkg_name %{name}}

%{?scl:%thermostat_find_provides_and_requires}

%global base_name       beanutils
%global short_name      commons-%{base_name}

Name:           %{?scl_prefix}apache-%{short_name}
Version:        1.8.3
Release:        18%{?dist}
Summary:        Java utility methods for accessing and modifying the properties of arbitrary JavaBeans
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}
BuildArch:      noarch
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  maven30-maven-local
BuildRequires:  %{?scl_prefix}mvn(commons-collections:commons-collections)
BuildRequires:  %{?scl_prefix}mvn(commons-logging:commons-logging)
BuildRequires:  maven30-mvn(org.apache.commons:commons-parent) >= 26-7

%description
The scope of this package is to create a package of Java utility methods
for accessing and modifying the properties of arbitrary JavaBeans.  No
dependencies outside of the JDK are required, so the use of this package
is very lightweight.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.

%prep
%{?scl:scl enable maven30 %{scl} - << "EOF"}
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' *.txt

%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :maven-assembly-plugin

%mvn_alias :{*} :@1-core :@1-bean-collections
%mvn_alias :{*} org.apache.commons:@1 org.apache.commons:@1-core org.apache.commons:@1-bean-collections
%mvn_file : %{name} %{name}-core %{name}-bean-collections
%mvn_file : %{short_name} %{short_name}-core %{short_name}-bean-collections
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - << "EOF"}
# Some tests fail in Koji
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.txt RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Wed Jun 18 2014 Severin Gehwolf <sgehwolf@redhat.com> - 1.8.3-18
- Rebuild so as to fix wrongly generated requires.

* Tue Jun 17 2014 Severin Gehwolf <sgehwolf@redhat.com> - 1.8.3-17
- Build against maven30 collection.

* Mon Jan 20 2014 Omair Majid <omajid@redhat.com> - 1.8.3-16
- Rebuild in order to fix osgi()-style provides.
- Resolves: RHBZ#1054813

* Wed Nov 27 2013 Severin Gehwolf <sgehwolf@redhat.com> - 1.8.3-15
- Properly enable SCL.

* Wed Nov 20 2013 Severin Gehwolf <sgehwolf@redhat.com> - 1.8.3-14
- Use SCL-ized packages as BRs.

* Fri Nov 15 2013 Omair Majid <omajid@redhat.com> - 1.8.3-13
- Find provides and requires automatically
- Remove Obsoletes/Provides

* Fri Nov 08 2013 Omair Majid <omajid@redhat.com> - 1.8.3-13
- SCL-ized package

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.3-13
- Add BuildRequires on apache-commons-parent >= 26-7
- Remove BuildRequires on commons-collections-testframework

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.3-12
- Remove workaround for rpm bug #646523

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.3-11
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.3-10
- Build with xmvn
- Don't generate extra JARs
- Simplify build dependencies
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.8.3-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8.3-5
- Packaging fixes
- Remove unneeded depmap
- Remove versioned jars and javadocs
- Use maven 3 to build

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8.3-3
- Add license to javadoc subpackage

* Mon May 24 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8.3-2
- Added provides to javadoc subpackage

* Fri May 21 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8.3-1
- Re-did whole spec file, dropped gcj support
- Rename package (jakarta-commons-beanutils->apache-commons-beanutils)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7.0-12.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7.0-11.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 23 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-10.3
- Fedora-specific: enable GCJ support

* Thu Oct 23 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-10.2
- Fedora-specific: BuildRequires: java-1.6.0-devel

* Thu Oct 23 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-10.1
- Fedora-specific: remove repolib
- Fedora-specific: enable JDK6 support

* Mon Oct 20 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-10
- add flag to build with maven

* Fri Sep 19 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-9
- add jdk6 patch
- fix repolib

* Sun Jun 15 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-8.jpp5
- fix duplicate files
- correctly unpack sources
- remove spurious gnu-crypto requirement
- remove spurious javadoc package requirements
- fix javadoc directory
- fix build-classpath call
- use macros

* Fri May 30 2008 Permaine Cheung <pcheung@redhat.com> - 0:1.7.0-7
- First JPP5 build

* Tue Jul 24 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.7.0-6jpp
- Make Vendor, Distribution based on macro
- Fix aot build
- Add poms and depmap frags
- Build with maven1 by default
- Add manual subpackage when built with maven

* Tue Mar 13 2007 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.7.0-2jpp.ep1.2
- Fix repolib location

* Tue Mar 13 2007 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-2jpp.ep1.1
- New repolib location

* Mon Mar 05 2007 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-2jpp.el4ep1.3
- Remove pre section used for RHUG cleanup

* Tue Feb 20 2007 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.7.0-2jpp.el4ep1.2
- Add -brew suffix

* Fri Feb 17 2007 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.7.0-2jpp.el4ep1.1
- Add repolib support

* Thu Aug 17 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-5jpp
- Require what is used in post/postun for javadoc

* Fri Jul 14 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-4jpp
- Add AOT bits

* Thu May 11 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-3jpp
- Add header
- Remove unecessary macro definitions

* Wed Feb 22 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-2jpp_1rh
- Merge with upstream

* Wed Apr 27 2005 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-1jpp_3rh
- Fix build so that collections jar is created

* Sat Jan 29 2005 Ralph Apel <r.apel@r-apel.de> - 0:1.7.0-2jpp
- Use the "dist" target to get a full build, including bean-collections

* Thu Oct 21 2004 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-1jpp_1rh
- Import from upstream

* Thu Oct 21 2004 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-1jpp
- Upgrade to 1.7.0

* Fri Oct 1 2004 Andrew Overholt <overholt@redhat.com> 0:1.6.1-4jpp_6rh
- add coreutils BuildRequires

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.6.1-5jpp
- Rebuild with ant-1.6.2

* Fri Jul 2 2004 Aizaz Ahmed <aahmed@redhat.com> 0:1.6.1-4jpp_5rh
- Added trigger to restore symlinks that are removed if ugrading
  from a commons-beanutils rhug package

* Fri Apr  2 2004 Frank Ch. Eigler <fche@redhat.com> 0:1.6.1-4jpp_4rh
- more of the same, for version-suffixed .jar files

* Fri Mar 26 2004 Frank Ch. Eigler <fche@redhat.com> 0:1.6.1-4jpp_3rh
- add RHUG upgrade cleanup

* Fri Mar  5 2004 Frank Ch. Eigler <fche@redhat.com> 0:1.6.1-4jpp_2rh
- RH vacuuming part II

* Thu Mar  4 2004 Frank Ch. Eigler <fche@redhat.com> 0:1.6.1-4jpp_1rh
- RH vacuuming

* Fri May 09 2003 David Walluck <david@anti-microsoft.org> 0:1.6.1-4jpp
- update for JPackage 1.5

* Thu Feb 27 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.6.1-2jpp
- fix ASF license and add packager name

* Wed Feb 19 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.6.1-1jpp
- 1.6.1

* Thu Feb 13 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.6-1jpp
- 1.6

* Thu Oct 24 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.5-1jpp
- 1.5

* Fri Aug 23 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.4.1-1jpp
- 1.4.1

* Tue Aug 20 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.4-1jpp
- 1.4

* Fri Jul 12 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.3-3jpp
- change to commons-xxx.jar instead of commons-xxx.home in ant parameters

* Mon Jun 10 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.3-2jpp
- use sed instead of bash 2.x extension in link area to make spec compatible
  with distro using bash 1.1x

* Fri Jun 07 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.3-1jpp
- 1.3
- added short names in %%{_javadir}, as does jakarta developpers
- first jPackage release
