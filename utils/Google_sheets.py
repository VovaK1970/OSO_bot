import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

sample_spreadsheet_ID = "1s3WEnxUGNOw9CzJc34ohm6F5KIPswM56ABLbihgPO7s"
sample_range_name = "Кружок Программирования!A2:B50"


def main():
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

  try:
    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=sample_spreadsheet_ID, range=sample_range_name)
        .execute()
    )
    values = result.get("values", [])
    question=[]
    answer=[]
    if not values:
      return
    for row in values:
      question.append(row[0])
      answer.append(row[1])
      dictionary=dict(zip(question,answer))
    return dictionary
  except HttpError as err:
    return
dictionary_of_programming_circle=main()

sample_range_name = "Студенческое научное общество!A2:B50"
dictionary_of_student_scientific_society=main()

sample_range_name = "Кураторы ИАТЭ НИЯУ МИФИ!A2:B50"
dictionary_of_curators=main()

sample_range_name = "Совет общежитий (СО)!A2:B50"
dictionary_of_council_of_dormitories=main()

print(dictionary_of_programming_circle)
print(dictionary_of_student_scientific_society)
print(dictionary_of_curators)
print(dictionary_of_council_of_dormitories)
