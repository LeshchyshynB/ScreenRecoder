import pyautogui as pg
import numpy
import cv2
from config import *

class Screen_record:
	@classmethod
	def recording(self):
		print("Video recording start.\nPress \"q\" to stop.")
		cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
		cv2.resizeWindow("Live", 480, 270)
		while True:
			img = numpy.array(pg.screenshot(region=mon))
			rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			out.write(rgb_img)
			cv2.imshow('Live', rgb_img)
		    # Stop recording when we press 'q'
			if cv2.waitKey(1) == ord('q'):
				break
		out.release()
		print("\n-Video record succesfull.-\n:>",path)
		cv2.destroyAllWindows()

if __name__ == '__main__':
	Screen_record.recording()