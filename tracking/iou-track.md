# IOU track

ref: 

    High-Speed Tracking-by-Detection Without Using Image Information

With ever increasing performances of object detectors, the basis for a tracker becomes much more reliable.

Both high precision detections and the usage of video footage with high frame rates can greatly simplify the tracking task.

This method is based on the assumption that the detector produces a detection per frame for every object to be tracking, i.e. there are none or only few gaps in the detections. Furthermore, they assume that detections of an object in consecutive frames have an unmistakably high overlap IOU.

**If both requirements are met, tracking becomes trivial and can be done even without using image information.**