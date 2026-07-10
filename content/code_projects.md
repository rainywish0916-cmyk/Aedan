Title: Building a portfolio for jobs with Python
Date: 2026-07-08
Category: Projects
Summary: A collection of my projects from college and personal projects, as well as a journal of my college degree.

# My Project Collection

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Load data and split
data = pd.read_csv('dataset.csv')
X_train, X_text, y_train, y_test = train_test_split(X, y, test_size=0.2)
print("Data successfully split!")
```
