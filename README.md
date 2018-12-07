# Semantic Image Segmentation using Deeplab on Custom Image Dataset

## 1.Introduction

The major goal of Semantic Image Segmentation is to label each pixel in an image to a corresponding class of what it is representing. We were given a task to classify all pixels in an image of a building surface as Brick, Wall and Window.

Using transfer learning was the best practical approach towards this problem. You can find out more about Deeplab on this post http://liangchiehchen.com/projects/DeepLab.html

## 2. Steps

1. First we collect our Image data and label it. We used Labelme to create JSON annotations on our image data. Labelme is a graphical image annotation tool inspired by http://labelme.csail.mit.edu. You can clone their repository from <a href="https://github.com/wkentaro/labelme">here</a>
We use the instructions on <a href="https://github.com/wkentaro/labelme/tree/master/examples/semantic_segmentation">this</a> page to convert our annotations to a Pascal VOC like dataset.

2. Clone Deeplab and follow their installation instructions form <a href="https://github.com/tensorflow/models/tree/master/research/deeplab">here</a>

3. Convert your VOC like dataset to TfRecord for input to Deeplab. This is can be done by running the build_lucid_data.py script. Follow the instrucions on <a href="http://hellodfan.com/2018/07/06/DeepLabv3-with-own-dataset/">this</a> page if you would like more details or run into issues.

4. Download the model checkpoint of the model you would like to use for training it on your own data. We used the Xception_65 checkpoint for our data and placed it in the ./xception_65/ directory.

5. Train your model by running the command included in train_command.txt

6. Visualize your model's performance by running the visualization_command.txt from your terminal. The visualizations will be stored in the ./vis directory for our example.

![](final.gif)

## References

[1] Semantic Image Segmentation with Deep Convolutional Nets and Fully
Connected CRFs Liang-Chieh Chen+, George Papandreou+, Iasonas Kokkinos, Kevin
Murphy, Alan L. Yuille In ICLR, 2015.

[2]. B. C. Russell, A. Torralba, K. P. Murphy, W. T. Freeman. LabelMe: a Database and
Web-based Tool for Image Annotation. International Journal of Computer Vision,
77(1-3):157-173, 2008

[3]. "Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected
CRFs"

[4]. Rethinking Atrous Convolution for Semantic Image Segmentation Liang-Chieh
Chen, George Papandreou, Florian Schroff, Hartwig Adam. arXiv: 1706.05587, 2017

[5]. Encoder-Decoder with Atrous Separable Convolution for Semantic Image
Segmentation Liang-Chieh Chen, Yukun Zhu, George Papandreou, Florian Schroff,
Hartwig Adam. [link]. In ECCV, 2018

[6]. ParseNet: Looking Wider to See Better Wei Liu, Andrew Rabinovich, Alexander C
Berg arXiv:1506.04579, 2015
