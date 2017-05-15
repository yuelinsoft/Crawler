# -*- coding: utf-8 -*-

def press_button(driver, button_get_type, button_get_content):
    if button_get_type == 0:  # is By.XPATH:
        driver.find_element_by_xpath(button_get_content).click()
    elif button_get_type == 1:  # is By.CLASS_NAME:
        driver.find_element_by_class_name(button_get_content).click()
    elif button_get_type == 2:  # is By.CSS_SELECTOR:
        driver.find_element_by_css_selector(button_get_content).click()
    elif button_get_type == 3:  # is By.ID:
        driver.find_element_by_id(button_get_content).click()
    elif button_get_type == 4:  # is By.LINK_TEXT:
        driver.find_element_by_link_text(button_get_content).click()
    elif button_get_type == 5:  # is By.NAME:
        driver.find_element_by_name(button_get_content).click()
    elif button_get_type == 6:  # is By.TAG_NAME:
        driver.find_element_by_tag_name(button_get_content).click()