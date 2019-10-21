from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (500, 400)
camera.framerate = 10
# camera.annotate_text_size = 50
camera.start_preview()
# camera.annotate_text = "foobar"
sleep(5)
camera.capture('/home/pi/rpi/camera/foo.jpg')
camera.stop_preview()
