import qrcode
import argparse
import base64

MAX_QRCODE_CONTENT_LEN = 1000


def parse_args():
    parser = argparse.ArgumentParser(description="QR code senders")
    parser.add_argument("-f", "--file",
                        required=True, help="File to be send")

    args, _ = parser.parse_known_args()
    return args


def create_image(data):
    qr = qrcode.QRCode()
    qr.add_data(data)
    img = qr.make_image()
    img.show()


def main():
    args = parse_args()

    with open(args.file, "rb") as ifile:
        create_image(args.file)
        while True:
            buffer = ifile.read(MAX_QRCODE_CONTENT_LEN)
            data = base64.b64encode(buffer)
            create_image(data)
            if len(buffer) != MAX_QRCODE_CONTENT_LEN:
                break


if __name__ == "__main__":
    main()
