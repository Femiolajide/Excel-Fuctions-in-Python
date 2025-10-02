import pandas as pd
def excel_sum(*numbers: list | tuple | pd.DataFrame | pd.Series) -> int | float:
    """**Excel**
    Add all the numbers in a range of ceels
    
**Python**
    Add all the numbers in a container (by container, 
    I mean data structure like list, tuple, dataframe,
    and series) as a representation of range of cells
    
**Parameters**
    -------------------------------------------------------------
        **numbers**: int, float, list, tuple, pandas serues or datafram
        
        number1,number2....(number to sum is not limited unlike excel's
        that allows only from 1 to 255). Logical values and texts are 
        ignored in containers (list, tuple, series and dataframe), but
        included if typed as arguments.
**Returns**
    -------------------------------------------------------------
        **int or float**
        
**Raises**
    -------------------------------------------------------------
        **TypeError**
        Raises TypeError if the arguments contain unrecognized string

**Note**
    -------------------------------------------------------------
        This is purely logical representation of how sum function behaves 
        in excel.
    """
    # importing the required packages
    import numpy as np
    import pandas as pd 
    # Separating the parameters into different data structure/type
    num_text = [] # append if type is str, int or float
    from_cont = [] # unpack all the elements in list or tuple into this
    from_pandas = [] # unpack all the elements in dataframe or series into this
    for x in numbers:
        if isinstance(x,(str,float,int)):
            num_text.append(x)
        elif isinstance(x,(tuple,list)):
            from_cont.extend(x)
        elif isinstance(x,(pd.DataFrame,pd.Series)):
            # Trying to do some cleanup here
            # Replacing all logical values (True or False) with 0
            no_logicals = x.map(lambda x: 0 if x == True or x == False
                                else x)
            # Converting the outcome to numpy then to list 
            no_logicals = no_logicals.to_numpy()
            # An attempt to reshape dataframe to (n,) form
            no_logicals = no_logicals.flatten()
            # Converting numpy to list 
            no_logicals = list(no_logicals)
            # unpacking the contents into from_pandas 
            from_pandas.extend(no_logicals)
        else:
            # Let the users know that their datatype is not allowed
            raise TypeError ("#VALUE?\nA value used in this function\
 is of wrong data type")
    # Trying to do some cleanup here also
    # Replacing all logical values (True or False) in from_cont with 0
    from_cont = [0 if x == True or x == False else x for x in from_cont]
    # Joining from_cont and from_pandas together 
    container = from_cont + from_pandas
    # An attempt to exclude all unrecognized text in container
    clean_cont = []
    for x in container:
        try:
            clean_cont.append(float(x))
        except ValueError:
            pass 
    # Joining clean_cont and num_text together 
    all_nums = clean_cont + num_text
    # An attempt to cast all string-like numbers in all_nums to float
    clean_all_nums = []
    for x in all_nums:
        try:
            clean_all_nums.append(float(x))
        except ValueError:
            clean_all_nums.append(x)
    # Error handling and finalizing the answer
    if all([isinstance(x,(int,float)) for x in clean_all_nums]):
        if sum(clean_all_nums) == int(sum(clean_all_nums)):
            return int(sum(clean_all_nums))
        else:
            return sum(clean_all_nums)
    else:
        raise TypeError ("#VALUE?\nA value used in this function\
 is of wrong data type")
        







    
