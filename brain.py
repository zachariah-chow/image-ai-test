from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsSqueezeNet()
prediction.setModelPath(os.path.join(
    execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()
