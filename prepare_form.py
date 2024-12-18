import file_helper
import form_submit as fs
import url_util
import adjust_answer as ans


def prepare_form():
    payload_generator = fs.generate_payloads(url_util.URL_GET, False, ans.adjust_answer, 100)
    file_helper.save_payloads_to_excel(payload_generator, filename="output_data.xlsx")


prepare_form()
