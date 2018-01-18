#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class sqlite_ormConan(ConanFile):
    name = "sqlite_orm"
    version = "20180118"
    commit_id = "8c2dc3ae937c31b715c49f0d9dae109f92af1661"
    license = "MIT"
    exports = ["LICENSE"]
    description = "SQLite ORM light header only library for modern C++."
    url = "https://github.com/AlexandrePTJ/conan-sqlite_orm"

    requires = (
        "sqlite3/[~=3]@bincrafters/stable"
    )

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/fnc12/sqlite_orm"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.commit_id))
        extracted_dir = self.name + "-" + self.commit_id
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        include_folder = os.path.join(self.source_subfolder, "include")
        self.copy(pattern="LICENSE")
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
