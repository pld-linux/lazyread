Summary:	Program that auto-scrolls files on your screen in movie credit fashion.
Summary(pl):	Program automatycznie przewijajacy zawarto¶æ plików tekstowych na ekranie.
Name:		lazyread
Version:	1.6
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.seekrut.com/rk/lr-%{version}.tar.gz
Patch0:		lazyread-curses.patch
URL:		http://seekrut.com/rk/lazyread.html
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/lr-%{version}-root-%(id -u -n)

%description
Lazyread is a program that auto-scrolls files on your screen in movie
credit fashion. You just sit back and read without needing to touch your
keyboard to manually scroll files. There are a few commands you can enter
while the program is running such as changing the scroll speed, viewing
file info, pausing etc.

%prep
%setup -q -n lr-%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install lr $RPM_BUILD_ROOT%{_bindir}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}
%doc README
