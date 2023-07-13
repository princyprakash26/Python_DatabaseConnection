

from getpass import getpass
from mysql.connector import connect, Error


class Quiz:
  
    def connection_to_database(self):
        try:
            with connect(
                host = 'localhost',
                user = input('Enter the user name: '),
                password = getpass('Enter password: '),
                database = 'Quiz'
            ) as self.connection:
                print('Database connected')
                print('Start')
                Question_table = """
                CREATE TABLE Questions(
                Q_id INT AUTO_INCREMENT PRIMARY KEY,
                Question VARCHAR(50)
                )
                 """
            
                with self.connection.cursor() as cursor:
                    cursor.execute(Question_table)
                    self.connection.commit()
                    print('Questions Table Created')

                Answer_table = """
                CREATE TABLE Answers(
                id INT AUTO_INCREMENT PRIMARY KEY,
                Que_id INT,
                correct_option VARCHAR(50),
                FOREIGN KEY(Que_id) REFERENCES Questions(Q_id)
                )
                """
                with self.connection.cursor() as cursor:
                    cursor.execute(Answer_table)
                    self.connection.commit()
                    print('Answer tables is created')
                update_question = """
                ALTER TABLE Questions
                ADD COLUMN option1 VARCHAR(50),
                ADD COLUMN option2 VARCHAR(50),
                ADD COLUMN option3 VARCHAR(50),
                ADD COLUMN option4 VARCHAR(50)
                
                """
                modify_question ="""
                ALTER TABLE Questions
                MODIFY COLUMN option1 VARCHAR(100),
                MODIFY COLUMN option2 VARCHAR(100),
                MODIFY COLUMN option3 VARCHAR(100),
                MODIFY COLUMN option4 VARCHAR(100)
                """
                with self.connection.cursor() as cursor:
                    cursor.execute(modify_question)
                    self.connection.commit()
                    print('updated')

                insert_into_Questions = """
                INSERT INTO Questions(Question, option1, option2, option3, option4)
                VALUES ("What's the name of Python's sorting algorithm",
                        "Quicksort",
                        "Merge sort",
                        "Bubble sort",
                        "Timsort")
                """
                QUESTIONS = {
                    "When was the first known use of the word 'quiz'": [
                        "1771",
                        "1781",
                        "1871",
                        "1881",
                    ],
                    "Which builtin function can get information from the user": [
                        "get",
                        "print",
                        "input",
                        "write",
                    ],
                    "Which keyword do you use to loop over a given list of elements": [
                        "for",
                        "while",
                        "each",
                        "loop",
                    ],
                    "What's the purpose of the built-in zip() function": [
                        "To combine several strings into one",
                        "To iterate over two or more sequences at the same time",
                        "To compress several files into one archive",
                        "To get information from the user",
                    ],
                    "What's the name of Python's sorting algorithm": [
                        "Quicksort",
                        "Merge sort",
                        "Bubble sort",
                        "Timsort",
                    ]
                }

                with self.connection.cursor() as cursor:
                    for question, options in QUESTIONS.items():
                        cursor.execute(insert_into_Questions,(question)+tuple(options))
                        self.connection.commit()
                    print('Questions and options executed')

                insert_into_answertable = """
                INSERT INTO Answers(id,Que_id,correct_option)
                VALUES(1,1,2),
                (2,2,3),
                (3,3,1),
                (4,4,2),
                (5,5,4)
                """

                with self.connection.cursor() as cursor:
                    cursor.execute(insert_into_answertable)
                    self.connection.commit()
                    print('Answers Table executed')


        except Error as e:
            print(e)
        

    def main(self):
        self.connection_to_database()
       
        
       
quiz = Quiz()
quiz.main()