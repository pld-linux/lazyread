Summary:	Program that auto-scrolls files on your screen in movie credit fashion
Summary(pl):	Program automatycznie przewijajacy zawarto¶æ plików tekstowych na ekranie
Name:		lazyread
Version:	1.6
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.seekrut.com/rk/lr-%{version}.tar.gz
# Source0-md5:	874a8b3b2615fa7d816f51432d3fb4e7
URL:		http://seekrut.com/rk/lazyread.html
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/lr-%{version}-root-%(id -u -n)

%description
Lazyread is a program that auto-scrolls files on your screen in movie
credit fashion. You just sit back and read without needing to touch
your keyboard to manually scroll files. There are a few commands you
can enter while the program is running such as changing the scroll
speed, viewing file info, pausing etc.

%description -l pl
lazyread to program automatycznie przewijaj±cy zawarto¶æ plików na
ekranie w sposób podobny do napisów koñcowych w filmach. Pozwala
czytaæ bez potrzeby dotykania klawiatury w celu przewijania plików.
W czasie dzia³ania programu dzia³a kilka poleceñ, s³u¿±cych do zmiany
prêdko¶ci, ogl±dania informacji o pliku, zatrzymywania itp.

%prep
%setup -q -n lr-%{version}

%build
%{__cc} %{rpmcflags} %{rpmldflags} -Wall -o lr lr.c -I/usr/include/ncurses -lncurses

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install lr $RPM_BUILD_ROOT%{_bindir}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
