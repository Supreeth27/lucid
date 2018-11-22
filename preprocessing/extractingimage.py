import cv2
print(cv2.__version__)
#add the video file name 
vidcap = cv2.VideoCapture('DJI_0006.MP4')
success,image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print 'Read a new frame: ', success
  count += 1
