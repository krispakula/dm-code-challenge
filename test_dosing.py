import dosing
import pandas as pd
import dosing 
import unittest
import params


# read the csv files
df_ec = pd.read_csv("t2_ec 20190619.csv")
df_registry = pd.read_csv("t2_registry 20190619.csv")

class Testing(unittest.TestCase):

    # test filter_records function
    def test_filter_records(self):
        df = dosing.merge_dataframes(df_registry, df_ec, 'RID', 'VISCODE')

        assert dosing.filter_records(df,  'w02', "Y", "Y" ).SVSTDT[7] == '8/9/18'
        assert dosing.filter_records(df, 'w02', "Y" , "Y").USERID_x[7] == 'BBAGGINS_UCSD_EDU_2'

    def test_merge_dataframes(self):
        assert dosing.merge_dataframes(df_registry, df_ec, 'RID', 'VISCODE').SVSTDT[7] == '8/9/18'
        assert dosing.merge_dataframes(df_ec, df_registry,'RID', 'VISCODE').SVRESCRN[7] == '-4'

if __name__ == '__main__':

    unittest.main()
