--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.3 в Вт мар 8 20:29:32 2022
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: markers
CREATE TABLE markers (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    marker   VARCHAR,
    exp_name VARCHAR,
    info     VARCHAR
);

INSERT INTO markers (
                        id,
                        marker,
                        exp_name,
                        info
                    )
                    VALUES (
                        0,
                        '1',
                        'BAIKAL',
                        'По-бурятски это озеро называется Байгаал-далай. Монгольское слово «далай» — «океан», «великий» — указывает и на размеры, и на святость Байкала (по аналогии с далай-ламой). По преданию кабанских бурят, живущих на восточном берегу озера, однажды земля в этом месте содрогнулась, и появилась трещина с пылающим в ней огнем. Боги не вняли молитвам испуганных людей, тогда они воскликнули: «Бай, гал!» — «Огонь, остановись!» Огонь стал затухать. Постепенно трещина заполнилась водой и осталась в памяти народа под именем Байгаал.'
                    );

INSERT INTO markers (
                        id,
                        marker,
                        exp_name,
                        info
                    )
                    VALUES (
                        1,
                        NULL,
                        'PESHERA_ARAL',
                        'Самый большой грот Байкала находится со стороны моря на мысе Арал на Малом Море, его длина достигает 37 м, ширина до 5 м, высота до 5 м. Вторая пещера-грот расположена на мысе Калтыгей в 1,5 км к северу от пос. Малая Зама. Длина этой пещеры 13 м и ширина около 5 м. Особенно живописный гроты в марте, когда они покрыты ледяным ожерельем. До пещеры около 1 часа ходьбы от Замы.'
                    );

INSERT INTO markers (
                        id,
                        marker,
                        exp_name,
                        info
                    )
                    VALUES (
                        2,
                        NULL,
                        'NEPRA',
                        'Нерпа – это байкальский эндемик и один из трех видов пресноводных тюленей, которые существуют в мире. Большинство учёных склоняются к мнению, что данные млекопитающие, кстати, как и байкальский омуль, попали в озеро из Северного ледовитого океана в межледниковый период, когда ещё существовал водный путь по руслу нынешних рек Ангара и Енисей. По крайней мере, последние 20 000 лет нерпа существует и эволюционирует обособленно от остальных видов тюленей.'
                    );

INSERT INTO markers (
                        id,
                        marker,
                        exp_name,
                        info
                    )
                    VALUES (
                        3,
                        NULL,
                        'OMYL',
                        'Принадлежит байкальский омуль к семейству лососевые, роду сиги. Впервые он был описан в 1775 году и получил название «мигрирующий сиг». Данный вид является эндемиком и живёт только в Байкале, потому что этой рыбе нужна вода, богатая кислородом. Тело удлинённой формы, чешуя мелкая, рот конический, челюсти равной длины. Окраска туловища светло-серебристая. Спина темнее боков. Цвет у неё буровато-зелёный с серебристым оттенком. На голове и спинном плавнике имеются тёмные пятна. Средний размер взрослых рыб составляет 37-40 см при все 0,6-0,8 кг.'
                    );

INSERT INTO markers (
                        id,
                        marker,
                        exp_name,
                        info
                    )
                    VALUES (
                        4,
                        NULL,
                        'OLHONSKY_BURATA',
                        'В состав этнотерриториальной группы ольхонских бурят входили такие малые племена, как шоно, абазай, хамнай, хэнгэлдэр, алагуй, сойод, галзуд, сэгэнуд, хайтал, буян, дурлай, харбяд, нохой, баяндай, булагад. Ольхонские буряты расселены на острове Ольхон и в средней части западного побережья озера Байкал и являются коренным народом Байкала.'
                    );

INSERT INTO markers (
                        id,
                        marker,
                        exp_name,
                        info
                    )
                    VALUES (
                        5,
                        NULL,
                        'PIROMYD_IS_CUMNEY',
                        'Согласно верованиям бурят, в каждой местности обитают свои духи. Для самых сильных из них сооружают обоо — пирамиду из камней, возле которой совершают жертвоприношения. В качестве жертвы выступают сладости и молочные продукты, монеты, хлеб, завязанные полоски ткани, жгуты благовония.'
                    );

INSERT INTO markers (
                        id,
                        marker,
                        exp_name,
                        info
                    )
                    VALUES (
                        6,
                        NULL,
                        'SHAMAN_CUMEN',
                        'Было у старого богатыря Байкала 336 сыновей и единственная дочь Ангара, которую он прятал на морском дне. Когда пришло время Ангаре выйти замуж, отец задумал отдать ее за соседа Иркута. Но чайка, прилетевшая издалека, рассказала девушке про красивого богатыря Енисея, и зажглось сердце Ангары любовью. Она обманула отца, пробила горный хребет и вырвалась из моря. Обнаружив побег, Байкал в ярости кинул вслед дочери скалу, которая стоит у истоков Ангары и которую люди прозвали Шаман-камнем.'
                    );

INSERT INTO markers (
                        id,
                        marker,
                        exp_name,
                        info
                    )
                    VALUES (
                        7,
                        NULL,
                        'TRADITION_HOME_BURATA',
                        'Традиционным жилищем бурят является юрта. Юрты бывают как войлочные, так и в виде сруба из бруса или брёвен, деревянные юрты — шести- или восьмиугольные. Юрты не имеют окон. Перед юртой устраивали коновязь в виде столба с орнаментом. В XIX веке богатые буряты начали строить для жилья избы.'
                    );

INSERT INTO markers (
                        id,
                        marker,
                        exp_name,
                        info
                    )
                    VALUES (
                        8,
                        NULL,
                        'SUV_LAVKA',
                        'Это сувенирная лавка. Здесь можно купить различные сувениры'
                    );

INSERT INTO markers (
                        id,
                        marker,
                        exp_name,
                        info
                    )
                    VALUES (
                        9,
                        NULL,
                        'STARTPOINT',
                        'Начальная позиция. Выберете маршрут и следуйте ему!'
                    );


-- Таблица: navigation
CREATE TABLE navigation (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    a_exp_id   INTEGER,
    b_exp_id   INTEGER,
    navigation VARCHAR
);

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           1,
                           1,
                           9,
                           'lu'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           2,
                           2,
                           9,
                           'ru'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           3,
                           3,
                           9,
                           'ru'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           4,
                           4,
                           9,
                           'lu'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           5,
                           5,
                           9,
                           'rulu'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           6,
                           6,
                           9,
                           'd'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           7,
                           7,
                           9,
                           'd'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           8,
                           8,
                           9,
                           'luru'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           9,
                           1,
                           2,
                           'rr'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           10,
                           3,
                           4,
                           'll'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           11,
                           5,
                           6,
                           'r'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           12,
                           6,
                           7,
                           'r'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           13,
                           7,
                           8,
                           'r'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           14,
                           2,
                           1,
                           'll'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           15,
                           3,
                           4,
                           'rr'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           16,
                           6,
                           5,
                           'l'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           17,
                           8,
                           7,
                           'l'
                       );

INSERT INTO navigation (
                           id,
                           a_exp_id,
                           b_exp_id,
                           navigation
                       )
                       VALUES (
                           18,
                           7,
                           6,
                           'l'
                       );


-- Таблица: routs
CREATE TABLE routs (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    routs VARCHAR
);

INSERT INTO routs (
                      id,
                      routs
                  )
                  VALUES (
                      1,
                      '1/2/3/4/5/6/7/8'
                  );

INSERT INTO routs (
                      id,
                      routs
                  )
                  VALUES (
                      2,
                      '1/2/5/6/7/8/4/3'
                  );

INSERT INTO routs (
                      id,
                      routs
                  )
                  VALUES (
                      3,
                      '3/4/8/7/6/5/2/1'
                  );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
