import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pytest
import params 
from optparse import OptionParser

df_ec = pd.read_csv("t2_ec 20190619.csv")
df_registry = pd.read_csv("t2_registry 20190619.csv")
df_registry = df_registry[ df_registry.SVPERF == 'Y' ]
df_registry = df_registry[ df_registry.VISCODE != 'bl' ]

def draw_pie(df_ec, df_registry):
   fig = go.Figure(go.Pie(
      name = "",
      labels = df_registry.VISCODE,
      hovertemplate = "Viscode: <B>%{label}</B><br><B>Count: %{value} (%{percent}) </B>",
      title = dict(text="Viscodes from Registry", font=dict(size=20), position="top left") 
   ))
   fig.show()
   return

# Read CSV files
def csv_report():
   df_ec = pd.read_csv("t2_ec 20190619.csv")
   df_registry = pd.read_csv("t2_registry 20190619.csv")
   return df_ec, df_registry

# Merge dataframes on RID and VISCODE
def merge_dataframes(df_ec, df_registry, rid='RID', viscode='VISCODE'):
   df_merge = pd.merge(df_registry, df_ec, on = ['RID','VISCODE'], how='outer', indicator=True) 
   return df_merge

# Filter records
def filter_records(df, viscode, svdose, ecsdstxt):
   df_filtered = df[ df_merge.VISCODE == viscode ]
   df_filtered = df_filtered[ df_filtered.SVDOSE == svdose ]
   df_filtered = df_filtered[ df_filtered.ECSDSTXT != ecsdstxt ]
   print(df_filtered)
   return df_filtered

# Create CSV file 
def create_csv_file(df, options):
   df_csv = df[['ID_x','RID','USERID_x','VISCODE','SVDOSE','ECSDSTXT']]
   print(df_csv) 
   csv = df_csv.to_csv(options.results, index=False, header=False) 
   print(csv) 

if __name__ == "__main__":

   parser = OptionParser()
   parser.add_option('', '--viscode',  dest='viscode',  default='w02', help='Viscode parameter') 
   parser.add_option('', '--rid',      dest='rid',      default='RID', help='Rid parameter') 
   parser.add_option('', '--svdose',   dest='svdose',   default='Y', help='Svdose parameter') 
   parser.add_option('', '--ecsdstxt', dest='ecsdstxt', default='180', help='Ecsdstxt parameter') 
   parser.add_option('', '--results',  dest='results',  default='results.csv', help='results directory parameter') 
   options = parser.parse_args()[0]

   draw_pie(df_ec, df_registry)
   df_merge = merge_dataframes(df_ec, df_registry, options.rid, options.viscode)
   df_filtered = filter_records(df_merge,  options.viscode, options.svdose, options.ecsdstxt)
   create_csv_file(df_filtered, options) 

