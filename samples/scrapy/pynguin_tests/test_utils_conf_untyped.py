# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import utils.conf_untyped as module_0
import scrapy.settings as module_1
import scrapy.exceptions as module_2
import scrapy.utils.deprecate as module_3


@pytest.mark.xfail(strict=True)
def test_case_0():
    var_0 = module_0.init_env()
    var_1 = module_0.get_sources()
    dict_0 = {}
    module_0.build_component_list(var_1, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "aw<H8E@?a"
    none_type_0 = None
    module_0.build_component_list(str_0, convert=none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    dict_0 = {}
    var_0 = module_0.build_component_list(dict_0)
    var_0.__lshift__(var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    var_0 = module_0.get_sources()
    module_0.arglist_to_dict(var_0)


def test_case_4():
    var_0 = module_0.closest_scrapy_cfg()
    assert var_0 == ""


def test_case_5():
    var_0 = module_0.init_env()


def test_case_6():
    base_settings_0 = module_1.BaseSettings()
    var_0 = module_0.get_sources(base_settings_0)
    with pytest.raises(module_2.UsageError):
        module_0.feed_process_params_from_cli(base_settings_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    base_settings_0 = module_1.BaseSettings()
    var_0 = module_0.feed_process_params_from_cli(
        base_settings_0, base_settings_0, overwrite_output=base_settings_0
    )
    var_1 = module_0.arglist_to_dict(var_0)
    var_0.__rdivmod__(var_1)


@pytest.mark.xfail(strict=True)
def test_case_8():
    var_0 = module_0.init_env()
    var_1 = module_0.get_sources()
    dict_0 = {var_0: var_0}
    var_2 = module_0.build_component_list(dict_0)
    module_0.build_component_list(var_1)


@pytest.mark.xfail(strict=True)
def test_case_9():
    var_0 = module_0.get_sources()
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_1 = module_0.build_component_list(dict_0)
    base_settings_0 = module_1.BaseSettings()
    var_2 = module_0.feed_complete_default_values_from_settings(dict_0, base_settings_0)
    module_0.feed_process_params_from_cli(
        base_settings_0, bool_0, overwrite_output=var_1
    )


@pytest.mark.xfail(strict=True)
def test_case_10():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.init_env(bool_0)
    var_1 = module_0.build_component_list(dict_0, dict_0)
    var_2 = module_0.get_config()
    var_3 = module_0.get_config()
    var_4 = dict_0.__eq__(var_0)
    var_5 = module_0.get_sources()
    var_6 = module_0.init_env()
    int_0 = var_2.__len__()
    var_7 = var_1.__eq__(var_1)
    module_0.build_component_list(var_2)


def test_case_11():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    var_0 = module_3.update_classpath(bool_0)
    var_1 = module_0.build_component_list(dict_0)
    var_2 = module_0.build_component_list(dict_0, var_1)
    var_3 = var_0.__and__(bool_0)
    var_4 = module_0.init_env(bool_0, var_2)
    var_5 = module_0.get_config(var_1)
    var_6 = var_1.__eq__(bool_0)
    var_7 = module_0.init_env(set_syspath=var_4)
    base_settings_0 = module_1.BaseSettings()
    var_8 = module_0.feed_complete_default_values_from_settings(dict_0, base_settings_0)
    var_9 = module_0.init_env()
    var_10 = module_0.closest_scrapy_cfg()
    assert var_10 == ""
    none_type_0 = None
    var_11 = var_1.__eq__(none_type_0)
    var_12 = module_0.build_component_list(base_settings_0)
    var_13 = module_0.init_env(var_12)


def test_case_12():
    base_settings_0 = module_1.BaseSettings()
    var_0 = module_0.build_component_list(base_settings_0)
    var_1 = module_0.closest_scrapy_cfg()
    assert var_1 == ""
    var_2 = module_0.closest_scrapy_cfg()
    assert var_2 == ""


@pytest.mark.xfail(strict=True)
def test_case_13():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    base_settings_0 = module_1.BaseSettings(dict_0)
    module_0.build_component_list(base_settings_0, convert=dict_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    var_0 = module_3.update_classpath(bool_0)
    var_1 = module_0.build_component_list(dict_0)
    int_0 = 2776
    var_2 = var_0.__rdivmod__(dict_0)
    var_3 = var_0.__or__(int_0)
    tuple_0 = (var_2, var_3, var_2, var_2)
    module_0.build_component_list(int_0, tuple_0)


def test_case_15():
    base_settings_0 = module_1.BaseSettings()
    var_0 = module_0.feed_complete_default_values_from_settings(
        base_settings_0, base_settings_0
    )


@pytest.mark.xfail(strict=True)
def test_case_16():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    base_settings_0 = module_1.BaseSettings()
    var_0 = module_0.feed_complete_default_values_from_settings(dict_0, base_settings_0)
    module_0.feed_process_params_from_cli(
        base_settings_0, bool_0, overwrite_output=var_0
    )


def test_case_17():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.closest_scrapy_cfg()
    assert var_0 == ""
    var_1 = module_0.build_component_list(dict_0)
    var_2 = module_0.build_component_list(dict_0, var_1)
    var_3 = module_0.init_env(bool_0, var_2)
    var_4 = module_0.get_config(var_1)
    var_5 = var_1.__eq__(bool_0)
    var_6 = module_0.init_env(set_syspath=var_3)
    base_settings_0 = module_1.BaseSettings()
    with pytest.raises(module_2.UsageError):
        module_0.feed_process_params_from_cli(
            base_settings_0, var_4, overwrite_output=dict_0
        )


def test_case_18():
    base_settings_0 = module_1.BaseSettings()
    var_0 = module_0.feed_process_params_from_cli(
        base_settings_0, base_settings_0, overwrite_output=base_settings_0
    )


def test_case_19():
    base_settings_0 = module_1.BaseSettings()
    var_0 = module_0.feed_complete_default_values_from_settings(
        base_settings_0, base_settings_0
    )
    with pytest.raises(module_2.UsageError):
        module_0.feed_process_params_from_cli(base_settings_0, var_0)


def test_case_20():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    base_settings_0 = module_1.BaseSettings(dict_0)
    with pytest.raises(module_2.UsageError):
        module_0.feed_process_params_from_cli(base_settings_0, dict_0, bool_0)


def test_case_21():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.build_component_list(dict_0)
    var_1 = var_0.clear()
    var_2 = module_0.init_env(bool_0, var_1)
    var_3 = module_0.init_env(set_syspath=var_2)
    var_4 = module_0.init_env()
    var_5 = module_0.get_config(dict_0)
    base_settings_0 = module_1.BaseSettings(var_3)
    with pytest.raises(module_2.UsageError):
        module_0.feed_process_params_from_cli(base_settings_0, var_0, bool_0)
