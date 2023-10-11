import numpy as np
import os
import glob


def pred_to_label(outputs_classifier, outputs_regressor):
	"""Convert output model to label. Get aspects have reliability >= 0.5

	Args:
		outputs_classifier (numpy.array): Output classifier layer
		outputs_regressor (numpy.array): Output regressor layer

	Returns:
		predicted label
	"""
	result = np.zeros((outputs_classifier.shape[0], 6))
	mask = (outputs_classifier >= 0.5)
	result[mask] = outputs_regressor[mask]
	return result



def get_proj_path():
    A_dir = os.path.dirname(os.getcwd())
    return A_dir



def save_split_dir(prep_train_df, prep_test_df):
    A_dir = get_proj_path()
    save_dir = os.path.join(A_dir, 'datasets', 'data_split')
    train_dir = os.path.join(save_dir, r"trainset.csv")
    test_dir = os.path.join(save_dir, r"testset.csv")

    prep_train_df.to_csv(train_dir)
    prep_test_df.to_csv(test_dir)



def get_train_dev_path():
    A_dir = get_proj_path()
    trainset_dir = os.path.join(A_dir, "datasets", "data_split", "trainset.csv")
    devset_dir = os.path.join(A_dir, "datasets", "data_split", "testset.csv") 
    return trainset_dir, devset_dir



def get_test_path():
    A_dir = get_proj_path()
    testset_path = os.path.join(A_dir, "datasets", "private_test", "chall_02_private_test.csv")
    return testset_path



def get_weight_path():
    weights_dir = r'/content/drive/MyDrive/Review_analysis_training/Review_analysis_DreamTim/A/weights'
    
    # Get a list of all files in the "weights" directory with the appropriate filename format (e.g. *.h5 if you use Keras)
    weight_files = glob.glob(os.path.join(weights_dir, '*.pt'))

    if not weight_files:
        return None

    # Sort the list of files by date modified from new to old
    weight_files.sort(key=os.path.getmtime, reverse=True)

    # Get the latest weight file
    latest_weight_path = weight_files[0]

    return latest_weight_path
