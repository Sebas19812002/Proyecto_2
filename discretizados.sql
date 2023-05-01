BEGIN;

CREATE TABLE mytable(
  id          smallint NOT NULL,
  age         smallint NOT NULL,
  sex         smallint NOT NULL,
  cpt         smallint NOT NULL,
  pressure    smallint NOT NULL,
  chol        smallint NOT NULL,
  sugar       smallint NOT NULL,
  ecg         smallint NOT NULL,
  maxbpm      smallint NOT NULL,
  angina      smallint NOT NULL,
  oldpeak     smallint NOT NULL,
  slope       smallint NOT NULL,
  flourosopy  smallint NOT NULL,
  thal        smallint NOT NULL,
  diagnosis   smallint NOT NULL
);

-- COPY mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) FROM stdin;
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (1,3,1,1,4,2,1,2,2,0,3,3,0,6,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (2,4,1,4,4,2,0,2,1,1,2,2,3,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (3,4,1,4,2,2,0,2,1,1,3,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (4,1,1,3,3,2,0,0,3,0,4,3,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (5,2,0,2,3,2,0,2,3,0,2,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (6,3,1,2,2,2,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (7,3,0,4,4,2,0,2,2,0,4,3,2,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (8,3,0,4,2,3,0,0,2,1,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (9,3,1,4,3,2,0,2,2,0,2,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (10,2,1,4,4,2,1,2,2,1,4,3,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (11,3,1,4,4,1,0,0,2,0,1,2,0,6,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (12,3,0,2,4,2,0,2,2,0,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (13,3,1,3,3,2,1,2,2,1,1,2,1,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (14,2,1,2,2,2,0,0,3,0,1,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (15,2,1,3,4,1,1,0,2,0,1,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (16,3,1,3,4,1,0,0,3,0,2,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (17,2,1,2,1,2,0,0,2,0,2,3,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (18,2,1,4,4,2,0,0,2,0,2,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (19,2,0,3,3,2,0,0,1,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (20,2,1,2,3,2,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (21,3,1,1,1,2,0,2,2,1,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (22,3,0,1,4,2,1,2,2,0,2,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (23,3,1,2,2,2,0,2,2,0,2,2,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (24,3,1,3,3,2,0,2,3,0,4,1,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (25,3,1,4,3,2,0,2,1,1,3,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (26,2,0,3,2,2,0,0,2,0,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (27,3,0,3,2,3,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (28,4,0,1,4,2,0,0,1,0,3,3,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (29,2,1,4,4,2,0,0,3,0,2,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (30,2,1,4,1,1,0,2,1,1,3,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (31,4,0,1,4,2,0,0,2,0,2,1,2,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (32,3,1,4,1,2,1,0,2,1,2,1,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (33,3,1,3,4,3,0,0,2,0,1,1,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (34,3,1,4,3,2,0,0,2,0,1,2,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (35,2,1,3,3,2,0,0,3,1,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (36,2,1,4,4,2,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (37,2,1,4,2,1,0,2,1,1,3,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (38,3,1,4,4,2,0,2,1,1,1,2,1,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (39,3,1,4,3,3,0,0,1,1,2,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (40,3,1,3,4,2,1,0,1,1,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (41,4,0,4,4,2,0,2,1,0,2,2,3,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (42,2,1,1,4,1,0,0,3,1,2,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (43,4,0,2,4,3,0,0,2,0,1,1,2,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (44,3,1,3,4,2,1,0,2,0,2,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (45,3,0,4,3,3,0,2,2,0,1,1,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (46,3,1,3,1,2,0,2,2,0,3,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (47,2,1,3,1,1,0,0,1,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (48,2,1,4,4,2,0,2,1,0,3,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (49,4,0,3,4,3,1,2,2,0,1,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (50,2,1,3,3,1,1,2,2,0,2,3,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (51,2,0,2,1,1,0,0,2,0,1,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (52,4,1,4,2,1,0,0,2,0,1,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (53,2,1,4,1,2,0,2,2,0,1,1,1,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (54,2,1,2,3,2,0,2,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (55,3,1,4,3,2,0,0,2,1,2,1,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (56,2,1,4,2,2,0,2,1,1,3,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (57,2,1,3,4,2,0,0,2,0,1,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (58,2,1,4,1,1,0,2,2,0,1,1,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (59,2,1,3,2,2,0,2,2,0,1,3,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (60,2,1,1,2,2,0,2,1,1,2,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (61,2,0,4,3,3,0,0,2,1,2,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (62,2,0,3,4,1,0,2,2,1,2,3,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (63,3,1,4,2,2,0,2,1,1,3,2,3,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (64,2,0,3,3,3,1,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (65,2,1,4,2,1,0,0,1,0,2,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (66,3,1,4,4,2,0,2,2,1,3,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (67,3,1,3,4,1,0,2,2,0,3,2,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (68,2,1,3,4,2,0,2,2,0,2,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (69,3,1,4,4,3,0,2,2,1,4,3,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (70,2,1,3,4,2,0,0,2,0,4,2,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (71,4,0,3,4,2,0,0,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (72,4,1,4,2,2,1,0,2,0,1,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (73,3,1,4,2,2,0,0,1,1,2,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (74,4,1,4,1,2,0,2,2,0,1,1,2,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (75,2,1,4,1,1,0,2,3,0,1,1,1,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (76,4,0,3,4,3,0,2,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (77,3,1,4,2,2,0,2,2,1,3,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (78,2,0,3,4,3,0,2,2,0,2,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (79,2,1,2,3,2,0,2,3,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (80,3,1,4,4,2,0,2,1,1,1,1,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (81,2,1,4,1,2,0,2,2,1,3,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (82,2,0,4,3,2,0,2,2,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (83,1,1,3,4,3,0,2,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (84,4,1,3,4,2,1,2,2,1,2,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (85,2,1,2,2,3,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (86,2,1,3,4,2,0,2,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (87,2,1,3,3,2,0,2,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (88,2,0,4,3,2,0,2,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (89,2,0,3,3,2,0,2,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (90,4,1,4,2,3,0,2,2,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (91,3,0,4,4,1,0,2,2,0,4,3,3,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (92,3,1,3,3,2,0,0,2,0,2,2,3,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (93,2,0,3,1,1,0,0,3,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (94,3,0,3,3,2,0,2,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (95,2,1,4,2,2,0,0,2,1,1,1,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (96,3,1,4,1,2,0,2,2,1,2,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (97,3,0,4,4,2,0,2,2,0,3,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (98,2,1,2,3,2,0,0,2,0,1,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (99,2,1,4,2,2,0,2,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (100,2,1,4,1,2,0,2,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (101,1,1,1,1,1,0,2,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (102,3,0,4,2,3,0,2,2,0,1,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (103,4,0,3,1,2,1,2,1,0,1,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (104,2,1,3,2,1,0,0,1,0,3,2,3,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (105,2,1,2,1,3,0,0,2,0,1,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (106,3,1,4,4,1,0,0,2,1,1,1,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (107,3,1,3,2,2,0,2,2,0,1,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (108,3,1,4,2,2,0,0,2,1,4,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (109,1,1,4,1,2,0,0,2,0,2,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (110,3,0,4,4,3,0,2,2,1,2,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (111,3,1,4,2,2,1,2,2,1,2,2,1,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (112,2,1,1,1,1,0,2,3,0,1,2,0,6,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (113,2,0,4,3,3,1,2,1,1,3,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (114,3,0,3,3,2,0,0,1,0,2,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (115,2,1,2,3,2,0,0,1,0,1,2,0,6,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (116,3,1,3,4,2,1,2,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (117,1,0,4,3,1,0,0,3,0,2,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (118,3,1,4,3,3,1,2,1,1,2,1,3,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (119,4,1,4,3,2,0,2,1,0,3,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (120,2,1,4,3,2,1,2,2,1,1,1,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (121,3,0,4,4,3,0,2,2,0,4,2,3,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (122,2,1,3,1,2,0,0,2,1,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (123,3,1,4,4,2,0,0,1,1,4,3,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (124,4,1,1,3,2,1,2,3,0,2,2,1,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (125,2,0,2,3,2,0,2,3,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (126,3,0,4,5,2,1,2,1,1,4,3,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (127,2,1,4,1,2,0,0,1,1,3,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (128,2,1,2,2,2,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (129,3,0,4,2,2,0,0,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (130,2,1,3,2,2,0,2,2,0,1,2,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (131,2,1,3,1,2,0,0,2,1,1,1,1,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (132,1,1,2,3,2,0,2,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (133,2,1,4,4,2,0,2,3,1,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (134,2,0,3,2,2,0,0,2,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (135,3,0,2,3,2,0,2,2,0,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (136,4,1,4,4,1,0,0,1,1,3,3,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (137,3,1,2,2,2,0,2,1,0,2,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (138,1,1,4,2,1,0,0,1,1,2,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (139,2,1,3,2,2,1,2,2,0,3,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (140,3,1,2,4,2,0,0,2,1,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (141,3,1,1,4,2,0,2,2,0,1,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (142,2,1,2,2,2,1,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (143,3,1,3,2,3,0,0,1,1,2,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (144,3,1,3,1,2,0,2,2,1,1,2,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (145,2,1,3,1,2,0,0,2,0,1,1,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (146,3,1,4,4,2,1,2,1,0,2,2,3,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (147,2,1,3,1,2,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (148,2,1,2,2,3,0,2,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (149,3,0,3,1,3,0,0,2,0,1,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (150,2,1,1,4,2,1,0,3,0,2,2,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (151,2,0,4,1,2,0,2,1,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (152,4,0,3,1,3,0,2,2,0,2,2,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (153,3,1,4,4,2,0,2,2,1,1,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (154,3,1,4,2,2,0,2,1,1,3,3,1,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (155,4,1,4,3,3,0,2,1,0,3,2,3,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (156,2,1,4,4,2,0,0,3,1,2,1,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (157,3,1,4,2,2,0,2,3,0,1,1,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (158,3,1,4,4,2,0,2,3,0,2,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (159,4,1,3,1,2,0,0,2,0,2,1,1,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (160,2,1,2,1,1,1,0,2,0,1,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (161,4,1,4,2,3,0,2,2,1,1,1,3,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (162,2,0,3,1,2,0,0,2,0,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (163,3,0,4,1,2,0,2,1,0,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (164,2,1,3,2,2,1,0,3,0,1,1,2,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (165,3,1,4,3,2,0,0,2,1,1,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (166,2,0,2,3,2,1,2,2,1,1,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (167,1,1,4,2,2,0,2,2,1,1,1,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (168,2,0,2,1,1,0,0,1,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (169,4,1,3,4,2,0,0,1,1,3,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (170,2,1,4,4,2,0,2,1,1,1,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (171,3,0,4,4,2,0,0,2,1,1,2,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (172,3,0,4,4,3,0,2,2,0,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (173,3,1,4,4,2,0,2,1,0,3,2,2,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (174,3,1,4,4,2,0,0,1,1,2,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (175,2,1,4,1,2,1,0,2,0,1,1,3,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (176,3,1,4,3,1,0,2,1,1,3,2,1,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (177,2,1,3,3,3,0,0,2,0,2,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (178,2,1,3,3,2,1,2,3,0,1,1,3,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (179,2,1,4,2,2,0,2,2,0,1,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (180,3,0,4,3,3,0,2,2,1,2,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (181,2,1,1,4,2,0,2,3,0,1,1,2,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (182,3,1,1,4,2,0,2,2,0,4,3,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (183,3,0,4,4,3,0,2,2,0,1,1,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (184,3,0,2,4,1,0,0,3,0,1,1,2,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (185,2,1,3,2,2,1,0,3,0,1,3,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (186,4,1,2,4,2,0,0,1,1,1,2,3,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (187,2,1,2,5,2,0,2,3,0,1,1,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (188,4,1,3,4,2,0,2,2,0,3,2,3,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (189,2,1,3,2,1,0,0,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (190,2,1,4,4,2,0,0,1,1,4,2,3,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (191,3,0,4,3,2,1,0,1,0,2,2,3,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (192,4,0,3,2,2,0,2,1,0,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (193,4,1,4,1,2,0,2,1,1,1,2,2,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (194,4,1,1,4,2,1,2,1,0,1,2,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (195,2,0,4,3,2,0,2,2,1,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (196,2,0,2,2,2,0,0,2,0,2,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (197,3,1,1,4,2,0,2,1,0,1,1,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (198,2,0,4,1,2,0,2,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (199,3,0,4,4,3,0,0,2,1,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (200,3,1,3,4,1,1,0,3,0,1,1,1,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (201,3,0,3,4,3,0,0,1,0,1,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (202,2,1,4,1,2,0,0,2,0,1,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (203,2,1,4,4,3,0,2,2,1,1,2,3,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (204,3,1,4,2,2,0,2,1,1,3,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (205,2,1,4,4,2,0,2,1,1,1,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (206,3,1,2,3,2,0,0,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (207,3,0,4,4,2,0,0,2,1,2,2,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (208,1,0,3,2,2,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (209,1,1,1,2,2,0,0,3,1,4,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (210,2,1,3,3,2,0,2,2,0,3,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (211,4,0,4,4,2,1,0,2,1,2,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (212,2,1,4,1,2,0,0,2,0,1,1,1,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (213,3,1,1,2,1,0,2,2,0,2,2,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (214,2,0,2,1,2,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (215,2,0,4,3,2,0,2,2,1,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (216,3,0,4,3,3,0,0,1,0,3,2,2,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (217,3,1,4,3,2,0,2,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (218,2,0,3,1,2,0,2,3,1,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (219,2,0,3,1,2,0,2,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (220,1,0,3,1,1,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (221,2,1,4,2,2,0,0,1,1,3,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (222,3,0,4,1,2,0,0,2,1,2,2,2,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (223,1,0,2,1,2,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (224,2,1,4,1,2,0,0,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (225,4,0,3,4,2,0,0,3,0,1,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (226,2,1,4,1,2,0,2,1,1,1,2,1,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (227,4,1,4,1,2,0,2,1,1,1,1,1,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (228,2,0,3,3,1,0,2,2,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (229,3,0,4,4,3,0,1,1,1,4,2,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (230,2,1,3,1,1,0,2,1,0,1,1,3,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (231,4,0,2,2,2,0,2,1,1,1,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (232,2,0,3,4,2,0,0,2,0,1,1,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (233,2,1,4,2,2,0,2,1,1,4,2,2,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (234,3,1,4,3,2,1,2,1,1,2,3,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (235,2,1,4,2,2,0,2,2,0,1,1,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (236,2,0,2,3,2,0,0,2,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (237,2,1,2,2,2,0,0,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (238,2,1,2,1,2,0,0,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (239,2,0,2,2,3,0,0,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (240,2,0,4,3,2,0,0,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (241,3,1,1,3,2,0,0,2,0,3,2,2,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (242,3,0,3,2,1,1,0,1,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (243,4,1,4,2,2,0,0,1,0,2,2,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (244,3,1,4,1,2,0,0,2,0,1,1,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (245,2,1,4,1,2,0,2,1,1,2,2,1,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (246,2,1,4,2,2,0,0,2,0,2,1,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (247,3,1,2,2,2,1,2,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (248,3,1,4,1,2,0,0,1,1,2,2,0,6,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (249,3,1,4,4,2,0,0,1,0,3,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (250,3,1,4,2,2,0,0,1,1,1,2,1,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (251,2,0,3,2,2,0,2,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (252,2,1,4,1,3,0,0,3,0,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (253,2,0,3,2,2,0,0,3,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (254,4,0,4,1,2,0,0,2,0,1,1,2,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (255,4,0,3,4,1,0,1,1,0,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (256,4,1,2,4,2,0,2,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (257,3,1,2,2,2,0,0,2,0,1,1,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (258,2,0,3,1,2,0,0,2,0,1,2,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (259,3,0,2,3,3,1,2,2,0,1,1,2,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (260,3,0,1,4,2,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (261,2,1,3,2,2,0,0,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (262,3,1,4,3,1,0,2,1,1,4,2,1,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (263,2,1,4,3,3,0,0,1,1,2,2,0,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (264,3,1,3,2,2,1,0,1,0,3,2,1,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (265,2,1,4,4,2,0,0,3,0,1,1,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (266,2,1,3,3,1,0,0,2,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (267,3,1,4,4,2,0,2,1,1,2,1,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (268,4,1,4,4,2,0,2,1,0,3,1,0,6,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (269,2,1,4,4,3,0,0,1,1,2,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (270,4,0,4,1,1,0,0,1,0,2,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (271,3,1,1,3,2,0,0,2,0,1,1,2,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (272,3,1,1,4,2,0,2,2,0,1,2,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (273,4,0,3,4,2,0,2,2,0,1,2,1,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (274,1,0,3,3,2,0,0,2,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (275,3,1,2,4,2,0,2,2,0,1,1,1,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (276,3,0,4,3,1,0,0,1,0,1,2,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (277,3,1,4,1,3,0,0,2,1,3,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (278,2,1,3,3,2,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (279,3,0,4,2,2,0,1,1,1,3,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (280,1,1,2,2,1,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (281,3,1,4,4,2,0,0,2,0,1,1,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (282,3,1,4,1,3,0,1,2,0,4,3,3,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (283,3,0,4,4,2,1,2,2,1,3,2,2,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (284,3,1,2,3,2,0,2,2,0,1,1,0,7,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (285,3,1,2,2,2,0,0,2,0,1,3,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (286,4,1,3,4,2,0,2,2,0,1,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (287,3,0,2,3,3,0,0,2,0,2,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (288,2,1,4,2,1,0,0,2,1,3,3,0,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (289,3,1,4,4,1,0,2,2,1,4,1,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (290,3,0,4,2,1,0,0,1,1,1,2,0,3,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (291,2,1,2,2,1,0,0,3,0,1,1,0,3,0);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (292,3,1,4,4,1,1,2,1,0,2,2,2,6,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (293,3,0,4,4,2,0,0,1,1,1,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (294,2,1,1,1,2,0,0,1,0,2,2,0,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (295,4,1,4,4,1,1,0,2,0,4,2,2,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (296,3,1,4,3,1,0,0,1,1,2,2,1,7,1);
insert into mytable (id,age,sex,cpt,pressure,chol,sugar,ecg,maxbpm,angina,oldpeak,slope,flourosopy,thal,diagnosis) values (297,3,0,2,3,2,0,2,3,0,1,2,1,3,1);


ALTER TABLE ONLY mytable
  ADD CONSTRAINT mytable_pkey PRIMARY KEY (id);

-- ALTER TABLE ONLY country
--     ADD CONSTRAINT country_pkey PRIMARY KEY (code);

-- ALTER TABLE ONLY country_language
--     ADD CONSTRAINT country_language_pkey PRIMARY KEY (country_code, "language");

-- ALTER TABLE ONLY country
--     ADD CONSTRAINT country_capital_fkey FOREIGN KEY (capital) REFERENCES city(id);

-- ALTER TABLE ONLY country_language
--     ADD CONSTRAINT country_language_country_code_fkey FOREIGN KEY (country_code) REFERENCES country(code);

-- -- Added in 2.1
-- ALTER TABLE city
--     ADD CONSTRAINT country_fk
--     FOREIGN KEY (country_code) REFERENCES country (code);

-- COMMENT ON COLUMN country.gnp IS GNP is 'Gross national product';

COMMIT;

ANALYZE mytable;