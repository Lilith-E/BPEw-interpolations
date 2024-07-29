import numpy as np
from scipy.spatial import distance

def calculate_rmse(gt_list, interpolated_list):
    """
    Calculates the Root Mean Squared Error (RMSE) between two lists of values.
    
    Parameters:
        gt_list (array-like): Ground truth values.
        interpolated_list (array-like): Interpolated values.
        
    Returns:
        float: RMSE value.
    """
    rmse = np.sqrt(np.mean((np.array(gt_list) - np.array(interpolated_list))**2))
    return rmse

def bhattacharyya_distance(p, q):
    """
    Calculates the Bhattacharyya distance between two probability distributions.
    
    Parameters:
        p (array-like): First probability distribution.
        q (array-like): Second probability distribution.
        
    Returns:
        float: Bhattacharyya distance.
    """
    p = np.array(p)
    q = np.array(q)
    
    if len(p) != len(q):
        raise ValueError("Distributions must have the same length.")
    
    p_nonzero = p + 1e-10
    q_nonzero = q + 1e-10
    
    bc = np.sum(np.sqrt(p_nonzero * q_nonzero))
    
    bd = -np.log(bc)
    
    return bd


def evaluation_metrics(gt_list, interpolated_list):
    """
    Calculates evaluation metrics between ground truth and interpolated values.
    
    Parameters:
        gt_list (array-like): Ground truth values.
        interpolated_list (array-like): Interpolated values.
        
    Returns:
        tuple: Euclidean distance, RMSE, Bhattacharyya distance, Cross entropy.
    """
    euclidean_dist = round(distance.euclidean(gt_list, interpolated_list), 3)
    rmse = calculate_rmse(gt_list, interpolated_list)
    
    # Normalize the lists
    gt_list = np.array(gt_list) / np.sum(gt_list)
    interpolated_list = np.array(interpolated_list) / np.sum(interpolated_list)
    
    bhattacharyya_dist = bhattacharyya_distance(gt_list, interpolated_list)
    
    return euclidean_dist, rmse, bhattacharyya_dist
