import json
import os

nb_path = 'd:/OASIS/OIBSIP/jaskaran_Task4/notebook/Spam_Detection.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        if any("pd.read_csv" in line for line in source):
            # This is the cell that loads the dataset
            new_source = [
                "import os\n",
                "import sqlite3\n",
                "import pandas as pd\n",
                "from IPython.display import display\n",
                "if os.path.exists('dataset/spam_database.sqlite'):\n",
                "    base_dir = '.'\n",
                "elif os.path.exists('../dataset/spam_database.sqlite'):\n",
                "    base_dir = '..'\n",
                "else:\n",
                "    base_dir = None\n",
                "\n",
                "if base_dir is None:\n",
                "    print('Please ensure the SQLite database spam_database.sqlite is present in the dataset/ folder.')\n",
                "else:\n",
                "    db_path = os.path.join(base_dir, 'dataset', 'spam_database.sqlite')\n",
                "    # Connect to the SQLite database\n",
                "    conn = sqlite3.connect(db_path)\n",
                "    # Read the data using a SQL query\n",
                "    df = pd.read_sql('SELECT * FROM messages', conn)\n",
                "    conn.close()\n",
                "    \n",
                "    display(df.head())\n",
                "    display(df.info())\n",
                "    print('Null values:', df.isnull().sum())\n"
            ]
            cell['source'] = new_source
            break

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
