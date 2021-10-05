from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from tensorflow.keras.applications.inception_v3 import preprocess_input

def examine_ine(image,model,cat_list):
	img_array=img_to_array(image)
	img_dims = np.expand_dims(img_array,axis=0)
	preds=model.predict(preprocess_input(img_dims))
	preds_reshape = preds.reshape(-1,preds.shape[0])

	ine_array=np.array(ine_list).reshape(len(ine_list),-1)
	
	preds_sort=preds_reshape[np.argsort(preds_reshape[:,0])[::-1]]

	ine_sort = ine_array[np.argsort(preds_reshape[:,0])[::-1]]

	set_result=np.concatenate([ine_sort,preds_sort],1)

	return set_result[0:3,:]