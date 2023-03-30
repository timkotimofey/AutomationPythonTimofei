from pages.form_page import FormPage


class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_fields_and_submit()
        result = form_page.form_result()
        print(person)
        print(result)
        # assert f'{first_name} {last_name}' == result[0], 'the form has not been filled'     # assert позволяет сравнить одно с другим (протестировать)
        # assert email == result[1], 'the form has not been filled'
