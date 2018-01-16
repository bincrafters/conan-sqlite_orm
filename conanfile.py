#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class sqlite_ormConan(ConanFile):
    name = "sqlite_orm"
    version = "master"
    license = "MIT"
    exports = ["LICENSE"]
    description = " The C++14 wrapper around sqlite library."
    url = "https://github.com/AlexandrePTJ/conan-sqlite_modern_cpp"

    def source(self):
        base_url = "https://github.com/fnc12/sqlite_orm"
        archive_prefix = "/archive/"
        archive_ext = ".tar.gz"
        tools.get(base_url + archive_prefix + self.version + archive_ext)

    def package(self):
        self.copy("*.h", dst="include", src="sqlite_orm-%s/include" % (self.version))

    def package_id(self):
        self.info.header_only()
