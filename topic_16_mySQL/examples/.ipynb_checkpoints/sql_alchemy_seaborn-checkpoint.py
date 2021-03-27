import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt


class SalaryViaSqlAlchemy:
    """
    Данная БД взята с сайта Kaggle
    https://www.kaggle.com/kaggle/sf-salaries
    """

    def __init__(self,
                 user='admin',
                 password='password',
                 host='127.0.0.1',
                 port='3306',
                 db_name='database'):

        try:
            self.engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}")

        except Exception as err:
            print(err)
            self.engine.dispose()

    def visualize_n_most_popular_job_titles(self, n=10):
        """
        Получить N самых популярных профессий (по количеству людей с данным JobTitle)
        :param n: число
        """
        df = pd.read_sql_query(f"SELECT JobTitle, COUNT(*) AS Num "
                               f"FROM Salaries " 
                               f"GROUP BY JobTitle "
                               f"ORDER BY Num DESC "
                               f"LIMIT {n}", self.engine)

        print(df.head(10))

        sns.set_theme(style="darkgrid")
        my_plot = sns.lineplot(x="JobTitle", y="Num", marker="o", data=df)
        my_plot.set_xticklabels(labels=df["JobTitle"], rotation=90)

        plt.show()


def main():
    my_db = SalaryViaSqlAlchemy()
    my_db.visualize_n_most_popular_job_titles(n=20)
    pass


if __name__ == '__main__':
    main()
