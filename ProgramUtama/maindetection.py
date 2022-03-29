# ِبِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيْم

import cv2
import mediapipe as mp
import numpy as np
import socket

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
ip = "192.168.100.169"
port = 2609
cap = cv2.VideoCapture(2)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


def kirimUDP(data):
    sock.sendto(data.encode('utf-8'), (ip, port))


def sudutBahuKanan(a,b,c):
    a = np.array(a) # Awal
    b = np.array(b) # Tengah
    c = np.array(c) # Akhir
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    sBahukanan = np.abs(radians*180.0/np.pi)
    
    if sBahukanan > 180.0:
        sBahukanan = 360-sBahukanan
        
    return sBahukanan 

def sudutBahuKiri(a,b,c):
    a = np.array(a) # Awal
    b = np.array(b) # Tengah
    c = np.array(c) # Akhir
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    sBahukiri = np.abs(radians*180.0/np.pi)
    
    if sBahukiri > 180.0:
        sBahukiri = 360-sBahukiri
        
    return sBahukiri

def sudutSikuKanan(a,b,c):
    a = np.array(a) # Awal
    b = np.array(b) # Tengah
    c = np.array(c) # Akhir
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    sSikukanan = np.abs(radians*180.0/np.pi)
    
    if sSikukanan > 180.0:
        sSikukanan = 360-sSikukanan
        
    return sSikukanan 

def sudutSikuKiri(a,b,c):
    a = np.array(a) # Awal
    b = np.array(b) # Tengah
    c = np.array(c) # Akhir
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    sSikuKiri = np.abs(radians*180.0/np.pi)
    
    if sSikuKiri > 180.0:
        sSikuKiri = 360-sSikuKiri
        
    return sSikuKiri 

## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            # Get koordinat kiri
            pinggulKiri = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            bahuKiri = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            sikuKiri = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            ptanganKiri = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            # Get koordinat kanan
            pinggulKanan = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            bahuKanan = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            sikuKanan = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            ptanganKanan = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

            # Kalkulasi untuk bahu kiri
            nilaiBahukiri = sudutBahuKiri(pinggulKiri, bahuKiri, sikuKiri)
            # Kalkulasi untuk bahu kanan
            nilaiBahukanan = sudutBahuKanan(pinggulKanan, bahuKanan, sikuKanan)
            # Kalkulasi siku kiri
            nilaSikukiri = sudutSikuKiri(bahuKiri, sikuKiri, ptanganKiri)
            # Kalkulasi siku kiri
            nilaSikukanan = sudutSikuKanan(bahuKanan, sikuKanan, ptanganKanan)

            
            # tampil kalkulasi bahu kiri
            cv2.putText(image, str(round(nilaiBahukiri)), 
                           tuple(np.multiply(bahuKiri, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
            # tampil kalkulasi bahu kanan
            cv2.putText(image, str(round(nilaiBahukanan)), 
                           tuple(np.multiply(bahuKanan, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )      

            # tampil kalkulasi siku kiri
            cv2.putText(image, str(round(nilaSikukiri)), 
                           tuple(np.multiply(sikuKiri, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
            # tampil kalkulasi siku kanan
            cv2.putText(image, str(round(nilaSikukanan)), 
                           tuple(np.multiply(sikuKanan, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                ) 
            # kirimUDP
            dataSemua = str(round(nilaiBahukiri)) +";" + str(round(nilaiBahukanan)) +";"+ str(round(nilaSikukiri)) + ";" + str(round(nilaSikukanan))
            kirimUDP(dataSemua)     

        except:
            pass
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        
        cv2.imshow('Nakula Gesture Remote', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()