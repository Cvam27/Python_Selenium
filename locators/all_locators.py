def customColumn(column_id :int):
    column = f'[id="resultTable"] tr > td:nth-child({column_id})'
    return column


class Locators:
    table = '[id="resultTable"]'
    fileUpload = '[id="myFile"]'
    dropdown = '[id="cars"]'
    alertButton = '//button[contains(text(),"Window Alert")]'


#     Shadow dom elements
    sd_element = '[id="userName"]'
    sd_usernameInput = '[id="kils"]'
