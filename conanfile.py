#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class sqlite_ormConan(ConanFile):
    name = "sqlite_orm"
    version = "20180116"
    license = "MIT"
    exports = ["LICENSE"]
    description = "SQLite ORM light header only library for modern C++."
    url = "https://github.com/AlexandrePTJ/conan-sqlite_orm"


    def source(self):
        base_url = "https://github.com/fnc12/sqlite_orm"
        archive_prefix = "/archive/"
        archive_ext = ".tar.gz"
        tools.get(base_url + archive_prefix + self.version + archive_ext)

    def package(self):
        self.copy("*.h", dst="include", src="sqlite_orm-%s/include" % (self.version))

    def package_id(self):
        self.info.header_only()
