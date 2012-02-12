#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	QWizard
%include	/usr/lib/rpm/macros.perl
Summary:	QWizard - Display a series of questions, get the answers, and act on the answers
Name:		perl-QWizard
Version:	3.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HARDAKER/QWizard-%{version}.tar.gz
# Source0-md5:	e5cf695466d39ad6c7f242ad58b7ad97
URL:		http://search.cpan.org/dist/QWizard/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QWizard displays a list of grouped questions, and retrieves and
processes user-specified answers to the questions. Multiple
question/answer sets may be displayed before the answers are dealt
with. Once a "commit" action is taken (instigated by the user), a
series of actions is performed to handle the answers. The actions are
executed in the order required by the QWizard programmer.

QWizard's real power lies in its inherent ability to keep track of all
state information between one wizard screen and the next, even in
normally stateless transaction environments like HTTP and HTML. This
allows a QWizard programmer to collect a large body of data with a
number of simple displays. After all the data has been gathered and
verified, then it can be handled as appropriate (e.g., written to a
database, used for system configuration, or used to generate a graph.)

Current user interfaces that exist are HTML, Gtk2, Tk, and (minimally)
ReadLine. A single QWizard script implementation can make use of any
of the output formats without code modification. Thus it is extremely
easy to write portable wizard scripts that can be used without
modification by both graphical window environments (Gtk2 and Tk) and
HTML-based web environments (e.g., CGI scripts.), as well with
intercative command line enviornments (ReadLine).

Back-end interfaces (child classes of the QWizard::Generator module)
are responsible for displaying the information to the user. Currently
HTML, Gtk2, Tk and ReadLine, are the output mechanisms that work the
best (in that order). Some others are planned (namely a curses
version), but are not far along in development. Developing new
generator back-ends is fairly simple and doesn't take a lot of code
(assuming the graphic interface is fairly powerful and contains a
widget library.)

QWizard operates by displaying a series of "screens" to the user. Each
screen is defined in a QWizard construct called a primary that
describes the attributes of a given screen, including the list of
questions to be presented to the user. Primaries can contain
questions, things to do immediately after the questions are answered
(post_answers), and things to do once the entire series of screens
have been answered (actions). Other information, such as a title and
an introduction, can also be attached to a primary.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/QWizard/
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
