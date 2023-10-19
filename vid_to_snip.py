import cv2


video_capture = cv2.VideoCapture("vid2m.mp4")


frame_counter = 0


capture_interval = 1  


fps = int(video_capture.get(cv2.CAP_PROP_FPS))

while True:
    
    ret, frame = video_capture.read()

    if not ret:
        break

    
    frame_counter += 1

    
    if frame_counter % (fps * capture_interval) == 0:
       
        filename = f"frame_{frame_counter // (fps * capture_interval)}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Captured {filename}")


video_capture.release()
cv2.destroyAllWindows()
