from email.mime import base
from pathlib import Path
import time
import PIL.Image
import PIL.ImageDraw
import cv2  # type: ignore
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
    coords_blackout = []
    if baseline:
        print("Please get out of frame for baseline pic. Be back in 5 seconds.")
        with open(f"{Path().home()}/baseline_pic_faceID_no_human.png", "wb") as f:
            f.write(take_picture()[1])

        print("Be in the frame for next picture.")
        for i in range(10, 0, -1):
            print(i)
            time.sleep(1)
        print("Taking picture...")
        with open(f"{Path().home()}/baseline_pic_faceID.png", "wb") as f:
            f.write(take_picture()[1])
        print("Done")
        baseline_pic_no_human = PIL.Image.open(
            f"{Path().home()}/baseline_pic_faceID_no_human.png")
        baseline_pic_with_human = PIL.Image.open(
            f"{Path().home()}/baseline_pic_faceID.png")
        baseline_pic_no_human.resize(baseline_pic_with_human.size)
        for i in range(baseline_pic_with_human.size[0]):
            for j in range(baseline_pic_with_human.size[1]):
                if all(abs(x - y) <= 7 for x, y in zip(baseline_pic_no_human.getpixel((i, j)), baseline_pic_with_human.getpixel((i, j)))):  # type: ignore
                    PIL.ImageDraw.Draw(baseline_pic_with_human).point((i, j), (0, 0, 0))
                    coords_blackout.append((i, j))

    else:
        base_pic = PIL.Image.open(Path().home() / "baseline_pic_faceID.png")
        pic = PIL.Image.open(take_picture()[0]).resize(base_pic.size)
        for x, y in coords_blackout:
            PIL.ImageDraw.Draw(pic).point((x, y), (0, 0, 0))
        average = [0, 0]
        for i in range(pic.size[0]):
            for j in range(pic.size[1]):

                if all(abs(x - y) <= 10 for x, y in zip(base_pic.getpixel((i, j)), pic.getpixel((i, j)))):  # type: ignore
                    average[0] += 1
                average[1] += 1

        print(average[0] / average[1] * 100)
        if average[0] / average[1] * 100 > 67:
            print("Face detected")
        else:
            print("Face not detected")


if __name__ == "__main__":
    main()
