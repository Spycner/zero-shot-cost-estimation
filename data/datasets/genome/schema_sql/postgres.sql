

DROP TABLE IF EXISTS "ATT_CLASSES";

CREATE TABLE "ATT_CLASSES" (
  "ATT_CLASS_ID" integer  DEFAULT 0,
  "ATT_CLASS" char(50) ,
  PRIMARY KEY ("ATT_CLASS_ID")
) ;

DROP TABLE IF EXISTS "IMG_OBJ";

CREATE TABLE "IMG_OBJ" (
  "IMG_ID" integer  DEFAULT 0,
  "OBJ_SAMPLE_ID" integer  DEFAULT 0,
  "OBJ_CLASS_ID" integer DEFAULT NULL,
  "X" integer DEFAULT NULL,
  "Y" integer DEFAULT NULL,
  "W" integer DEFAULT NULL,
  "H" integer DEFAULT NULL,
  PRIMARY KEY ("IMG_ID","OBJ_SAMPLE_ID")
) ;

DROP TABLE IF EXISTS "IMG_OBJ_ATT";

CREATE TABLE "IMG_OBJ_ATT" (
  "IMG_ID" integer  DEFAULT 0,
  "ATT_CLASS_ID" integer  DEFAULT 0,
  "OBJ_SAMPLE_ID" integer  DEFAULT 0,
  PRIMARY KEY ("IMG_ID","ATT_CLASS_ID","OBJ_SAMPLE_ID")
) ;

DROP TABLE IF EXISTS "IMG_REL";

CREATE TABLE "IMG_REL" (
  "IMG_ID" integer  DEFAULT 0,
  "PRED_CLASS_ID" integer  DEFAULT 0,
  "OBJ1_SAMPLE_ID" integer  DEFAULT 0,
  "OBJ2_SAMPLE_ID" integer  DEFAULT 0,
  PRIMARY KEY ("IMG_ID","PRED_CLASS_ID","OBJ1_SAMPLE_ID","OBJ2_SAMPLE_ID")
) ;

DROP TABLE IF EXISTS "OBJ_CLASSES";

CREATE TABLE "OBJ_CLASSES" (
  "OBJ_CLASS_ID" integer  DEFAULT 0,
  "OBJ_CLASS" char(50) ,
  PRIMARY KEY ("OBJ_CLASS_ID")
) ;

DROP TABLE IF EXISTS "PRED_CLASSES";

CREATE TABLE "PRED_CLASSES" (
  "PRED_CLASS_ID" integer  DEFAULT 0,
  "PRED_CLASS" char(100) ,
  PRIMARY KEY ("PRED_CLASS_ID")
) ;

