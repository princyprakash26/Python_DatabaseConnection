from getpass import getpass
from mysql.connector import connect,Error


class Quiz():
    def Get_Quiz(self):
        try:
             
           with connect(
               host = 'localhost',
               user = input('user name:'),
               password = getpass('password:'),
               database = 'Quiz'
            ) as self.connection:
                print('Database Connected')
                
                Questions = """
                select Q_id,Question ,option1,option2,option3,option4 
                from Questions
                """
                scores = 0
                with self.connection.cursor() as cursor:
                    cursor.execute(Questions)
                    questions = cursor.fetchall()
                    print('***QUIZ STARTED***')
                    for (Q_id,Question,option1,option2,option3,option4) in questions:
                        print(f'{Q_id}:{Question}?')
                        print(f'{1}:{option1}')
                        print(f'{2}:{option2}')
                        print(f'{3}:{option3}')
                        print(f'{4}:{option4}')
                        user_option =input('choose the correct option:')
                        print(user_option)

                        select_correct_option = """
                        SELECT correct_option 
                        FROM Answers
                        where Que_id = %s
                        """
                        with self.connection.cursor() as cursor:
                            cursor.execute(select_correct_option,(Q_id,))
                            correct_option = cursor.fetchone()[0]
                            self.connection.commit()
               
                        if user_option == correct_option:
                           print('****Correct answer****')
                           scores +=1
                        else:
                            print('**Wrong Answer**')
                            print(f'{correct_option} is the correct answer')
                            scores = 1

                print(f'Your Score Is {scores}')
                print('Quiz Completed')

        except Error as e:
            print(e)



quiz = Quiz()
quiz.Get_Quiz() 
    