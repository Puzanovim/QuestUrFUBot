import pymysql
import pymysql.cursors

from config import MYSQL_DB, MYSQL_USER, MYSQL_HOST, MYSQL_PWD


class Db:
    def connect(self):
        self.conn = pymysql.connect(host=MYSQL_HOST,
                                    user=MYSQL_USER,
                                    password=MYSQL_PWD,
                                    db=MYSQL_DB,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def query(self, query, params=()):
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
        except pymysql.OperationalError:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
        finally:
            self.conn.close()
        return cursor

    def count(self, user_id):
        sql = "SELECT COUNT(*) FROM `teams_quest` WHERE `user_id`=%s"
        self.request = self.query(sql, user_id)
        self.result = self.request.fetchone()
        print("Db().count(): Counted")
        if self.result['COUNT(*)'] > 0:
            return True
        return False

    def create_team(self, user_id, name=""):
        exist = self.count(user_id)
        if not exist:
            sql = "INSERT INTO `teams_quest` (`user_id`, `name`) VALUES (%s, %s)"
            self.request = self.query(sql, (user_id, name))
            sql = "INSERT INTO `points_table_quest` (`user_id`, `current_question`) VALUES (%s, %s)"
            self.request = self.query(sql, (user_id, 0))
            print("Db().create_team(): Created")
        else:
            sql = "UPDATE `teams_quest` SET `name`=%s WHERE `user_id`=%s"
            self.request = self.query(sql, (name, user_id))
            print("Db().create_team(): Updated")

    def update_name(self, user_id, name=""):
        exist = self.count(user_id)
        if exist:
            sql = "UPDATE `teams_quest` SET `name`=%s WHERE `user_id`=%s"
            self.request = self.query(sql, (name, user_id))
            print("Db().update_name(): Updated")
            return 1
        else:
            return 0

    def get_name(self, user_id):
        exist = self.count(user_id)
        if exist:
            sql = "SELECT * FROM `teams_quest` WHERE `user_id`=%s"
            self.request = self.query(sql, user_id)
            self.result = self.request.fetchone()
            print("Db().get_name(): Got")
            return self.result["name"]
        else:
            return ""

    def add_contact_face(self, user_id, contact_face):
        exist = self.count(user_id)
        if exist:
            sql = "UPDATE `teams_quest` SET `contact_face`=%s WHERE `user_id`=%s"
            self.request = self.query(sql, (contact_face, user_id))
            print("Db().add_contact_face(): Added")
        else:
            print("Db().add_contact_face(): User doesn't exist")

    def add_link_vk(self, user_id, link_vk):
        exist = self.count(user_id)
        if exist:
            sql = "UPDATE `teams_quest` SET `link_vk`=%s WHERE `user_id`=%s"
            self.request = self.query(sql, (link_vk, user_id))
            print("Db().add_link_vk(): Added")
        else:
            print("Db().add_link_vk(): User doesn't exist")

    def add_tel_number(self, user_id, tel_number):
        exist = self.count(user_id)
        if exist:
            sql = "UPDATE `teams_quest` SET `tel_number`=%s WHERE `user_id`=%s"
            self.request = self.query(sql, (tel_number, user_id))
            print("Db().add_tel_number(): Added")
        else:
            print("Db().add_tel_number(): User doesn't exist")

    def add_institute(self, user_id, institute=""):
        exist = self.count(user_id)
        if exist:
            sql = "UPDATE `teams_quest` SET `institute`=%s WHERE `user_id`=%s"
            self.request = self.query(sql, (institute, user_id))
            print("Db().add_institute(): Added")
        else:
            print("Db().add_institute(): User doesn't exist")

    def get_result(self, user_id):
        sql = "SELECT `result` FROM `points_table_quest` WHERE `user_id`=%s"
        self.request = self.query(sql, user_id)
        self.result = self.request.fetchone()
        print("Db().get_result(): Done")

        return int(self.result['result'])

    def get_current_question(self, user_id: int) -> int:
        sql = "SELECT `current_question` FROM `points_table_quest` WHERE `user_id`=%s"
        self.request = self.query(sql, user_id)
        self.result = self.request.fetchone()
        print("Db().get_current_question(): Done")

        return int(self.result['current_question'])

    def set_point(self, user_id: int, question: int):
        result = self.get_result(user_id)
        new_result = result + 1
        sql = "UPDATE `points_table_quest` SET `%s`='1', `result`=%s WHERE `user_id`=%s"
        self.request = self.query(sql, (question, str(new_result), user_id))
        print("Db().set_point(): Done")

    def increment_current_question(self, user_id: int, current_question: int):
        new_question = current_question + 1
        sql = "UPDATE `points_table_quest` SET `current_question`=%s WHERE `user_id`=%s"
        self.request = self.query(sql, (str(new_question), user_id))
        print("Db().increment_current_question(): Done")

    def get_users(self):
        sql = "SELECT * FROM `teams_quest`"
        self.request = self.query(sql)
        self.result = self.request.fetchall()
        print("Db().get_users(): Done")

        return self.result


def test():
    user = 8929
    db = Db()
    db.create_user(user, "Nowhere man")
    db.add_institute(user, "simple")
    question = db.get_current_question(user)
    db.set_point(user, 5)
    db.increment_current_question(user, question)
    print(db.get_result(user))
