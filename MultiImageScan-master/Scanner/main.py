import argparse
import logging
import cv2
from Scanner import processImage


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-b', '--debug', dest='debug', action='store_true', help='enable debug logging')
    parser.add_argument('-t', '--thresh', dest='thresh', default=0.5, type=float, help='threshold for mask')
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    
    logger = logging.getLogger("main")
    
    image = cv2.imread("Receipt4.jpg")

    img = processImage(image)

    cv2.imwrite("contoured.jpg", img)

    