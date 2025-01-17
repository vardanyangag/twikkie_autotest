import logging
import time

from pytest import mark

import utilities.custom_logger as cl
from pages.login_page.login_page import LoginPage
from pages.settings_company.company_settings import SettingsCompanyPage


@mark.regression
@mark.smoke
def test_that_user_can_see_the_Settings_icon_and_is_working_TC_1(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(f"{test_that_user_can_see_the_Settings_icon_and_is_working_TC_1} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(settings_company_page.DOMAIN_NAME)
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.VALID_PASSWORD)
    time.sleep(2)
    user_login_page.click_on_later_button()
    assert settings_company_page.check_settings_icon_presence()
    settings_company_page.click_on_setting_icon()
    time.sleep(2)
    assert settings_company_page.URL_SETTINGS_SUBDIRECTORY in driver.current_url
    log.info(f"{test_that_user_can_see_the_Settings_icon_and_is_working_TC_1} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_on_clicking_Settings_icon_user_is_been_directed_to_Settings_screen_TC_2(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_that_on_clicking_Settings_icon_user_is_been_directed_to_Settings_screen_TC_2} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(settings_company_page.DOMAIN_NAME)
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.VALID_PASSWORD)
    time.sleep(5)
    user_login_page.click_on_later_button()
    assert settings_company_page.check_settings_icon_presence()
    settings_company_page.click_on_setting_icon()
    time.sleep(1)
    assert settings_company_page.URL_SETTINGS_SUBDIRECTORY in driver.current_url
    log.info(
        f"{test_that_on_clicking_Settings_icon_user_is_been_directed_to_Settings_screen_TC_2} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_Company_Module_is_visible_on_Settings_page_TC_3(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(f"{test_that_Company_Module_is_visible_on_Settings_page_TC_3} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(settings_company_page.DOMAIN_NAME)
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.VALID_PASSWORD)
    time.sleep(1)
    settings_company_page.navigate_to_the_settings_page()
    assert settings_company_page.check_company_module_presence()
    log.info(f"{test_that_Company_Module_is_visible_on_Settings_page_TC_3} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_upon_clicking_Company_module_company_detail_page_should_appear_TC_4(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_that_upon_clicking_Company_module_company_detail_page_should_appear_TC_4} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(settings_company_page.DOMAIN_NAME)
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.VALID_PASSWORD)
    settings_company_page.navigate_to_settings_company_module()
    time.sleep(2)
    assert settings_company_page.URL_COMPANY_SETTING_SUBDIRECTORY in driver.current_url
    assert settings_company_page.check_company_module_detail_page_appear
    log.info(
        f"{test_that_upon_clicking_Company_module_company_detail_page_should_appear_TC_4} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_company_detail_page_is_showing_the_same_details_which_user_has_entered_while_sign_up_TC_5(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_that_company_detail_page_is_showing_the_same_details_which_user_has_entered_while_sign_up_TC_5} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(settings_company_page.DOMAIN_NAME)
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.VALID_PASSWORD)
    settings_company_page.navigate_to_settings_company_module()
    assert settings_company_page.validate_company_module_page_data
    log.info(
        f"{test_that_company_detail_page_is_showing_the_same_details_which_user_has_entered_while_sign_up_TC_5} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_by_default_logo_color_is_showing_green_TC_6(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(f"{test_that_by_default_logo_color_is_showing_green_TC_6} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(settings_company_page.DOMAIN_NAME)
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.VALID_PASSWORD)
    settings_company_page.navigate_to_settings_company_module()
    assert settings_company_page.check_logo_color
    log.info(f"{test_that_by_default_logo_color_is_showing_green_TC_6} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_there_is_an_edit_icon_and_its_working_TC_7(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(f"{test_that_there_is_an_edit_icon_and_its_working_TC_7} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(settings_company_page.DOMAIN_NAME)
    user_login_page.user_login(user_login_page.VALID_USERNAME, user_login_page.VALID_PASSWORD)
    settings_company_page.navigate_to_settings_company_module()
    assert settings_company_page.check_edit_icon_presence()
    log.info(f"{test_that_there_is_an_edit_icon_and_its_working_TC_7} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_Upon_clicking_on_edit_icon_user_cannot_edit_the_Domain_name_field_TC_8(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_that_Upon_clicking_on_edit_icon_user_cannot_edit_the_Domain_name_field_TC_8} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    settings_company_page.fill_otp()
    settings_company_page.click_on_setting_icon()
    settings_company_page.click_on_company_module()
    settings_company_page.click_on_edit_icon()
    assert settings_company_page.check_domain_name_has_readonly_attribute
    log.info(
        f"{test_that_Upon_clicking_on_edit_icon_user_cannot_edit_the_Domain_name_field_TC_8} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_in_editable_form_user_is_able_to_modify_Company_name_TC_9(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(f"{test_that_in_editable_form_user_is_able_to_modify_Company_name_TC_9} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    settings_company_page.fill_otp()
    settings_company_page.edit_company_name_from_company_module(settings_company_page.NEW_COMPANY_NAME)
    assert (user_login_page.get_operation_successful_validation_message() ==
            user_login_page.OPERATION_SUCCESSFUL_VALIDATION_MESSAGE)
    assert (settings_company_page.get_filled_input_field(settings_company_page.NEW_COMPANY_NAME) ==
            settings_company_page.NEW_COMPANY_NAME)
    settings_company_page.edit_company_name_from_company_module(settings_company_page.COMPANY_NAME)
    log.info(f"{test_that_in_editable_form_user_is_able_to_modify_Company_name_TC_9} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_In_Editable_form_user_is_able_to_modify_Contact_Person_First_name_and_Last_Name_TC_10(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_that_In_Editable_form_user_is_able_to_modify_Contact_Person_First_name_and_Last_Name_TC_10} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    settings_company_page.fill_otp()
    time.sleep(2)
    settings_company_page.edit_first_and_last_name_from_company_module(settings_company_page.NEW_FIRST_NAME,
                                                                       settings_company_page.NEW_LAST_NAME)
    assert (user_login_page.get_operation_successful_validation_message() ==
            user_login_page.OPERATION_SUCCESSFUL_VALIDATION_MESSAGE)
    assert (settings_company_page.get_filled_input_field(
        settings_company_page.NEW_FIRST_NAME + ' ' + settings_company_page.NEW_LAST_NAME) ==
            settings_company_page.NEW_FIRST_NAME + ' ' + settings_company_page.NEW_LAST_NAME)
    settings_company_page.edit_first_and_last_name_from_company_module(settings_company_page.FIRST_NAME,
                                                                       settings_company_page.LAST_NAME)
    log.info(
        f"{test_that_In_Editable_form_user_is_able_to_modify_Contact_Person_First_name_and_Last_Name_TC_10} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_In_Editable_form_user_is_able_to_modify_Contact_Email_Address_TC_11(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_that_In_Editable_form_user_is_able_to_modify_Contact_Email_Address_TC_11} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    settings_company_page.fill_otp()
    settings_company_page.edit_email_address_from_company_module(user_login_page.VALID_USERNAME2.capitalize())
    assert (user_login_page.get_operation_successful_validation_message() ==
            user_login_page.OPERATION_SUCCESSFUL_VALIDATION_MESSAGE)
    assert (settings_company_page.get_filled_input_field(user_login_page.VALID_USERNAME2.capitalize()) ==
            user_login_page.VALID_USERNAME2.capitalize())
    settings_company_page.edit_email_address_from_company_module(user_login_page.VALID_USERNAME2.casefold())
    log.info(
        f"{test_that_In_Editable_form_user_is_able_to_modify_Contact_Email_Address_TC_11} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_if_user_changed_email_address_and_update_it_such_update_is_visible_TC_12(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_that_if_user_changed_email_address_and_update_it_such_update_is_visible_TC_12} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    settings_company_page.fill_otp()
    settings_company_page.edit_email_address_from_company_module(settings_company_page.NEW_VALID_USERNAME)
    assert (user_login_page.get_operation_successful_validation_message() ==
            user_login_page.OPERATION_SUCCESSFUL_VALIDATION_MESSAGE)
    assert (settings_company_page.get_filled_input_field(settings_company_page.NEW_VALID_USERNAME) ==
            settings_company_page.NEW_VALID_USERNAME)
    settings_company_page.edit_email_address_from_company_module(settings_company_page.NEW_VALID_USERNAME)
    log.info(
        f"{test_that_if_user_changed_email_address_and_update_it_such_update_is_visible_TC_12} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_user_cannot_be_able_to_login_with_their_changed_correspondence_email_address_TC_13(driver):
    log = cl.custom_logger(logging.DEBUG)
    settings_company_page = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_that_user_cannot_be_able_to_login_with_their_changed_correspondence_email_address_TC_13} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    settings_company_page.fill_otp()
    settings_company_page.edit_email_address_from_company_module(settings_company_page.NEW_VALID_USERNAME)
    user_login_page.click_on_logout_button()
    user_login_page.user_login(settings_company_page.NEW_VALID_USERNAME, user_login_page.VALID_PASSWORD2)
    assert (user_login_page.get_invalid_credentials_error_message() ==
            user_login_page.INVALID_CREDENTIALS)
    log.info(
        f"{test_that_user_cannot_be_able_to_login_with_their_changed_correspondence_email_address_TC_13} >>>>>>>>>>>>>>>>> finished")


@mark.regression
@mark.smoke
def test_that_selecting_a_country_automatically_selects_the_corresponding_currency_in_the_dropdown_TC_15(driver):
    log = cl.custom_logger(logging.DEBUG)
    company_module = SettingsCompanyPage(driver)
    user_login_page = LoginPage(driver)
    log.info(
        f"{test_that_selecting_a_country_automatically_selects_the_corresponding_currency_in_the_dropdown_TC_15} >>>>>>>>>>>>>>>>> started")
    user_login_page.navigate_to_domain_page()
    user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
    user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
    company_module.fill_otp()
    company_module.navigate_to_edit_form()
    company_module.select_random_option_from_dropdown(company_module.country_dropdown_xpath_locator)
    time.sleep(2)
    assert company_module.get_automatically_selected_currency(company_module.default_currency_xpath_locator)
    log.info(
        f"{test_that_selecting_a_country_automatically_selects_the_corresponding_currency_in_the_dropdown_TC_15} >>>>>>>>>>>>>>>>> finished")



























# @mark.regression
# @mark.smoke
# def test_that_system_cannot_allow_user_submit_update_upon_leaving_any_of_the_mandatory_field_blank_TC_21(driver):
#     log = cl.custom_logger(logging.DEBUG)
#     company_module = SettingsCompanyPage(driver)
#     user_login_page = LoginPage(driver)
#     driver = SeleniumDriver(driver)
#     log.info(
#         f"{test_that_system_cannot_allow_user_submit_update_upon_leaving_any_of_the_mandatory_field_blank_TC_21} >>>>>>>>>>>>>>>>> started")
#     user_login_page.navigate_to_domain_page()
#     user_login_page.submit_domain_name(user_login_page.DOMAIN_NAME_TESTAUTO)
#     user_login_page.accept_cookies()
#     user_login_page.user_login(user_login_page.VALID_USERNAME2, user_login_page.VALID_PASSWORD2)
#     company_module.fill_otp()
#     time.sleep(2)
#     company_module.navigate_to_edit_form()
#     company_module.click_on_first_name_field()
#     company_module.clear_first_name_field()
#     company_module.click_on_first_name_field()
#     company_module.clear_first_name_field()
#     company_module.fill_input_field(' ',
#                                     company_module.first_name_field_xpath_locator)
#     company_module.clear_first_name_field()
#     # driver.clear_input_fields(company_module.company_name_field_xpath_locator)
#     # driver.clear_input_fields(company_module.first_name_field_xpath_locator)
#     company_module.click_on_submit_button()
#     time.sleep(100)
#     log.info(
#         f"{test_that_system_cannot_allow_user_submit_update_upon_leaving_any_of_the_mandatory_field_blank_TC_21} >>>>>>>>>>>>>>>>> finished")
