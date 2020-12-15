MESSAGES = {
    "start": "Привет, друг! Я — Leader Online\nА как тебя зовут? Напиши свое ФИО",
    "help": "Вот что я могу: \n\n/start — познакомимся?\n"
            "/result — получить результат квеста\n"
            "/start_Quiz — начать квест",
    "result": "Твой результат квеста: ",
    "name_team": "Введи название своей команды:",
    "contact_face": "Введи ФИО капитана команды или контактного лица:",
    "link_vk": "Введи ссылку в вк или логин в телеграме на капитана команды или контактное лицо:",
    "tel_number": "Введи телефонный номер капитана команды или контактного лица:",
    "institute": "Выбери свой институт в УрФУ:",
    "end_reg": "Чтобы начать квест нажми: /start_Quiz",
    "the_end": "Благодарим Вас за участие в нашей квест-экскурсии!\n"
               "https://drive.google.com/file/d/1NFhPI45YW1rYbeQcR9eknd0cqQh-ZT8K/view?usp=sharing"
               "\nБудем рады видеть Вас снова!",
    "unknown": "Прости, я не понял :(\nПопробуй ещё раз или обратись за помощью к @Puzanovim ;)",
    "you are finished": "Ты уже прошел квест! Свой результат можешь посмотреть по команде /result :)",
    "Привет": "Привет, хочешь сыграть в игру? Жми /start, если мы с тобой ещё не познакомились :)",
    "Как дела?": "Супер! А у тебя как?",
    "Хорошо": "Хорошо, когда все хорошо :)",
    "Супер": "Гуд ;)",
    "Отлично": "Рад это слышать!",
    "gift": "Привет, друг!\nПоздравляю тебя с успешным прохождением квеста!\nДержи свой сертификат ;)",
    "change_name": "Введи новое имя или символ N, если хочешь оставить прежнее:",
    "new_name": "Твое ФИО обновлено на ",
    "old_name": "Осталось прежнее ФИО — ",
    "repeat_name": "К сожалению, ты не проходил квест :(",
    "change_name_again": "\nОно будет указано в твоем сертификате. Если хочешь изменить ФИО нажми /change_name",
    "alert_change_name": "Привет, друг!\nНа этих выходных пришлем тебе твой сертификат ;)\n"
                         "Но перед этим, хотим, чтобы ты проверил корректность твоего имени.\n"
                         "Если хочешь его поменять — используй команду /change_name\n"
                         "Твое текущее имя: ",
    "go": "\nНажми кнопку \"Поехали!\", когда доберешься до следующей точки ;)",
    "duck": "«Сфотографироваться с утками»:\n"
            "Вам необходимо сделать фотографию, повторив снимок, который представлен схематично, "
            "то есть соблюсти примерный ракурс и позы учасников группы, а также добавить на снимок картинку утки, "
            "например, картинка может быть на экране телефона.\n"
            "Отправляй фотографию @Cou_D",
    "error_photo": "К сожалению, мы не смогли отправить тебе фотографию.\n"
                   "Сделай груповое фото так, чтобы в кадр попала утка 🦆"
}


questions = {
    1: {
        "Place": "Вы находитесь около главного учебного корпуса УрФУ. Ознакомьтесь с видео-фрагментом экскурсии, а затем ответьте на короткий вопрос.\nhttps://drive.google.com/file/d/1NFWIp0y2miUITDeqGIaHEnschGmtUg39/view",
        "Question": "Главный учебный корпус был построен только к 1939 году. В каком стиле построено здание? (укажите букву правильного ответа)\n\nA) Классицизм\nB) Конструктивизм\nC) Сталинский ампир",
        "Choices": ["A", "B", "C"],
        "Answer": "C",
        "Move": "Следующая точка маршрута: Памятник Кирову. Адрес: Втузгородок, Кировский район, Екатеринбург",
        "Photo": False,
        "Duck": False
    },
    2: {
        "Place": "Вы находитесь около памятника Сергею Мироновичу Кирову. С.М. Киров - один из известнейших государственных и партийных деятелей советской эпохи 1920–1930-х гг. и ближайших соратников И.В. Сталина. Ответьте на короткий вопрос.",
        "Question": "Настоящая фамилия Кирова? (Укажите фамилию с большой буквы)",
        "Choices": ["Костриков"],
        "Answer": "Костриков",
        "Move": "Следующая точка маршрута: Екатеринбургский дендропарк. Адрес: центральный вход на пересечении улиц Первомайская и Мира.",
        "Photo": False,
        "Duck": False
    },
    3: {
        "Place": "Вы находитесь около дендропарка на улице Первомайской, который ведет свою историю с 1932 года. Здесь проходят акклиматизацию растения со всего мира и потом получают широкое распространение по всему Уралу. Ответьте на короткий вопрос.",
        "Question": "Правда ли, что в дендропарке обитают утки? (укажите букву правильного ответа)\n\nA)Да\nB) Нет",
        "Choices": ["A", "B"],
        "Answer": "A",
        "Move": "Следующая точка маршрута: Коляда-театр. Адрес: Ленина проспект, 97 Втузгородок, Кировский район",
        "Photo": False,
        "Duck": True
    },
    4: {
        "Place": "Вы находитесь около Коляда -театра - частного театр Николая Коляды. Коляда-театр был создан 4 декабря 2001 года в день рождения своего художественного руководителя. Театр долгое время “путешествовал” по разным зданиям в Екатеринбурге и в здании на проспекте Ленина оказался только в апреле 2014. Ответьте на короткий вопрос.",
        "Question": "Как назывался первый спектакль, поставленный Николаем Колядой? (укажите букву правильного ответа)\n\nA)Персидская сирень\nB)Арабская алыча\nC) Китайская вишня",
        "Choices": ["A", "B", "C"],
        "Answer": "A",
        "Move": "Следующая точка маршрута: Железнодорожный мост. Адрес: жд станция Первомайская.",
        "Photo": False,
        "Duck": True
    },
    5: {
        "Place": "Вы находитесь около железнодорожного моста, который является частью большого маршрута - Транссибирской магистрали - в одну сторону Европа, в другую - Азия. Ответьте на короткий вопрос.",
        "Question": "Назовите протяженность транссибирской магистрали (с точностью до 1 знака после запятой, км)",
        "Choices": ["9288,2 км"],
        "Answer": "9288,2 км",
        "Move": "Следующая точка маршрута:Штаб центрального военного округа. Адрес: Проспект Ленина 71. ",
        "Photo": False,
        "Duck": True
    },
    6: {
        "Place": "Вы находитесь около Штаба Центрального Военного округа. Ознакомьтесь с видео-фрагментом экскурсии, а затем ответьте на короткий вопрос.\n"
                 "https://drive.google.com/file/d/1Bxn2Caju5wx9tTkBu5hwdc_Ai9e6grLF/view?usp=sharing "
                 "\nОтветьте на короткий вопрос.",
        "Question": "Кого называли маршалом Победы? (Укажите фамилию человека)",
        "Choices": ["Жуков"],
        "Answer": "Жуков",
        "Move": "Следующая точка маршрута: Музей истории и археологии Екатеринбурга. Адрес: Проспект Ленина 69/ 10",
        "Photo": False,
        "Duck": False
    },
    7: {
        "Place": "Вы находитесь около Музея истории и археологии Урала. Ознакомьтесь с видео-фрагментом экскурсии, а затем ответьте на короткий вопрос.\n"
                 "https://drive.google.com/file/d/1vMUPq_q7WtOcbG7b1kUi0IKF3iz17xLd/view?usp=sharing "
                 "\nОтветьте на короткий вопрос.",
        "Question": "Сколько лет шигирскому идолу? (укажите в ответе цифру)",
        "Choices": ["11600"],
        "Answer": "11600",
        "Move": "Следующая точка маршрута: Памятник Свердлову. Адрес: Центр, Октябрьский район, напротив здания УрФУ на Ленина 51.",
        "Photo": False,
        "Duck": False
    },
    8: {
        "Place": "Вы находитесь около памятника Я.М. Свердлову напротив одного из учебных корпусов УрФУ. Ознакомьтесь с видео-фрагментом экскурсии, а затем ответьте на короткий вопрос.\n"
                 "https://drive.google.com/file/d/1KNEhrDQGuR7oK1NFG7zJ7qS3QUfWrKYI/view?usp=sharing "
                 "\nОтветьте на короткий вопрос.",
        "Question": "На какой площади расположено здание Ленина 51. (укажите букву правильного ответа)"
                    "\n\nA)Площадь труда\nB) Площадь парижской коммуны\nC) Площадь первой пятилетки",
        "Choices": ["A", "B", "C"],
        "Answer": "B",
        "Move": "Следующая точка маршрута: Львы около оперного театра. Адрес: Скульптурная композиция напротив кафе “Пельмени клаб” - Красноармейская 2",
        "Photo": False,
        "Duck": True
    },
    9: {
        "Place": "Сейчас вы находитесь около скульптурной композиции “Львы”.  На этом месте они появились примерно в 40-е годы XX века и служили украшением парка Оперного театра. Интересный факт, что сам театр был открыт в далеком 1912 году.",
        "Question": "",
        "Choices": [""],
        "Answer": "",
        "Move": "Следующая точка маршрута: Памятник Высоцкому около бизнес-центра Антей. Адрес: Красноармейская 10",
        "Photo": False,
        "Duck": True
    },
    10: {
        "Place": "Владимир Семёнович Высоцкий - советский поэт, актёр театра и кино, автор-исполнитель песен (бард); автор прозаических произведений и сценариев. В.С. Высоцкий приезжал в Свердловск дважды в один и тот же год приезжал с гастролями в 1962 году. Ответьте на короткий вопрос.",
        "Question": "Кто сидит рядом с Владимиром Высоцким? (Укажите фамилию девушки с большой буквы)",
        "Choices": ["Влади"],
        "Answer": "Влади",
        "Move": "Следующая точка маршрута: Небоскреб Высоцкий. Адрес: Малышева 51.",
        "Photo": False,
        "Duck": False
    },
    11: {
        "Place": "Вы находитесь около Бизнес-центра Высоцкий. Ознакомьтесь с видео-фрагментом экскурсии, а затем ответьте на короткий вопрос.\n"
                 "https://drive.google.com/file/d/1GITKIkg0GU5FsVyzWB9N7rM8IGZHraXu/view?usp=sharing "
                 "\nОтветьте на короткий вопрос.",
        "Question": "Строчку из песни какой группы Тимофей Радя изобразил на одном из зданий около БЦ Высоцкий?"
                    "\n\nA) Чайф\nB) Агата Кристи\nC)Смысловые галлюцинации",
        "Choices": ["A", "B", "C"],
        "Answer": "C",
        "Move": "Следующая точка маршрута:Кинотеатр Колизей - Екатеринбургский театр кукол. Адрес: Проспект Ленина 43.",
        "Photo": True,
        "Duck": False
    },
    12: {
        "Place": "Механика: Вы находитесь около Кинотеатра Колизей - Екатеринбургского театра кукол. "
                 "В этом здании ранее располагался кинотеатр «Колизей» - первый городской театр в Екатеринбурге. "
                 "Ответьте на короткий вопрос.",
        "Question": "В каком году был основан театр Колизей? (укажите букву правильного ответа)"
                    "\n\nA)1734\nB)1812\nC) 1914",
        "Choices": ["A", "B", "C"],
        "Answer": "C",
        "Move": "Следующая точка маршрута: Памятник Попову. Адрес: Рядом со зданием Главпочтампта - Ленина 39.",
        "Photo": False,
        "Duck": True
    },
    13: {
        "Place": "Вы находитесь около памятника Александру Степановичу Попову. "
                 "А.С. Попов - русский физик и электрик, профессор. Является одним из создателей радио. "
                 "Ответьте на короткий вопрос.",
        "Question": "Студенты какого факультета УрФУ каждый год ухаживают за памятником А.С. Попова? "
                    "(укажите букву правильного ответа)\n\nA) Филологи\nB) Радисты\nC) Туристы",
        "Choices": ["A", "B", "C"],
        "Answer": "B",
        "Move": "Следующая точка маршрута:Граффити “Волшебные растения Екатеринбурга”. Адрес: Толмачева 23",
        "Photo": False,
        "Duck": True
    },
    14: {
        "Place": "Вы находитесь около граффити “Волшебные растения Екатеринбурга” - Каждый из 33 художников "
                 "арт-сообщества взялся изучить историю и существующую мифологию Екатеринбурга, на основе которой "
                 "каждый создал “растение”, тем или иным образом связанное с главным объектом граффити. Каждое "
                 "растение обладает некой ярко выраженной символикой, так как через растения (мифы о них) проявляются "
                 "основные архитипы Урала, уральца. Ответьте на короткий вопрос.",
        "Question": "Сколько метров составлял объект, ставший основой граффити «Волшебные растения Екатеринбурга»? "
                    "(укажите букву правильного ответа)\n\nA)239\nB)400\nC) 150",
        "Choices": ["A", "B", "C"],
        "Answer": "A",
        "Move": "Следующая точка маршрута: Литературный квартал",
        "Photo": False,
        "Duck": True
    },
    15: {
        "Place": "Вы находитесь в Литературном квартале. Ознакомьтесь с видео-фрагментом экскурсии, "
                 "а затем ответьте на короткий вопрос."
                 "\nhttps://drive.google.com/file/d/19YWvg-qTWr2y7jyY47oFCdXWBjozTNdN/view?usp=sharing "
                 "\nОтветьте на короткий вопрос.",
        "Question": "Назовите писателей, живших в литературном квартале? (укажите букву правильного ответа)\n\n"
                    "A) Мамин-Сибиряк, Решетников, Бажов\n"
                    "B) Маяковский, Решетников, Бажов\n"
                    "C) Пушкин, Мамин-Сибиряк, Бажов",
        "Choices": ["A", "B", "C"],
        "Answer": "A",
        "Move": "",
        "Photo": False,
        "Duck": False
    },
}


institutes = {
    "ИРИТ-РТФ": ["Программирование глубоких нейронных сетей на Python (https://openedu.ru/course/urfu/PYDNN/)",
                 "Основные приложения линейной алгебры в инженерном образовании (https://openedu.ru/course/urfu/LineAlg/)",
                 "Теория вероятностей и математическая статистика для инженеров (https://openedu.ru/course/urfu/TheorVer/)",
                 "Информационные сервисы в управлении инженерной деятельностью (https://openedu.ru/course/urfu/ITS/)",
                 "Взаимодействие государства и бизнеса в условиях цифровой трансформации (https://openedu.ru/course/urfu/GOVBUSINESS/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "ИнФО":     ["Информационные сервисы в управлении инженерной деятельностью (https://openedu.ru/course/urfu/ITS/)",
                 "Программирование глубоких нейронных сетей на Python (https://openedu.ru/course/urfu/PYDNN/)",
                 "Взаимодействие государства и бизнеса в условиях цифровой трансформации (https://openedu.ru/course/urfu/GOVBUSINESS/)",
                 "Основные приложения линейной алгебры в инженерном образовании (https://openedu.ru/course/urfu/LineAlg/)",
                 "Теория вероятностей и математическая статистика для инженеров (https://openedu.ru/course/urfu/TheorVer/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "ИнЭУ":     ["Взаимодействие государства и бизнеса в условиях цифровой трансформации (https://openedu.ru/course/urfu/GOVBUSINESS/)",
                 "Экономическая эффективность технических решений (https://openedu.ru/course/urfu/EFFSOLUTION/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "ИФКСиМП":  ["Взаимодействие государства и бизнеса в условиях цифровой трансформации (https://openedu.ru/course/urfu/GOVBUSINESS/)",
                 "Введение в биологию клетки (https://openedu.ru/course/urfu/CELLBIO/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "УГИ":      ["Взаимодействие государства и бизнеса в условиях цифровой трансформации (https://openedu.ru/course/urfu/GOVBUSINESS/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "ФТИ":      ["Введение в биологию клетки (https://openedu.ru/course/urfu/CELLBIO/)",
                 "Ядерная медицина (https://openedu.ru/course/urfu/NUCMED/)",
                 "Теория вероятностей и математическая статистика для инженеров (https://openedu.ru/course/urfu/TheorVer/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "ХТИ":      ["Ядерная медицина (https://openedu.ru/course/urfu/NUCMED/)",
                 "Введение в биологию клетки (https://openedu.ru/course/urfu/CELLBIO/)",
                 "Теория вероятностей и математическая статистика для инженеров (https://openedu.ru/course/urfu/TheorVer/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "ИСА":      ["Строительные технологии на основе хризотилцементных материалов (https://openedu.ru/course/urfu/chryso/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "ИНМТ":     ["Информационные сервисы в управлении инженерной деятельностью (https://openedu.ru/course/urfu/ITS/)",
                 "Строительные технологии на основе хризотилцементных материалов (https://openedu.ru/course/urfu/chryso/)",
                 "Теория вероятностей и математическая статистика для инженеров (https://openedu.ru/course/urfu/TheorVer/)",
                 "Экономическая эффективность технических решений (https://openedu.ru/course/urfu/EFFSOLUTION/)",
                 "Управление машиностроительным предприятием (https://openedu.ru/course/urfu/MANEGEMACH/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "УралЭНИН": ["Теория вероятностей и математическая статистика для инженеров (https://openedu.ru/course/urfu/TheorVer/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "ИЕНИМ":    ["Программирование глубоких нейронных сетей на Python (https://openedu.ru/course/urfu/PYDNN/)",
                 "Основные приложения линейной алгебры в инженерном образовании (https://openedu.ru/course/urfu/LineAlg/)",
                 "Взаимодействие государства и бизнеса в условиях цифровой трансформации (https://openedu.ru/course/urfu/GOVBUSINESS/)",
                 "Ядерная медицина (https://openedu.ru/course/urfu/NUCMED/)",
                 "Информационные сервисы в управлении инженерной деятельностью (https://openedu.ru/course/urfu/ITS/)",
                 "Введение в биологию клетки (https://openedu.ru/course/urfu/CELLBIO/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "ИТОО":     ["Взаимодействие государства и бизнеса в условиях цифровой трансформации (https://openedu.ru/course/urfu/GOVBUSINESS/)",
                 "Информационные сервисы в управлении инженерной деятельностью (https://openedu.ru/course/urfu/ITS/)",
                 "Программирование глубоких нейронных сетей на Python (https://openedu.ru/course/urfu/PYDNN/)",
                 "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                 "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
    "я не из УрФУ": ["Программирование глубоких нейронных сетей на Python (https://openedu.ru/course/urfu/PYDNN/)",
                    "Основные приложения линейной алгебры в инженерном образовании (https://openedu.ru/course/urfu/LineAlg/)",
                    "Взаимодействие государства и бизнеса в условиях цифровой трансформации (https://openedu.ru/course/urfu/GOVBUSINESS/)",
                     "Теория вероятностей и математическая статистика для инженеров (https://openedu.ru/course/urfu/TheorVer/)",
                    "Информационные сервисы в управлении инженерной деятельностью (https://openedu.ru/course/urfu/ITS/)",
                    "Ядерная медицина (https://openedu.ru/course/urfu/NUCMED/)",
                     "Введение в биологию клетки (https://openedu.ru/course/urfu/CELLBIO/)",
                     "Строительные технологии на основе хризотилцементных материалов (https://openedu.ru/course/urfu/chryso/)",
                    "Экономическая эффективность технических решений (https://openedu.ru/course/urfu/EFFSOLUTION/)",
                    "Управление машиностроительным предприятием (https://openedu.ru/course/urfu/MANEGEMACH/)",
                    "Основы личностного роста (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M1/)",
                     "Развитие ресурсов организма (для лиц с ОВЗ) (https://openedu.ru/course/urfu/Inclus_M2/)"],
}

