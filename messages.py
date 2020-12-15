MESSAGES = {
    "start": "Привет, друг! Я — Leader Online\nА как тебя зовут? Напиши свое ФИО",
    "help": "Вот что я могу: \n\n/start — познакомимся?\n/result — получить результат квеста\n/start_Quiz — начать квест",
    "result": "Твой результат квеста: ",
    "name_team": "Введи название своей команды:",
    "contact_face": "Введи ФИО капитана команды или контактного лица:",
    "link_vk": "Введи ссылку в вк или логин в телеграме на капитана команды или контактное лицо:",
    "tel_number": "Введи телефонный номер капитана команды или контактного лица:",
    "institute": "Выбери свой институт в УрФУ:",
    "course": "Я нашел для тебя интересные курсы\nЗарегистрируйся на один из них, отправь скришот курса со страницы \"Мои курсы\" и сможешь начать квест ;)\n\n\n",
    "end_reg": "Чтобы начать квест нажми: /start_Quiz",
    "the_end": "Благодарим Вас за участие в нашей квест-экскурсии! Прощание.mp4\nБудем рады видеть Вас снова!",  # TODO вставить ссылку на видео
    "hint": "Подсказка, специально для тебя:\n\n",
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
    "go": "\nНажми кнопку \"Поехали!\", когда доберешься до следующей точки ;)"
}


questions = {
    1: {
        "Question": "Недавно появилась технология беспроводной зарядки гаджетов. На каком максимальном  расстоянии может находится устройство для правильного функционирования?",
        "Choices": ["30 см", "10 см", "4 см"],
        "Answer": "4 см",
        "photo": ""
    },
    2: {
        "Question": "СМИ играют важную роль в жизни человека. Какой тип аудитории СМИ можно описать так: ... аудитория обладает набором общих социальных характеристик, состоит из людей с едиными информационными интересами, которые, в свою очередь, обусловлены единством социальных статусов.",
        "Choices": ["Массовая", "Целевая", "Федеральная"],
        "Answer": "Целевая"
    },
    3: {
        "Question": "СМИ для привлечения внимания использует технологию игрореализации (например репортаж \"Журналист меняет профессию\"). Существуют универсальные составляющие любой игры: правила игры, равенство шансов игроков и еще одно. Какое?\n\nA. Неопределенность результата\nB. Применение в любой ситуации\nC. Широкие возможности для экспериментов",
        "Choices": ["A", "B", "C"],
        "Answer": "A"
    },
    4: {
        "Question": "Как называлась  первая общенациональная государственная широковещательная радиостанция СССР, РСФСР и России. Имела самую мощную в мире радиосеть.",
        "Choices": ["Первый канал", "Первое радио", "Первая программа"],
        "Answer": "Первая программа"
    },
    5: {
        "Question": "Выбирете полный список стадий жизненного цикла систем в управлении инженерной деятельностью. (ГОСТ Р 57193-2016)\n\nA. Разработка, производство, вывод из эксплуатации\nB. Замысел, производство, поддержка, вывод из эксплуатации\nC. Замысел, разработка, производство, применение, поддержка и выведение из эксплуатации",
        "Choices": ["A", "B", "C"],
        "Answer": "C"
    },
    6: {
        "Question": "\"Эмоции имеют свой запах и привкус; возможно передаются от человека к человеку посредством каких-то особых войн\" Диана Сеттерфилд. Необычное высказывание, а как называется способность распозновать эмоции и управлять ими для решения практических задач?",
        "Choices": ["Эмпатия", "Эмоциональный интеллект", "Интуиция"],
        "Answer": "Эмоциональный интеллект"
    },
    7: {
        "Question": "Для того, чтобы эффективно управлять предприятием, необходимо четко понимать все группы людей, которые могут повлиять на деятельность. А какую группу можно описать следующими словами: это те, кто активно вовлечен в проект или бизнес, те, на чьи интересы может повлиять успех или неуспех проекта, а также те, кто в силу своей должности или полномочий может сам повлиять на проект.",
        "Choices": ["Стейкхолдеры", "Регулирующие органы", "Команда проекта"],
        "Answer": "Стейкхолдеры"
    },
    8: {
        "Question": "В 21 веке у каждого изнас формируются так называемые Soft skills, одним из которых является критическое мышление. А когда впервые появился  термин \"Критическое мышление\"?",
        "Choices": ["1986", "1910", "2001"],
        "Answer": "1910"
    },
    9: {
        "Question": "В 1980 году профессор психологии Роберт Плутчик придумал «колесо эмоций», выделив 8 ключевых из них. Выберите правльный список.\n\nA. гнев, злость, радость, грусть, обида, удивление, отрицание, любовь\nB. оптимизм, любовь, презрение, надежда, риск, зависть, любопытство, доминирование\nC. радость, грусть, страх, доверие, ожидание, удивление, злость, неудовольствие",
        "Choices": ["A", "B", "C"],
        "Answer": "C"
    },
    10: {
        "Question": "Цитология – это наука, изучающая\n\nA. Тканевый уровень организации живой материи\nB. Организменный уровень организации живой материи\nC. Клеточный уровень организации живой материи",
        "Choices": ["A", "B", "C"],
        "Answer": "C"
    },
    11: {
        "Question": "Одинаковый набор хромосом характерен для\n\nA. Гаметы мха\nB. Клетки фотосинтезирующей ткани листа\nC. Клетки корня цветкового растения",
        "Choices": ["A", "B", "C"],
        "Answer": "A"
    },
    12: {
        "Question": "Цитоплазма клетки – это:\n\nA. Водный раствор солей и органических веществ вместе с органоидами клетки, но без ядра;\nB. Раствор органических веществ, включающих ядро клетки;\nC. Водный раствор минеральных веществ, включающий все органоиды клетки вместе с ядром.",
        "Choices": ["A", "B", "C"],
        "Answer": "A"
    },
    13: {
        "Question": "... infrusructure – это, прежде всего, инфраструктура знания или человеческий капитал, включая институции, идеи, культурные нормы, концепты и решения.",
        "Choices": ["Hard", "Soft", "Light"],
        "Answer": "Soft"
    },
    14: {
        "Question": "Что такое «пруд-охладитель» на АЭС?\n\nA. Физический резервуар для воды, используемой для охлаждения АЭС\nB. Резервуар, в котором плавают работники станции в целях восстановления сил и здоровья\nC. Бассейн на территории АЭС",
        "Choices": ["A", "B", "C"],
        "Answer": "A"
    },
    15: {
        "Question": "Б. Такман выделил пять стадий развития команд, знание о которых позволит избежать трудностей и выстроить эффективную работу над проектом.\n\n1) Формирование, Forming\n\n2)Столкновение, Storming\n\n3)Нормализация, Norming\n\n4)Исполнение, Performing\n\n5)Закрытие, Adjourning\n\nНа какой стадии установилось согласие и сотрудничество, команда зрелая и хорошо организованна?",
        "Choices": ["3", "4", "5"],
        "Answer": "4"
    },
    16: {
        "Question": "К какому типу относится риск «Недостаточный спрос на продукт проекта»?",
        "Choices": ["Организационный", "Внутренний", "Внешний"],
        "Answer": "Внешний"
    },
    17: {
        "Question": "Python — это скриптовый язык программирования. Он универсален, поэтому подходит для решения разнообразных задач и многих платформ, начиная с iOS и Android и заканчивая серверными ОС. На этом языке были написаны знаменитые игры, например",
        "Choices": ["World of Tanks", "Dota 2", "Pac-Man"],
        "Answer": "World of Tanks"
    },
    18: {
        "Question": "Какой строительный материал называют \"горный лен\"",
        "Choices": ["Хризотилцемент", "Кирпич", "Известка"],
        "Answer": "Хризотилцемент"
    },
    19: {
        "Question": "... - состояние, когда человек оценивает себя в разных обастях, давая оценку тем или иным своим качествам\n\nA. Чувство собственного достоинства\nB. Самооценка\nC. Гордость",
        "Choices": ["A", "B", "C"],
        "Answer": "B"
    },
    20: {
        "Question": "Что такое матрица в алгебре?\n\nA. Прямоугольная таблица чисел или выражений, созданная для упрощения расчетов\nB. Фильм сестер Вачовски\nC. Буква",
        "Choices": ["A", "B", "C"],
        "Answer": "A"
    },
    21: {
        "Question": "Это автомобиль, который приводится в движение не двигателем внутреннего сгорания, а одним или несколькими электродвигателями, питающимися от аккумуляторов или топливных элементов.",
        "Choices": ["Автомобили Тесла относятся к этой категории транспорта"],
        "Answer": "электромобиль"
    },
    22: {
        "Question": "В функционале журналистов появилось новое: (ОН) должен побуждать читателей взаимодействовать "
                    "с контентом, пробуждать интерес к той или иной тематике, а также быть своего рода «якорем» для "
                    "дальнейших контактов с текстом или с его автором. В психологии Он - \"спусковой крючок\"",
        "Choices": ["Название соответвует российскому сериалу 2018 года с Максимом Матвеевым в главной роли"],
        "Answer": "триггер"
    },
    23: {
        "Question": "В широком смысле ЭТО – традиционный канон мысли, восприятия и поведения, шаблонная манера поведения.",
        "Choices": ["Ситуация, когда в России все ходят в шапках-ушанках и с медведями"],
        "Answer": "стереотип"
    },
    24: {
        "Question": "Какого числа отмечается день работника Атомной промышленности? ",
        "Choices": ["271 день в григорианском календаре"],
        "Answer": "28"
    },
    25: {
        "Question": "Как расшфровываеся МАГАТЕЭ?",
        "Choices": ["Организация была создана 3 декабря 1955 года"],
        "Answer": "международное агентство по атомной энергии"
    },
    26: {
        "Question": "В рамках креативной экономики существует большое количество показателей, один из которых Глобальный индекс креативности, показывающий потенциал стран в ключе модернизации и инвестиций. Как вы думаете, какая страна оказалась на момент 2015 года на первом месте по этому показателю?",
        "Choices": ["Континет Кенгуру и Коал, Родина Хью Джекмана"],
        "Answer": "австралия"
    },
    27: {
        "Question": "Сделайте прогноз, сколько еще часов необходимо потратить сотруднику для завершения задачи. В еженедельном отчете содержится следующая информация:\n\n- рабочая неделя — 5 дней, 8 часов в день\n- прогнозная длительность задачи – 3 рабочих дня;\n- сотрудник потратил 2 дня и выполнил половину работ.\n\nДиапазон: от 10 до 24 часов",
        "Choices": ["квадратный корень из 256"],
        "Answer": "16"
    },
    28: {
        "Question": "В рамках цифровизации отношений государства и бизнеса появляется понятие — ... — федеральные информационные системы и региональные информационные системы, созданные на основании соответственно федеральных законов, законов субъектов Российской Федерации, на основании правовых актов государственных органов.",
        "Choices": ["ЕГАИС - Единая ... автоматизированная ...  ... , предназначенная для государственного контроля над объёмом производства и оборота этилового спирта (но ответ во множественном числе)"],
        "Answer": "государственные информационные системы"
    },
    29: {
        "Question": "В зависимости от результата сколько видов стресса различают психологи? (Укажите число)",
        "Choices": ["Я робот и не знаком с психологией, но попробуй поискать четное простое число ;)"],
        "Answer": "2"
    },
    30: {
        "Question": "В известном сериале ученый разработал теорию лжи,основываясь на выражениях лиц людей. Как называется наука, которая стала основой этой теории, изучающая черты и выражения лица, обусловленные старением и типом личности?",
        "Choices": ["Это — метод определения типа личности человека, его душевных качеств и состояния здоровья, исходя из анализа внешних черт лица и его выражения."],
        "Answer": "Физиогномика"
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

