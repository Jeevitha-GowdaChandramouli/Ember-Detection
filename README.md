# Ember-Detection

## Objective
Reduce the impact of wildfire by detecting fire embers using computer vision and extinguishing them using water retardant bombs powered by drone technogolgies.

## Data
Train, test and validation split used for all the datasets: 70%, 15% and 15%


## Methodology
There were two approaches that were tried for detecting embers in images using MMDetection <br>
Approach 1 and 2: [Link](https://github.com/Jeevitha-GowdaChandramouli/Ember-Detection/tree/main/MMDetection)

(1) Approach 1: Vanilla FasterRCNN model from MMDetection <br>
Below shown are the plots for the various datasets for which Approach 1 was used:

<img width="461" alt="image" src="https://user-images.githubusercontent.com/98082950/168197156-7c43ae12-40ec-4a6c-8110-16872a3acf5b.png">

<img width="456" alt="image" src="https://user-images.githubusercontent.com/98082950/168197195-19c824df-b113-4dc5-b6e5-055b8821fffd.png">

<img width="519" alt="image" src="https://user-images.githubusercontent.com/98082950/168197209-0d187ad5-9b24-4d54-bcfc-e4f7b62d2684.png">
NOTE: med2 > med1 <br> <br>


(2) Approach 2: FasterRCNN with modified Anchor Generator Where the anchor scale was reduced from 8 to 4 (i.e. In config file (MMDetection), scales in rpn_head was changed from 8 to 4) <br>
    Motivation: Since the objects are very small, by reducing the anchor box size the model would perform better in detecting small objects

<img width="445" alt="image" src="https://user-images.githubusercontent.com/98082950/168197468-1fea8de5-cc01-4491-b3b3-aef89c300fe1.png">

Approach 2 was only tested for 0415_take2 and 0415_take1 datasets <br> <br>

(3) Approach 3 (Work in Progress): [Link](https://github.com/Jeevitha-GowdaChandramouli/Ember-Detection/blob/main/Ensemble_model/Ember_Detection.ipynb)

- Upstream: ResNet50 backbone followed by transpose convolution to increase width and height of feature map
- Downstream: Conv1 with kernel size (1x1) followed by non linearity
- Combing the models: Concatenate the outputs from Upstream and Downstream and pass it through FasterRCNN
- Motivation: Upstream path controls background suppression due to downscaling
			Downstream path enhances the small object detection due to the absence of downsampling
      
<img width="816" alt="image" src="https://user-images.githubusercontent.com/98082950/168198524-366cc5da-dc6d-4a1c-ad74-5a116932fc5d.png">

Output dimensions are in the format (batch_size, channels, width, height)

## Important MMDetection helper files that were created:

1. [Preprocessing_file](https://github.com/Jeevitha-GowdaChandramouli/Ember-Detection/blob/main/MMDetection/preprocessing_notebook.ipynb) for creating train, val, and test annotation files from the base annotation JSON file. This file also helps in splitting the dataset images into train, val, and test images.
2. Config files used are present in [Config](https://github.com/Jeevitha-GowdaChandramouli/Ember-Detection/tree/main/MMDetection/config) <br>
4. File to visualize the bounding boxes of the trained model: [Inference_file](https://github.com/Jeevitha-GowdaChandramouli/Ember-Detection/blob/main/MMDetection/inference.ipynb)

