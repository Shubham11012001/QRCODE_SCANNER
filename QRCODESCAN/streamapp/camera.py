import cv2,os,urllib.request
import numpy as np
from django.http import HttpResponse
from django.conf import settings

class VideoCamera(object):
	instance_called = 0
	def __init__(self):
		self.video = cv2.VideoCapture(0)
	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
		detector = cv2.QRCodeDetector()
		data, bbox, _ = detector.detectAndDecode(image)
		if bbox is not None:
			if data:
				#print("[+] QR Code detected, data:",data)
				x = data
				print(str(x))
				return x
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		print("We are Here Man, Come up")
		print(type(jpeg.tobytes()))
		return jpeg.tobytes()
