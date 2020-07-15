from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse
from django.http import HttpResponse
import sys,time
from streamapp.camera import VideoCamera
# Create your views here.


def index(request):
	return render(request, 'streamapp/home.html')

class gene:
	def __init__(self):
		self.initial = 0

	def gen(self,request,camera):
		#print("I am testing calls")
		while True:
			#print("I am generator")
			frame = camera.get_frame()
			try:
				if type(frame) == str:
					print(frame)
					raise StopIteration()
			except StopIteration:
				return redirect('important')
			try:
				yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
			except TypeError:
				return redirect('important/')
			self.initial+=1	
		
				
		

def video_feed(request):
	x = gene()
	result = x.gen(request,VideoCamera())
	try:
		response01 = StreamingHttpResponse(result,content_type='multipart/x-mixed-replace; boundary=frame')
		return response01
	except Exception:
		return render(request,"streamapp/Check.html")
	
	


def important(request):
	return render(request,"streamapp/Check.html")

	