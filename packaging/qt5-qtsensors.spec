# The MIT License (MIT)
# 
# Copyright (c) 2013 Tomasz Olszak <olszak.tomasz@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This file is based on qtsensors.spec from Mer project
# http://merproject.org

%if "%{tizen}" == "2.1"
%define profile mobile
%endif

%if "%{tizen}" == "2.3"
%define profile wearable
%endif

%bcond_with tizen_sensors

Name:       qt5-qtsensors
Summary:    Qt Sensors module
Version:    5.4.1
Release:    0
Group:      Base/Libraries
License:    LGPL-2.1+ or GPL-3.0
URL:        http://qt.digia.com
Source0:    %{name}-%{version}.tar.bz2
Source1001: %{name}.manifest
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes
%if %{with tizen_sensors}
BuildRequires:  pkgconfig(capi-system-sensor)
%endif

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt sensors module


%package devel
Summary:    Qt sensors - development files
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt sensors module development files


%package -n qt5-qtdeclarative-import-sensors
Summary:    QtQml sensors import
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtdeclarative

%description -n qt5-qtdeclarative-import-sensors
This package contains the Sensors import for Qtml

%package plugin-generic
Summary:    Generic sensors plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description plugin-generic
This package contains the generic plugin for sensors

%if %{with tizen_sensors}
%package plugin-tizen
Summary:    Tizen sensors plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description plugin-tizen
This package contains the tizen plugin for sensors
%endif

%package plugin-linuxsys
Summary:    Linux sensors plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description plugin-linuxsys
This package contains the linux plugin for sensors

%package plugin-gestures-shake
Summary:    Shake gesture plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description plugin-gestures-shake
This package contains the shake gesture plugin for sensors

%package plugin-gestures-sensor
Summary:    Sensor gesture plugin
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}

%description plugin-gestures-sensor
This package contains the gesture plugin for sensors

#### Build section

%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .
export QTDIR=/usr/share/qt5
touch .git
qmake -qt=5 
#CONFIG+=sensorfw
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
%fdupes %{buildroot}/%{_includedir}




#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig




#### File section


%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5Sensors.so.5
%{_libdir}/libQt5Sensors.so.5.*

%files devel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5Sensors.so
%{_libdir}/libQt5Sensors.prl
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/*
%{_datadir}/qt5/mkspecs
%{_libdir}/cmake

%files -n qt5-qtdeclarative-import-sensors
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/qml/QtSensors

%files plugin-generic
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/sensors/libqtsensors_generic.so

%if %{with tizen_sensors}
%files plugin-tizen
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/sensors/libqtsensors_tizen.so
%endif

%files plugin-linuxsys
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/sensors/libqtsensors_linuxsys.so

%files plugin-gestures-shake
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/sensorgestures/libqtsensorgestures_shakeplugin.so

%files plugin-gestures-sensor
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/qt5/plugins/sensorgestures/libqtsensorgestures_plugin.so


#### No changelog section, separate $pkg.changes contains the history
