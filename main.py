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



def update_sheet(SPREADSHEET_ID, body, frame):
    result = service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body).execute()
    print("Frame %s Sent" % frame)


SPREADSHEET_ID = "1GOgCT7G7BUo5b_iM7RpGT831GLZOAQW8jayO4XEBkrQ"
service = ToSpreadSheet.initSpreadSheet()
ROWS = 150
COLS = 300
FRAMES = 6300
print("Program Started")

data = []

for i in range(43, FRAMES + 1):
    img = cv2.imread('./Video/frames/%s.png' % i)
    body = CreateRequest.create_request(ROWS, COLS, img)
    print("Frame %s Rendered" % i)
    data.append(body)

for idx, frame in enumerate(data):
    update_sheet(SPREADSHEET_ID, frame, idx)