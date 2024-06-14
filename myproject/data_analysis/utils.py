import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def handle_uploaded_file(file):
    df = pd.read_csv(file)
    
    # Data analysis
    head = df.head().to_html()
    desc = df.describe().to_html()
    missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html()
    
    # Data visualization
    img = BytesIO()
    plt.figure(figsize=(10, 6))
    sns.histplot(df.select_dtypes(include=[np.number]).dropna(), kde=True)
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    
    data = {
        'head': head,
        'desc': desc,
        'missing_values': missing_values,
        'plot_url': plot_url,
    }
    return data
