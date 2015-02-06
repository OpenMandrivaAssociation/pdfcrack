Summary:	A Password Recovery Tool for PDF-files
Name:		pdfcrack
Version:	0.11
Release:	3
License:	GPL
Group:		File tools
URL:		http://pdfcrack.sourceforge.net/
Source0:	http://mesh.dl.sourceforge.net/project/pdfcrack/pdfcrack/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:		pdfcrack-0.11-no_strip.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PDFCrack is a tool for recovering passwords and content from PDF-files.

%prep

%setup -q
%patch0 -p0

%build
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 pdfcrack %{buildroot}%{_bindir}/pdfcrack

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO changelog
%{_bindir}/pdfcrack



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11-2mdv2011.0
+ Revision: 614489
- the mass rebuild of 2010.1 packages

* Mon Apr 19 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11-1mdv2010.1
+ Revision: 536728
- import pdfcrack


* Mon Apr 19 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11-1mdv2010.1
- initial Mandriva package
