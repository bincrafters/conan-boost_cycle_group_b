#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostCycleGroupBConan(base.BoostBaseConan):
    name = "boost_cycle_group_b" # Level 12
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_cycle_group_b"
    lib_short_names = [
        "lexical_cast",
        "math"
    ]
    header_only_libs = ["lexical_cast"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_atomic",
        "boost_concept_check",
        "boost_config",
        "boost_container",
        "boost_core",
        "boost_detail",
        "boost_fusion",
        "boost_integer",
        "boost_lambda",
        "boost_mpl",
        "boost_numeric_conversion",
        "boost_predef",
        "boost_range",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_tuple",
        "boost_type_traits"
    ]
