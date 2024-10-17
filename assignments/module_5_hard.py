class User:
    def __init__(self, nickname, password, age):
        '''
        nickname: string
        password: hash type
        age: int
        '''
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __hash__(self):
        return hash(self.password)
    
    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname==other.nickname and self.password==other.password
        else:
            return 'Неверный тип данных.'
    
    def __ne__(self, other):
        if isinstance(other, User):
            return self.nickname!=other.nickname or self.password!=other.password
        else:
            return 'Неверный тип данных.'

    def __contains__(self, item):
        return item in self.nickname
    
    def __repr__(self) -> str:
        return f'{self.nickname}'
    

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        '''
        title: string
        duration: int
        time-now: int
        adult_mode: bool
        '''
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __contains__(self, item):
        # item: str
        return item in self.title.lower()
    
    def __repr__(self) -> str:
        return self.title

class UrTube:
    def __init__(self, users=[], videos=[], current_user=None):
        '''
        users: list of objects of class User
        videos: list of objects of class Video
        current_user: object of class User
        '''
        # if users==None:
        #     users = []
        self.users = users
        self.videos = videos
        self.current_user = current_user
    
    def log_in(self, nickname, password):
        user_loging = User(nickname, password, 0)
        for i in range(len(self.users)):
            if user_loging==self.users[i]:
                self.current_user = User(nickname, hash(user_loging), self.users[i].age)
                flag = f'Регистрация успешна. Текущий пользователь: {self.current_user.nickname}.'
                break
            else:
                flag = 'Неверный логин или пароль.'
                continue
        return flag

    def get_user_names(self):
        names = []
        for i in range(len(self.users)):
            names.append(self.users[i].nickname)
        return names
    
    def get_video_titles(self):
        '''
        function gets the titles of all videos
        '''
        video_titles = []
        for i in range(len(self.videos)):
            video_titles.append(self.videos[i].title)
        return video_titles

    def __str__(self) -> str:
        for i in range(len(self.users)):
            return self.users[i].nickname
        
    def register(self, nickname, password, age):
        if nickname not in self.get_user_names():
            self.users.append(User(nickname, password, age))
            flag = f'Пользователь {nickname} успешно зарегистрирован(-а).'
            self.log_in(nickname, password)
        else:
            flag = f'Пользователь {nickname} уже существует. Придумайте новое имя.'
        return flag
    
    def log_out(self):
        self.current_user = None
        print('До свидания!')
    
    def add(self, *args):
        video_lowercase = [x.lower() for x in self.get_video_titles()]
        for video in args:
            if video.title.lower() not in video_lowercase:
                self.videos.append(video)
                flag = f'Добавлено видео "{video.title}".'
            else:
                flag = f'Видео под названием "{video.title}" уже существует. Придумайте новое название.'
        return flag

    def get_videos(self, keyword):
        '''
        Function finds all videos based on the keyword.
        '''
        videos_found = []
        for i in range(len(self.videos)):
            if keyword.lower() in self.videos[i]:
                videos_found.append(self.videos[i])
        return f'Результат поиска по слову {keyword}: \n{videos_found}'

    def watch_video(self, title):
        from time import sleep
        if self.current_user != None:
            for i in range(len(self.videos)):
                if title==self.videos[i].title:
                    if self.videos[i].adult_mode==True and self.current_user.age >= 18:
                        sec = 1
                        while sec <= self.videos[i].duration:
                            print(sec, sep=' ', end=' ', flush=True)
                            sleep(1)
                            sec += 1
                        flag = 'Конец видео.'
                        break
                    else:
                        flag = 'Вам нет 18 лет, пожалуйста, покиньте страницу.'
                        break
                else:
                    flag = 'Видео не найдено.'
                    continue
        else:
            flag = 'Войдите в аккаунт, чтобы смотреть видео.'
        print(flag)
        

if __name__=='__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')