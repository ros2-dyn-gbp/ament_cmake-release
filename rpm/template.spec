%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-ament-cmake-gtest
Version:        1.3.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ament_cmake_gtest package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       gtest-devel
Requires:       ros-humble-ament-cmake-test
Requires:       ros-humble-gtest-vendor
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake-core
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The ability to add gtest-based tests in the ament buildsystem in CMake.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Apr 25 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.4-1
- Autogenerated by Bloom

* Mon Nov 07 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.3-1
- Autogenerated by Bloom

* Tue May 17 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.2-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.1-2
- Autogenerated by Bloom

* Mon Mar 28 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.1-1
- Autogenerated by Bloom

* Mon Mar 21 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.0-3
- Autogenerated by Bloom

* Fri Feb 18 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.0-2
- Autogenerated by Bloom

* Fri Feb 18 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.3.0-1
- Autogenerated by Bloom

* Thu Feb 10 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.2.1-3
- Autogenerated by Bloom

* Tue Feb 08 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.2.1-2
- Autogenerated by Bloom

