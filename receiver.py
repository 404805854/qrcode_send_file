import cv2
import pyzbar.pyzbar as pyzbar
import argparse
import base64


def parse_args():
    parser = argparse.ArgumentParser(description="QR code receiver")
    parser.add_argument("-f", "--file",
                        required=True, help="Audio File")

    args, _ = parser.parse_known_args()
    return args


def main():
    args = parse_args()
    cap = cv2.VideoCapture(args.file)

    filename = ""
    ofile = None
    last = ""

    while (1):
        hasFrame, inputImage = cap.read()
        if not hasFrame:
            break
        decodedObjects = pyzbar.decode(inputImage)
        if len(decodedObjects):
            zbarData = decodedObjects[0].data
            if filename == "":
                filename = zbarData
                ofile = open(filename, "wb")
                last = filename
            elif zbarData != "":
                if last != zbarData:
                    last = zbarData
                    buffer = base64.b64decode(zbarData)
                    ofile.write(buffer)

    cv2.destroyAllWindows()
    if ofile:
        ofile.close()


if __name__ == "__main__":
    main()
