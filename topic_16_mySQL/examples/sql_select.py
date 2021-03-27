import mysql.connector
from mysql.connector import errorcode


class MyDB:
    """
    Данная БД взята с сайта Kaggle
    https://www.kaggle.com/kaggle/sf-salaries
    """

    def __init__(self,
                 user='admin',
                 password='password',
                 host='127.0.0.1',
                 database='database'):

        try:
            self.my_db = mysql.connector.connect(user=user,
                                                 password=password,
                                                 host=host,
                                                 database=database)
            self.my_cursor = self.my_db.cursor()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                self.my_db.close()

    def __del__(self):
        self.my_db.close()

    def get_select_all_from_table(self, table='Salaries'):
        """
        Получить все записи таблицы
        :param table: название таблицы
        :return: все записи из таблицы
        """
        self.my_cursor.execute(f"SELECT * FROM {table}")

        field_names = [i[0] for i in self.my_cursor.description]
        return field_names, self.my_cursor.fetchall()

    def unique_job_title_number(self):
        """
        Сколько уникальных должностей (JobTitle) в таблице Salaries?
        :return: количество уникальных должностей
        """
        self.my_cursor.execute("SELECT COUNT(DISTINCT JobTitle) "
                               "FROM Salaries")

        field_names = [i[0] for i in self.my_cursor.description]
        return field_names, self.my_cursor.fetchall()

    def get_unique_job_titles(self):
        """
        Получить список уникальных должностей (JobTitle) в таблице Salaries
        :return: список уникальных должностей
        """
        self.my_cursor.execute("SELECT DISTINCT JobTitle "
                               "FROM Salaries")

        field_names = [i[0] for i in self.my_cursor.description]
        return field_names, self.my_cursor.fetchall()

    def get_n_people_with_max_total_pay(self, n=10):
        """
        Получить список N имен (EmployeeName), доход (TotalPay) и должнось (JobTitle) людей с самым большим доходом (TotalPay)
        :return: список имен (EmployeeName), доход (TotalPay) и должнось (JobTitle)
        """
        self.my_cursor.execute(f"SELECT EmployeeName, TotalPay, JobTitle "
                               f"FROM Salaries "
                               f"ORDER BY TotalPay DESC "
                               f"LIMIT {n}")

        field_names = [i[0] for i in self.my_cursor.description]
        return field_names, self.my_cursor.fetchall()

    def get_max_base_pay(self):
        """
        Получить максимальную базовую оплату (BasePay)
        :return: максимальная базовая оплата
        """
        self.my_cursor.execute("SELECT BasePay "
                               "FROM Salaries "
                               "ORDER BY BasePay DESC "
                               "LIMIT 1")

        field_names = [i[0] for i in self.my_cursor.description]
        return field_names, self.my_cursor.fetchall()

    def get_job_title_number_with_word(self, word):
        """
        Получить количество должностей содержащих слово word
        :param word: слово для шаблона поиска
        :return: количество должностей содержащих слово word
        """
        self.my_cursor.execute(f"SELECT COUNT(JobTitle) "
                               f"FROM Salaries "
                               f"WHERE JobTitle LIKE '%{word}%'")

        field_names = [i[0] for i in self.my_cursor.description]
        return field_names, self.my_cursor.fetchall()

    def get_unique_employee_name_number(self):
        """
        Получить количество уникальных работников (по имени)
        :return: количество уникальных работников
        """
        self.my_cursor.execute("SELECT COUNT(DISTINCT EmployeeName) "
                               "FROM Salaries")

        field_names = [i[0] for i in self.my_cursor.description]
        return field_names, self.my_cursor.fetchall()

    def get_n_most_popular_job_titles(self, n=10):
        """
        Получить N самых популярных профессий (по количеству людей с данным JobTitle)
        :param n: число
        :return: список самых популярных профессий
        """
        self.my_cursor.execute(f"SELECT JobTitle, COUNT(*) AS Num "
                               f"FROM Salaries " 
                               f"GROUP BY JobTitle "
                               f"ORDER BY Num DESC "
                               f"LIMIT {n}")

        field_names = [i[0] for i in self.my_cursor.description]
        return field_names, self.my_cursor.fetchall()

    def get_job_titles_with_word(self, word):
        """
        Получить список должностей содержащих слово word и количество человек с этими должностями
        :param word: слово для шаблона поиска
        :return: список должностей содержащих слово word и количество человек с этими должностями
        """
        self.my_cursor.execute(f"SELECT JobTitle, COUNT(*) AS Num "
                               f"FROM Salaries "
                               f"WHERE JobTitle LIKE '%{word}%' "
                               f"GROUP BY JobTitle "
                               f"ORDER BY Num DESC")

        field_names = [i[0] for i in self.my_cursor.description]
        return field_names, self.my_cursor.fetchall()

    def get_employee_number_by_years(self):
        """
        Получить список лет и количество людей зарегистрированных в этот год
        :return: список лет и количество людей зарегистрированных в этот год
        """
        self.my_cursor.execute("SELECT Year, COUNT(*) AS Num "
                               "FROM Salaries "
                               "GROUP BY Year "
                               "ORDER BY Num DESC")
        field_names = [i[0] for i in self.my_cursor.description]
        return field_names, self.my_cursor.fetchall()

    def get_job_title_avg_payments(self):
        """
        Получить список профессий и средний доход для них
        :return: список профессий и средний доход для них
        """
        self.my_cursor.execute("SELECT "
                               "JobTitle, "
                               "AVG(BasePay) AS AvgBasePay, "
                               "AVG(OvertimePay) AS AvgOvertimePay, "
                               "AVG(OtherPay) AS AvgOtherPay, "
                               "AVG(Benefits) AS AvgBenefits, "
                               "AVG(TotalPay) AS AvgTotalPay, "
                               "AVG(TotalPayBenefits) AS AvgTotalPayBenefits "
                               "FROM Salaries "
                               "GROUP BY JobTitle "
                               "ORDER BY AvgTotalPay DESC")

        field_names = [i[0] for i in self.my_cursor.description]
        return field_names, self.my_cursor.fetchall()

    @staticmethod
    def print_result(title, field_names, result):
        print('\n', ('*' * 50).center(100), '\n')
        print(title + ': ', '\n')
        print(field_names)
        for x in result:
            print(x)


def main():
    my_db = MyDB()

    select_all_from_salaries_field_names, select_all_from_salaries = my_db.get_select_all_from_table()
    my_db.print_result(title='Список всех записей',
                       field_names=select_all_from_salaries_field_names,
                       result=select_all_from_salaries)

    unique_job_title_number_field_names, unique_job_title_number = my_db.unique_job_title_number()
    my_db.print_result(title='Количество уникальных дожностей',
                       field_names=unique_job_title_number_field_names,
                       result=unique_job_title_number)

    unique_job_titles_field_names, unique_job_titles = my_db.get_unique_job_titles()
    my_db.print_result(title='Список уникальных дожностей',
                       field_names=unique_job_titles_field_names,
                       result=unique_job_titles)

    people_with_max_total_pay_field_names, people_with_max_total_pay = my_db.get_n_people_with_max_total_pay(n=15)
    my_db.print_result(title='Список людей с самым большим доходом',
                       field_names=people_with_max_total_pay_field_names,
                       result=people_with_max_total_pay)

    max_base_pay_field_names, max_base_pay = my_db.get_max_base_pay()
    my_db.print_result(title='Максимальный базовый доход',
                       field_names=max_base_pay_field_names,
                       result=max_base_pay)

    job_title_number_with_firefighter_field_names, job_title_number_with_firefighter = my_db.get_job_title_number_with_word(word='firefighter')
    my_db.print_result(title='Количество должностей содержащих слово firefighter',
                       field_names=job_title_number_with_firefighter_field_names,
                       result=job_title_number_with_firefighter)

    unique_employee_name_number_field_names, unique_employee_name_number = my_db.get_unique_employee_name_number()
    my_db.print_result(title='Количество уникальных работников',
                       field_names=unique_employee_name_number_field_names,
                       result=unique_employee_name_number)

    most_popular_job_titles_field_names, most_popular_job_titles = my_db.get_n_most_popular_job_titles(10)
    my_db.print_result(title='Список самых популярных профессий',
                       field_names=most_popular_job_titles_field_names,
                       result=most_popular_job_titles)

    job_titles_with_police_field_names, job_titles_with_police = my_db.get_job_titles_with_word(word='police')
    my_db.print_result(title='Список должностей содержащих слово police и количество человек с этими должностями',
                       field_names=job_titles_with_police_field_names,
                       result=job_titles_with_police)

    employee_number_by_years_field_names, employee_number_by_years = my_db.get_employee_number_by_years()
    my_db.print_result(title='Список лет и количество людей зарегистрированных в этот год',
                       field_names=employee_number_by_years_field_names,
                       result=employee_number_by_years)

    job_title_avg_payments_field_names, job_title_avg_payments = my_db.get_job_title_avg_payments()
    my_db.print_result(title='Список профессий и средний доход для них',
                       field_names=job_title_avg_payments_field_names,
                       result=job_title_avg_payments)


if __name__ == '__main__':
    main()
