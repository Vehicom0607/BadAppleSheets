import cv2

def create_cell(pixel):
    return {
        "userEnteredFormat": {
            "backgroundColor": {
                "red": str(pixel[0] / 255),
                "green": str(pixel[1] / 255),
                "blue": str(pixel[2] / 255)

            }
        }
    }


def create_request(row, col, img):
    image = cv2.resize(img, (col, row))
    rows = []
    for image_row in image:
        new_row = []
        for pixel in image_row:
            new_row.append(create_cell(pixel))
        rows.append({"values": new_row})
    body = {
        "requests": [
            {
                "updateCells": {
                    "range": {
                        "sheetId": 0,
                        "startRowIndex": 0,
                        "endRowIndex": row,
                        "startColumnIndex": 0,
                        "endColumnIndex": col
                    },
                    "rows": rows,
                    "fields": "userEnteredFormat.backgroundColor"
                }
            }
        ]
    }
    return body
