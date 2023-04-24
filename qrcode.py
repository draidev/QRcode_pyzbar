import cv2 
from pyzbar.pyzbar import decode

if __name__=="__main__":
    #img = cv2.imread("qrcode_test.png")
    img = cv2.imread("qrcode_1.jpg")
#img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)

    qr = cv2.QRCodeDetector()
    data, box, straight_qrcode = qr.detectAndDecode(img)
    print("data : ",data)

    decoded = decode(img)
    print(decoded)
    for d in decoded:
        x, y, w, h = d.rect
        barcode_data = d.data.decode("utf-8")
        barcode_type = d.type
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
        print(barcode_data, barcode_type)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()