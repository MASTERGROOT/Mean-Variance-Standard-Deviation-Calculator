import numpy as np

def calculate(list):
    if len(list) < 9 :
        raise ValueError("List must contain nine numbers.")
    else:
        matrix = np.array(list).reshape(3,3)
        
        mean = [matrix.mean(axis=0).tolist(),matrix.mean(axis=1).tolist(),matrix.mean().tolist()]
        
        var = [matrix.var(axis=0).tolist(),matrix.var(axis=1).tolist(),matrix.var().tolist()]
        
        std = [matrix.std(axis=0).tolist(),matrix.std(axis=1).tolist(),matrix.std().tolist()]
        
        Max = [matrix.max(axis=0).tolist(),matrix.max(axis=1).tolist(),matrix.max().tolist()]
        
        Min = [matrix.min(axis=0).tolist(),matrix.min(axis=1).tolist(),matrix.min().tolist()]
        
        Sum = [matrix.sum(axis=0).tolist(),matrix.sum(axis=1).tolist(),matrix.sum().tolist()]
        
        result = {
            'mean' : mean,
            "variance" : var,
            'standard deviation' : std,
            'max' : Max,
            'min' : Min,
            'sum' : Sum 
        }
        return result
        
        
