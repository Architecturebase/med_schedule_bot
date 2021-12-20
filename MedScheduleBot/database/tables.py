import logging
import httplib2
import googleapiclient.discovery as GACD

from oauth2client.service_account import ServiceAccountCredentials as SAC
from api.loader import CREDENTIALS_FILE, spreadsheet_id

class database:
    def __init__(self, CREDENTIALS_FILE):
        credentials = SAC.from_json_keyfile_name(
            CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = GACD.build('sheets', 'v4', http = httpAuth)

        self.credentials = credentials
        self.spreadsheet_id = spreadsheet_id
        self.service = service

        #set column index for the respective data series

        self._name_surname = 0
        self._tel_number = 1
        self._email = 2
        self._user_name = 3
        self._came_at_time = 4
        self._wanted_time = 5
        self._service = 6
        self._user_id = 7
        self._came_from = 8

        #sheet parameters
        self.columns = []
        self.data = []
        self.dict_data = {}
        self.entries_count = 0
        self.visceral_therapy_num = 0
        self.manual_therapy_num = 0
        self.consult_num = 0
        self.update()

        logging.info(f'Start entries_count {self.entries_count}')

        #функция для внесения изменений в таблицах
        def update(self):
            values = self.service.spreadsheets().values().get(
                spreadsheetId = self.spreadsheet_id, majorDimension = 'COLUMNS'
            ).execute()

            self.raw_values = values['values']

            self.columns = [col[0] for col in self.raw_values]
            self.data = [col[1:] for col in self.raw_values]
            self.dict_data = dict(zip(self.columns, self.data))
            self.entries_count = len(self.dict_data[self.columns[self._user_id]])
            self.