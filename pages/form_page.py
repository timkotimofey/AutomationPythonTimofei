import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators   #rename as Locator for comfort using
class FormPage(BasePage):

    def fill_fields_and_submit(self):
        person = generated_person()
        path = generated_file()
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(person.email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys(person.mobile)
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(path)
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(Locators.SUBMIT).click()
        return person   # это то, что мы будем сравнивать с результатом

    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        # for i in result_list:
        #     result_text.append(i.text)

        return result_text




