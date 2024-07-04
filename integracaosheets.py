import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()
# If modifying these scopes, delete the file token.json.
SCOPES = [os.getenv("SCOPES")]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = os.getenv("SAMPLE_SPREADSHEET_ID")
SAMPLE_RANGE_NAME = os.getenv("SAMPLE_RANGE_NAME")

def get_sheet(): 
  '''
  Autentica e retorna um objeto de serviço do Google Sheets.
  '''
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  service = build("sheets", "v4", credentials=creds)
  sheet = service.spreadsheets()
  return sheet

def update_sheet(data):
  #we have to insert in the first empty row
  sheet = get_sheet()
  body = {'values': data}
  result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME,
                                insertDataOption='INSERT_ROWS', valueInputOption='USER_ENTERED', body=body).execute()                              

def locate_empty_row():
    '''
    Retorna a primeira linha vazia da planilha
    '''
    sheet = get_sheet()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
    #'values' contém os dados das células no formato de uma lista de listas (cada lista interna representa uma linha da planilha).
    values = result['values']
    return f"A{len(values)+1}"
