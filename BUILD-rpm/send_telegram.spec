%global debug_package %{nil}

Name:		send_telegram	
Version:	1.0
Release:	1%{?dist}
Summary:	send_message to Telegram via telegrambot

License:	Honzula Licence
URL:		https://github.com/honzula/send_telegram

#Source0: 	%{name}-%{version}.tar

#BuildRequires:	
Requires:	curl

%description


%prep
rm -rf %{_builddir}
mkdir -p %{_builddir}
cd %{_builddir}
git clone https://github.com/honzula/send_telegram
%build

%install
rsync -aur %{_builddir}/%{name}/%{name}/ $RPM_BUILD_ROOT/

%files
#%doc
/usr/bin/send_telegram
%config(noreplace) /etc/send_telegram

%changelog

