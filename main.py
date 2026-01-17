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

        return (f.name, f.read())

def main(baseline: bool = False):
    if baseline:
        with open(f"{Path().home()}/baseline_pic_faceID.png", "wb") as f:
            f.write(take_picture()[1])

    else:
        pic = PIL.Image.open(take_picture()[0])
        base_pic = PIL.Image.open(f"Path().home()")
        for i in range(pic.size[0]):
            for j in range(pic.size[1]):
                pass






if __name__ == "__main__":
    main()
