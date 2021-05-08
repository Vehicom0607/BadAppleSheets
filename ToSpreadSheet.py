from googleapiclient.discovery import build
from google.oauth2 import service_account
def initSpreadSheet():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    credentials = service_account.Credentials.from_service_account_file('./Key/creds.json', scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    return service
