import file_helper as file
import form_submit as fs
import url_util
import adjust_answer as ans


def prepare_form():
    payload_generator = fs.generate_payloads(url_util.URL_GET, False, ans.adjust_answer, 100)

    file.save_payloads_to_excel(payload_generator, filename=file.RAW_DATA_PATH_FILE)


prepare_form()
