import seaborn as sns; sns.set(color_codes=True)
import pandas as pd
import matplotlib.pyplot as plt


#cols and rows
def normal(saveas,metric,link, df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric, method = link,robust = False, yticklabels = species, cmap = 'coolwarm')
    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'_normal.png', dpi = 800)
    plt.clf()
    plt.close()
    plt.show()
def robust(saveas,metric,link, df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric,method = link,robust = True, yticklabels = species, cmap = 'coolwarm')
    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'_robust.png', dpi = 800)
    plt.clf()
    plt.close()    
def z_normal(saveas,metric,link, df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric,method = link,robust = False, z_score = True, yticklabels = species, cmap = 'coolwarm')
    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'_z-normal.png', dpi = 800)
    plt.clf()
    plt.close()
def z_robust(saveas,metric, link,df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric,method = link,robust = True, z_score = True, yticklabels = species, cmap = 'coolwarm')
    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'z-robust.png', dpi = 800)
    plt.clf()
    plt.close()
#rows
def normal_rows(saveas,metric, link,df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric,method = link,row_cluster = True, col_cluster= False,robust = False, yticklabels = species, cmap = 'coolwarm')
    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'_normal_rows.png', dpi = 800)
    plt.clf()
    plt.close()
def robust_rows(saveas,metric, link,df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric,method = link,row_cluster = True, col_cluster= False,robust = True, yticklabels = species, cmap = 'coolwarm')
    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'_robust_rows.png', dpi = 800)
    plt.clf()
    plt.close()
def z_normal_rows(saveas,metric,link, df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric,method = link,row_cluster = True, col_cluster= False,robust = False, z_score = True, yticklabels = species, cmap = 'coolwarm')
    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'_z-normal_rows.png', dpi = 800)
    plt.clf()
    plt.close()
def z_robust_rows(saveas,metric, link,df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric,method = link,row_cluster = True, col_cluster= False,robust = True, z_score = True, yticklabels = species, cmap = 'coolwarm')
    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'z-robust_rows.png', dpi = 800)
    plt.clf()
    plt.close()
#cols
def normal_cols(saveas,metric, link,df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric,method = link,row_cluster = False, col_cluster= True,robust = False, yticklabels = species, cmap = 'coolwarm')
    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'_normal_cols.png', dpi = 800)
    plt.clf()
    plt.close()
def robust_cols(saveas,metric,link, df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric,method = link,row_cluster = False, col_cluster= True,robust = True, yticklabels = species, cmap = 'coolwarm')
    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'_robust_cols.png', dpi = 800)
    plt.clf()
    plt.close()
def z_normal_cols(saveas,metric,link, df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric,method = link,row_cluster = False, col_cluster= True,robust = False, z_score = True, yticklabels = species, cmap = 'coolwarm')
    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'_z-normal_cols.png', dpi = 800)
    plt.clf()
    plt.close()
def z_robust_cols(saveas,metric,link, df, species):
    sns.set(font_scale=0.25) 
    g = sns.clustermap(df,metric = metric,method = link,row_cluster = False, col_cluster= True,robust = True, z_score = True, yticklabels = species, cmap = 'coolwarm')
##    #plt.tight_layout()
    plt.savefig(saveas+'_'+metric+'_'+link+'z-robust_cols_nt.png', dpi = 800)
    plt.clf()
    plt.close()
#make all these graphs
def make_all_cluster(saveas,metric,link, df, species):
    print(metric+' : '+link)
    print(1)
    normal(saveas,metric,link,df,species)
    print(2)
    robust(saveas,metric,link,df,species)
    print(3)
    z_normal(saveas,metric,link,df,species)
    print(4)
    z_robust(saveas,metric,link,df,species)
    print(5)
    normal_rows(saveas,metric,link,df,species)
    print(6)
    robust_rows(saveas,metric,link,df,species)
    print(7)
    z_normal_rows(saveas,metric,link,df,species)
    print(8)
    z_robust_rows(saveas,metric,link,df,species)
    print(9)
    normal_cols(saveas,metric,link,df,species)
    print(10)
    robust_cols(saveas,metric,link,df,species)
    print(11)
    z_normal_cols(saveas,metric,link,df,species)
    print(12)
    z_robust_cols(saveas,metric,link,df,species)
df = pd.read_excel('2019.05.23-PMC-Safety-01.xlsx', sheet_name = 'Corrilation_Matrix_Ratios_Genus')
species = df.pop("Species")
##saveas='20190527-safety'
##metrics = [
####        'braycurtis',
####	'canberra',
####	'chebyshev', #incomplete
####	'cityblock',
####	'correlation', 
####	'cosine',
####	'dice',
####	'euclidean', 
####	'hamming' ,
####	'jaccard',
######	'jensenshannon', #incomplete
######	'kulsinski',#incomplete
######	'mahalanobis',#incomplete 
####	'matching',
####	'minkowski', #incomplete
##	'rogerstanimoto', 
##	'russellrao',
##	'seuclidean',
##	'sokalmichener' ,
##	'sokalsneath',
##	'sqeuclidean',
##	'yule'#incomplete
##]
##linkage = [
##    	'single',# (default)
##	'complete',
##	'average',
##	'weighted',
##	'centroid',
##	'median',
##	'ward'
##    ]
##for metric in metrics:
##    for link in linkage:
##
z_robust('20190606_Safety_Corrilation_Average_Z_Score_Robust','correlation','average',df,species)
