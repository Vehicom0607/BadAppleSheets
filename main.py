# Downloads Youtube Video. Run only once.
# from Video import GetYoutubeVideo
# GetYoutubeVideo.DownloadYouTubeVideo()
# Rename video to video.mp4 after downloading

# Them convert the mp4 to individual frames using cv2
# Run ConvertToFrames.py manually. No idea why it doesn't work when i import it.
# Too lazy to debug this


# Downloads Youtube Video. Run only once.
# from Video import GetYoutubeVideo
# GetYoutubeVideo.DownloadYouTubeVideo()
# Rename video to video.mp4 after downloading

# Them convert the mp4 to individual frames using cv2
# Run ConvertToFrames.py manually. No idea why it doesn't work when i import it.
# Too lazy to debug this


import CreateRequest
import ToSpreadSheet
import cv2
import time
import gspread


def update_sheet(SPREADSHEET_ID, body):
    response = service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body).execute()
    print(response)
    return response





SPREADSHEET_ID = "1GOgCT7G7BUo5b_iM7RpGT831GLZOAQW8jayO4XEBkrQ"
service = ToSpreadSheet.initSpreadSheet()
ROWS = 94
COLS = 168
FRAMES = 5300

gc = gspread.service_account('./Key/creds.json')
wsh = gc.open_by_key(SPREADSHEET_ID).worksheet("Normal Sheet")


print("Program Started")


for i in range(1, FRAMES + 1):
    img = cv2.imread('./Video/rrframes/%s.png' % i)
    body = CreateRequest.create_request(ROWS, COLS, img)
    print("Frame %s Rendered" % i)
    result = False
    while not result:
        try:
            result = update_sheet(SPREADSHEET_ID, body)
            wsh.update_title(time.ctime())
        except:
            print("Tried Again")
            pass



