# Ember-Detection
Ember Detection and Tracking: <br>

There were two approaches that were tried for detecting embers in images <br>
(1) Approach 1: Vanilla FasterRCNN model from MMDetection <br>
(2) Approach 2: FasterRCNN with modified Anchor Generator Where the anchor scale was reduced from 8 to 4 (i.e. update the config file scales in rpn_head was changed from 8 to 4)


