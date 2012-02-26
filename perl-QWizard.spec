#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	QWizard
%include	/usr/lib/rpm/macros.perl
Summary:	QWizard - Display a series of questions, get the answers, and act on the answers
Summary(pl.UTF-8):	QWizard - wyświetlanie serii pytań, pobranie odpowiedzi i ich obsługa
Name:		perl-QWizard
Version:	3.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/QWizard/QWizard-%{version}.tar.gz
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

%description -l pl.UTF-8
QWizard wyświetla listę pogrupowanych pytań, a następnie pobiera i
przetwarza odpowiedzi użytkownika. Przed obsługą odpowiedzi może być
wyświetlonych wiele pytań/odpowiedzi. Po zatwierdzeniu całości (z
udziałem użytkownika) wykonywana jest seria akcji - w kolejności
wymaganej przez programistę.

Prawdziwa siła QWizarda polega na możliwości śledzenia informacji o
stanie między jednym ekranem kreatora a następnym, nawet w zwykle
bezstanowych środowiskach, takich jak HTTP i HTML. Pozwala to
programiście zebrać duży zestaw danych z wielu prostych ekranów. Po
zebraniu wszystkich danych i zweryfikowaniu ich, można je odpowiednio
obsłużyć (np. zapisać w bazie danych, użyć do konfiguracji systemu
albo do wygenerowania wykresu).

Aktualnie istniejące interfejsy użytkownika to HTML, Gtk2, Tk oraz
(minimalnie) ReadLine. Prosta implementacja skryptów QWizarda może
wykorzystywać dowolny z formatów wyjściowych bez modyfikowania kodu.
Dzięki temu bardzo łatwo napisać przenośne skrypty kreatorów, które
można bez żadnej modyfikacji wykorzystywać w środowiskach graficznych
(Gtk2 i Tk) oraz środowiskach WWW opartych na HTML-u (np. skryptach
CGI), a także interaktywnych środowiskach tekstowych (ReadLine).

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/QWizard_Widgets.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/QWizard.pm
%{perl_vendorlib}/QWizard
%attr(755,root,root) %{perl_vendorlib}/QWizard_Widgets.pl
%dir %{perl_vendorlib}/auto/QWizard
%dir %{perl_vendorlib}/auto/QWizard/Generator
%{perl_vendorlib}/auto/QWizard/Generator/autosplit.ix
%{_mandir}/man3/QWizard*.3pm*
%{_examplesdir}/%{name}-%{version}
