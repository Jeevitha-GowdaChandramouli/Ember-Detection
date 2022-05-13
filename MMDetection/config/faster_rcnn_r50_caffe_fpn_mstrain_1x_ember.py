# The new config inherits a base config to highlight the necessary modification
_base_ = '../faster_rcnn/faster_rcnn_r50_caffe_fpn_mstrain_1x_coco.py'

model = dict(
    backbone=dict(
        type = 'ResNet_mod',
        depth=18,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=False),
        norm_eval=True,
        style='caffe',
        init_cfg=dict(
            type='Pretrained',
            checkpoint='open-mmlab://detectron2/resnet50_caffe')),
    rpn_head=dict(
        type='RPNHead',
        in_channels=256,
        feat_channels=256,
        anchor_generator=dict(
            type='AnchorGenerator',
            scales = [8],
            ratios=[0.5, 1.0, 2.0],
            strides=[4, 8, 16, 32, 64]),
        loss_cls=dict(
            type='CrossEntropyLoss', use_sigmoid=True, loss_weight=1.0),
        loss_bbox=dict(type='L1Loss', loss_weight=1.0)),
    roi_head=dict(
        bbox_head=dict(num_classes=1),))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('__background__', 'ember')
data = dict(
    train=dict(
        img_prefix='data/EmberDetection/train2022/',
        classes=classes,
        ann_file='data/EmberDetection/annotations/ember_train_dataset.json'),
    val=dict(
        img_prefix='data/EmberDetection/val2022/',
        classes=classes,
        ann_file='data/EmberDetection/annotations/ember_val_dataset.json'),
    test=dict(
        img_prefix='data/EmberDetection/val2022/',
        classes=classes,
        ann_file='data/EmberDetection/annotations/ember_val_dataset.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
evaluation = dict(interval=12, metric='bbox')
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001)

checkpoint_config = dict(interval=1, by_epoch=False)

load_from = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
work_dir = './exps_filtersize_mod'
gpu_ids = [1]
