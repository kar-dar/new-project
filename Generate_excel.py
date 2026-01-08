import pandas as pd
from Paths_Connections import github_data
from Utility import Postgres
import new_queries

# GitHub credentials
github_organization = github_data.get('org')
github_token = github_data.get('token')

def Generate_Reconciliation_Sheet(tfs_collection, tfs_project):

    # Update Sheet with all details
    db_obj = Postgres.PostgresCls()
    db_obj.db_connect()

    query3 = new_queries.Genearte_Excel_from_git
    db_obj.cursor.execute(query3, (tfs_collection, tfs_project, tfs_collection, tfs_project, tfs_collection, tfs_project,tfs_collection, tfs_project, tfs_project))

    result = db_obj.cursor.fetchall()
    column = [desc[0] for desc in db_obj.cursor.description]
    df = pd.DataFrame(result, columns=column)
    print(df)
    db_obj.db_disconnect()
    df.to_excel(f"C:\\Users\\Darshan.K\\OneDrive - Nabors\\Desktop\\Migration_default\\{tfs_collection}-{tfs_project}-sprint5.xlsx", index=False)