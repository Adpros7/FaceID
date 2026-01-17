from pathlib import Path
import cv2 #type: ignore
import tempfile

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
        with open(Path().home(), "wb") as f:
            f.write(take_picture()[1])

    else:

        pic = take_picture()[1]
        






if __name__ == "__main__":
    main()
