import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from env import scopes
from env import sample_spreadsheet_ID

sample_range_name_of_programming_circle = "Кружок Программирования!A2:B50"
sample_range_name_of_student_scientific_society = "Студенческое научное общество!A2:B50"
sample_range_name_of_curators = "Кураторы ИАТЭ НИЯУ МИФИ!A2:B50"
sample_range_name_of_council_of_dormitories = "Совет общежитий (СО)!A2:B50"

def reading_google_sheets (sample_range_name):
  i=0
  creds = None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", scopes)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", scopes
      )
      creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
      token.write(creds.to_json())
  while i<1:
    try:
      service = build("sheets", "v4", credentials=creds)

      sheet = service.spreadsheets()
      result = (
          sheet.values()
          .get(spreadsheetId=sample_spreadsheet_ID, range=sample_range_name)
          .execute()
      )
    except HttpError as err:
      return
    else:
      values = result.get("values", None)
      question=[]
      answer=[]
      if values is None:
        return
      for row in values:
        question.append(row[0])
        answer.append(row[1])
        dictionary=dict(zip(question,answer))
      i+=1
    return dictionary
dictionary_of_programming_circle=reading_google_sheets(sample_range_name_of_programming_circle)
dictionary_of_student_scientific_society=reading_google_sheets(sample_range_name_of_student_scientific_society)
dictionary_of_curators=reading_google_sheets(sample_range_name_of_curators)
dictionary_of_council_of_dormitories=reading_google_sheets(sample_range_name_of_council_of_dormitories)
