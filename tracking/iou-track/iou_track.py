import numpy as np
from time import time

def load_detection(filename):
    data = []
    raw_detections = np.genfromtxt(filename, delimiter=',', dtype=np.float32)
    end_frame = int(np.max(raw_detections[:,0]))
    for i in range(1, end_frame+1):
        # extract detection from each frame
        idx = raw_detections[:,0] == i
        bbox = raw_detections[idx, 2:6]
        bbox[:,2:4] += bbox[:,0:2] # x1,y1,w,h --> x1,y1,x2,y2
        scores = raw_detections[idx,6]
        dets = []
        for bb, s in zip(bbox, scores):
            dets.append({'bbox':(bb[0], bb[1], bb[2], bb[3]), 'score':s})
        data.append(dets)

    return data

def iou(bbox1, bbox2):
    bbox1 = [float(x) for x in bbox1]
    bbox2 = [float(x) for x in bbox2]
    (x0_1, y0_1, x1_1, y1_1) = bbox1
    (x0_2, y0_2, x1_2, y1_2) = bbox2

    overlap_x0 = max(x0_1, x0_2)
    overlap_y0 = max(y0_1, y0_2)
    overlap_x1 = max(x1_1, x1_2)
    overlap_y1 = max(y1_1, y1_2)

    # check if there  is an overlap
    if overlap_x1 - overlap_x0 <=0 or overlap_y1 - overlap_y0 <=0:
        return 0

    size_1 = (x1_1 - x0_1) * (y1_1 - y0_1)
    size_2 = (x1_2 - x0_2) * (y1_2 - y0_2)
    size_intersection = (overlap_x1 - overlap_x0) * (overlap_y1 - overlap_y0)
    size_union = size_1 + size_2 - size_intersection
    if size_union == 0:
        return 0
    return size_intersection / size_union




def track_iou(detections, sigma_l, sigma_h, sigma_iou, t_min):
    # See "High-Speed Tracking-by-Detection Without Using Image Information by E. Bochinski, V. Eiselein, T. Sikora" for more information.

    tracks_active = [] # track active T_a
    track_finised = [] # T_f
    for frame_num, detections_frame in enumerate(detections, start=-1):
        # step1: filter the low threshold detections
        dets = [det for det in detections_frame if det['score'] >= sigma_l]

        updated_tracks = []
        # for each active tracks
        for track in tracks_active:
            if len(dets) > 0:
                best_match = max(dets, key = lambda x: iou(track['bboxes'][-1], x['bbox']))
                # if the best match is greather than threshold
                if iou(track['bboxes'][-1], best_match['bbox']) >= sigma_iou:
                    # append it to current active track
                    track['bboxes'].append(best_match['bbox'])
                    track['max_score'] = max(track['max_score'], best_match['score'])

                    updated_tracks.append(track)
                    # remove from best matching detection from detections
                    del dets[dets.index(best_match)]

            if len(updated_tracks) == 0 or track is not updated_tracks[-1]:
                # doest not update for current track, finish it
                if track['max_score'] >= sigma_h and len(track['bboxes']) >= t_min:
                    track_finised.append(track)

        # if still has detections,then create new tracks
        new_tracks = [{'bboxes': [det['bbox']], 'max_score': det['score'], 'start_frame': frame_num} for det in dets]
        tracks_active = updated_tracks + new_tracks

    # finished ,and  return all finished tracks and active track with meet some conditions
    track_finised += [track for track in tracks_active
                        if track['max_score'] >= sigma_h and len(track['bboxes']) >= t_min]

    return track_finised









if __name__ == '__main__':
    detections = load_detection('gt.txt')
    # just for tested, the parameters can ref the paper
    sigma_l = -0.5
    sigma_h = 0.5
    sigma_iou = 0.4
    t_min = 4
    start = time()
    tracks = track_iou(detections, sigma_l, sigma_h, sigma_iou, t_min)
    end = time()

    num_frames = len(detections)
    print("finished at " + str(int(num_frames / (end - start))) + " fps!")


