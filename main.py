import cv2 #type: ignore
import tempfile

def take_picture():
    cap = cv2.VideoCapture(0)
    for _ in range(15):
        frame = cap.read()[1]
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(cv2.imencode('.png', frame)[1])

    cap.release()

    return f.name

def main(baseline: bool = False):
    pass





if __name__ == "__main__":
    main()
