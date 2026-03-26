def customColumnLocatorGenerator(column_id :int):
    columnData = f'[id="resultTable"] tr > td:nth-child({column_id})'
    columnHeader = f'[id="resultTable"] th:nth-child({column_id})'
    return columnData, columnHeader


class Locators:
    userTable = '[id="resultTable"]'
    fileUpload = '[id="myFile"]'
    dropdown = '[id="cars"]'
    alertButton = '//button[contains(text(),"Window Alert")]'
    searchableTable = '[class*="elementor-widget-shortcode"]'
    searchableTable_searchInput = '[id="dt-search-0"]'
    searchableTable_OSColumn = '[id="tablepress-1"] tr > td:nth-child(2)'

    # User Table
    tableUsernameCell = '[id="resultTable"] tbody tr td:nth-child(2) a'
    tableHeader = '[id="resultTable"] th'


#     Shadow dom elements
    sd_element = '[id="userName"]'
    sd_usernameInput = '[id="kils"]'
