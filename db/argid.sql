--
-- ���� ������������ � ������� SQLiteStudio v3.3.3 � �� ��� 8 20:29:32 2022
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: markers
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
                        '��-�������� ��� ����� ���������� �������-�����. ����������� ����� ������ � ������, �������� � ��������� � �� �������, � �� �������� ������� (�� �������� � �����-�����). �� �������� ��������� �����, ������� �� ��������� ������ �����, ������� ����� � ���� ����� ������������, � ��������� ������� � �������� � ��� �����. ���� �� ����� �������� ���������� �����, ����� ��� �����������: ����, ���!� � ������, ����������!� ����� ���� ��������. ���������� ������� ����������� ����� � �������� � ������ ������ ��� ������ �������.'
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
                        '����� ������� ���� ������� ��������� �� ������� ���� �� ���� ���� �� ����� ����, ��� ����� ��������� 37 �, ������ �� 5 �, ������ �� 5 �. ������ ������-���� ����������� �� ���� �������� � 1,5 �� � ������ �� ���. ����� ����. ����� ���� ������ 13 � � ������ ����� 5 �. �������� ���������� ����� � �����, ����� ��� ������� ������� ���������. �� ������ ����� 1 ���� ������ �� ����.'
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
                        '����� � ��� ����������� ������� � ���� �� ���� ����� ������������ �������, ������� ���������� � ����. ����������� ������ ���������� � ������, ��� ������ �������������, ������, ��� � ����������� �����, ������ � ����� �� ��������� ���������� ������ � ������������� ������, ����� ��� ����������� ������ ���� �� ����� �������� ��� ������ � ������. �� ������� ����, ��������� 20 000 ��� ����� ���������� � �������������� ����������� �� ��������� ����� �������.'
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
                        '����������� ����������� ����� � ��������� ���������, ���� ����. ������� �� ��� ������ � 1775 ���� � ������� �������� ������������ ���. ������ ��� �������� ��������� � ���� ������ � �������, ������ ��� ���� ���� ����� ����, ������� ����������. ���� ��������� �����, ����� ������, ��� ����������, ������� ������ �����. ������� �������� ������-�����������. ����� ������ �����. ���� � �� ��������-������ � ����������� ��������. �� ������ � ������� �������� ������� ����� �����. ������� ������ �������� ��� ���������� 37-40 �� ��� ��� 0,6-0,8 ��.'
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
                        '� ������ ������������������� ������ ���������� ����� ������� ����� ����� �������, ��� ����, ������, ������, ���������, ������, �����, ������, �������, ������, ����, ������, ������, �����, �������, �������. ���������� ������ ��������� �� ������� ������ � � ������� ����� ��������� ��������� ����� ������ � �������� �������� ������� �������.'
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
                        '�������� ���������� �����, � ������ ��������� ������� ���� ����. ��� ����� ������� �� ��� ��������� ���� � �������� �� ������, ����� ������� ��������� ����������������. � �������� ������ ��������� �������� � �������� ��������, ������, ����, ���������� ������� �����, ����� ����������.'
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
                        '���� � ������� �������� ������� 336 ������� � ������������ ���� ������, ������� �� ������ �� ������� ���. ����� ������ ����� ������ ����� �����, ���� ������� ������ �� �� ������ ������. �� �����, ����������� ��������, ���������� ������� ��� ��������� �������� ������, � �������� ������ ������ �������. ��� �������� ����, ������� ������ ������ � ��������� �� ����. ��������� �����, ������ � ������ ����� ����� ������ �����, ������� ����� � ������� ������ � ������� ���� �������� �����-������.'
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
                        '������������ ������� ����� �������� ����. ���� ������ ��� ���������, ��� � � ���� ����� �� ����� ��� �����, ���������� ���� � �����- ��� ��������������. ���� �� ����� ����. ����� ����� ���������� �������� � ���� ������ � ����������. � XIX ���� ������� ������ ������ ������� ��� ����� ����.'
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
                        '��� ���������� �����. ����� ����� ������ ��������� ��������'
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
                        '��������� �������. �������� ������� � �������� ���!'
                    );


-- �������: navigation
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


-- �������: routs
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
