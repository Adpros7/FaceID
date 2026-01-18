from email.mime import base
from pathlib import Path
import PIL.Image
import cv2 #type: ignore
import tempfile
import PIL

def take_picture():
    cap = cv2.VideoCapture(0)
    for _ in range(15):
        frame = cap.read()[1]
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(cv2.imencode('.png', frame)[1])

        cap.release()

        return (f.name, cv2.imencode('.png', frame)[1])

def main(baseline: bool = False):
    if baseline:
        with open(f"{Path().home()}/baseline_pic_faceID.png", "wb") as f:
            f.write(take_picture()[1])

    else:
        base_pic = PIL.Image.open(Path().home() / "baseline_pic_faceID.png")
        pic = PIL.Image.open(take_picture()[0]).resize(base_pic.size)
        average = [0, 0]
        for i in range(pic.size[0]):
            for j in range(pic.size[1]):

                if all(abs(x - y) <= 10 for x, y in zip(base_pic.getpixel((i, j)), pic.getpixel((i, j)))): # type: ignore
                    average[0] += 1
                average[1] += 1

        if average[0] / average[1] > 75:
            print("Face detected")
        else:
            print("Face not detected")


if __name__ == "__main__":
    main()
