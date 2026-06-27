import os
import cv2

output_dir = './clf-data/all_'
mask_path = './data/masked.jpg'
mask = cv2.imread(mask_path, 0)

analysis = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)

(totalLabels, labels_ids, values, centroid) = analysis

slots = []
for i in range(1, totalLabels):
    area = values[i, cv2.CC_STAT_AREA]

    x1 = values[i, cv2.CC_STAT_LEFT]
    y1 = values[i, cv2.CC_STAT_TOP]
    w = values[i, cv2.CC_STAT_WIDTH]
    h = values[i, cv2.CC_STAT_HEIGHT]

    pt1 = (x1, y1)
    pt2 = (x1+w, y1+h)
    (X, Y) = centroid[i]


    slots.append([x1, y1, w, h])

video_path = './data/parking_small.mp4'

cap = cv2.VideoCapture(video_path)

frame_nmr = 0 
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nmr)
ret, frame = cap.read()
while ret:

    cap.set(cv2.CAP_PROP_FRAME, frame_nmr)
    ret, frame = cap.read()

    if ret:
        for slot_nmr, slot in enumerate(slots):

            if slot_nmr in [132, 147, ]


                slot = frame[slot[1]:slot[1] + slot[3], slot[0]:slot[0] + slot[2], :]

                cv2.imwrite(os.path.join(output_dir, '{}_{}.jpg'.format(str(frame_nmr).zfill(8), str(slot_nmr).zfill(8))), slot)
        
        frame_nmr += 10


cap.release()

        
