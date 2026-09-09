import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library

def test_add_student_multiple_data():
    # API
    api_url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('/home/qamaster/Udemy/API/APIAutomation/DataFiles/addStudentMultipleData.json')
    json_request = json.loads(file.read())

    obj = Library.Common('/home/qamaster/Udemy/API/APIAutomation/DataFiles/TestData.xlsx', 'Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range (2, row+1):
        updated_json_request = obj.update_request_with_data(i,json_request,keyList)
        response = requests.post(api_url,updated_json_request)
        print(response)