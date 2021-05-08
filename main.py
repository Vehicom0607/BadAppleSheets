import ToSpreadSheet


SPREADSHEET_ID = "1GOgCT7G7BUo5b_iM7RpGT831GLZOAQW8jayO4XEBkrQ"
service = ToSpreadSheet.initSpreadSheet()

body = {
  "requests": [
    {
      "updateCells": {
        "range": {
          "sheetId": 0,
          "startRowIndex": 0,
          "endRowIndex": 150,
          "startColumnIndex": 0,
          "endColumnIndex": 300
        },
        "rows": [
          {
            "values": [
              {
                "userEnteredFormat": {
                  "backgroundColor": {
                    "red": 1
                  }
                }
              }
            ]
          }
        ],
        "fields": "userEnteredFormat.backgroundColor"
      }
    }
  ]
}
response = service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body).execute()
