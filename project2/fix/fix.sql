-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: fix
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add car',7,'add_car'),(20,'Can change car',7,'change_car'),(21,'Can delete car',7,'delete_car'),(22,'Can add fix list',8,'add_fixlist'),(23,'Can change fix list',8,'change_fixlist'),(24,'Can delete fix list',8,'delete_fixlist'),(25,'Can add goods',9,'add_goods'),(26,'Can change goods',9,'change_goods'),(27,'Can delete goods',9,'delete_goods'),(28,'Can add user',10,'add_user'),(29,'Can change user',10,'change_user'),(30,'Can delete user',10,'delete_user'),(31,'Can add worker',11,'add_worker'),(32,'Can change worker',11,'change_worker'),(33,'Can delete worker',11,'delete_worker'),(34,'Can add power',12,'add_power'),(35,'Can change power',12,'change_power'),(36,'Can delete power',12,'delete_power');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$fpZTRLHVe7ln$WJ7nVNq/C5LPRV/7EMf8VgAf1A58bAcY5yoFjHahwUw=','2018-10-31 10:39:06.808954',1,'chilly','','','123@qq.com',1,1,'2018-10-27 06:45:13.811474'),(2,'pbkdf2_sha256$100000$lEKdSnvlCbhr$CFA19pPdGUbHSTYAVc3SO7haWEvYVND+FOgOWDq8qbY=','2018-10-31 10:38:31.759950',0,'6630050120','','','',0,1,'2018-10-27 06:52:22.438156');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carfix_car`
--

DROP TABLE IF EXISTS `carfix_car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `carfix_car` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `car_brand` varchar(32) NOT NULL,
  `car_broken_part` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=292 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carfix_car`
--

LOCK TABLES `carfix_car` WRITE;
/*!40000 ALTER TABLE `carfix_car` DISABLE KEYS */;
INSERT INTO `carfix_car` VALUES (11,'benchi','luntai'),(12,'benchi','yayay'),(13,'benchi','boli'),(14,'benchi','boli'),(15,'benchi','boli'),(55,'benchi','boli'),(56,'benchi','boli'),(57,'benchi','boli'),(58,'benchi','boli'),(59,'benchi','boli'),(60,'benchi','boli'),(61,'benchi','boli'),(62,'benchi','boli'),(63,'benchi','boli'),(64,'benchi','boli'),(65,'benchi','boli'),(66,'benchi','boli'),(67,'benchi','boli'),(68,'benchi','boli'),(69,'benchi','boli'),(70,'benchi','boli'),(71,'benchi','boli'),(72,'benchi','boli'),(73,'benchi','boli'),(74,'benchi','boli'),(75,'benchi','boli'),(76,'benchi','boli'),(77,'benchi','boli'),(78,'benchi','boli'),(79,'benchi','boli'),(80,'benchi','boli'),(81,'benchi','boli'),(82,'benchi','boli'),(83,'benchi','boli'),(84,'benchi','boli'),(85,'benchi','boli'),(86,'benchi','boli'),(87,'benchi','boli'),(88,'benchi','boli'),(89,'benchi','boli'),(90,'benchi','boli'),(91,'benchi','boli'),(92,'benchi','boli'),(93,'benchi','boli'),(94,'benchi','boli'),(95,'benchi','boli'),(96,'benchi','boli'),(97,'benchi','boli'),(98,'benchi','boli'),(99,'benchi','boli'),(100,'benchi','boli'),(101,'benchi','boli'),(102,'benchi','boli'),(103,'benchi','boli'),(104,'benchi','boli'),(105,'benchi','boli'),(106,'benchi','boli'),(107,'benchi','boli'),(108,'benchi','boli'),(109,'benchi','boli'),(110,'benchi','boli'),(111,'benchi','boli'),(112,'benchi','boli'),(113,'benchi','boli'),(118,'奔驰','轮胎'),(119,'奔驰','玻璃'),(120,'奔驰','轮胎'),(121,'奔驰','玻璃'),(122,'奥迪','123123'),(123,'奥迪','123123'),(124,'奥迪','123123'),(125,'奥迪','123123'),(126,'奥迪','123123'),(127,'奥迪','1'),(128,'奥迪','1'),(129,'奥迪','1'),(130,'奥迪','1'),(131,'奥迪','1'),(132,'奔驰','123123'),(133,'奔驰','123123'),(134,'奔驰','123123'),(135,'奔驰','123123'),(136,'奔驰','123123'),(137,'奔驰','123123'),(138,'奔驰','123123'),(139,'奔驰','123123'),(140,'奔驰','123123'),(141,'奥迪','123123'),(142,'奥迪','123123'),(143,'奥迪','123123'),(144,'奥迪','123123'),(145,'奥迪','123123'),(146,'奥迪','123123'),(147,'奥迪','123123'),(148,'奥迪','123123'),(149,'奔驰','123123'),(150,'奔驰','123123'),(151,'123','12'),(152,'123','12'),(153,'123','12'),(154,'123','12'),(155,'123','12'),(156,'123','12'),(157,'123','12'),(158,'123','12'),(159,'123','12'),(160,'123','12'),(161,'123','12'),(162,'123','12'),(163,'123','12'),(164,'123','12'),(165,'123','12'),(166,'123','123123'),(167,'123','123123'),(168,'123','123123'),(169,'123','123123'),(170,'奔驰','123123'),(171,'奔驰','123123'),(172,'123','123123'),(173,'123','123123'),(174,'123','123123'),(175,'123','123123'),(176,'123','123123'),(199,'123','123123'),(200,'奔驰','123123'),(201,'奔驰','123123'),(202,'奔驰','123123'),(203,'奔驰','123123'),(204,'奔驰','123123'),(205,'奔驰','123123'),(206,'奔驰','123123'),(207,'奔驰','123123'),(208,'奔驰','123123'),(209,'奔驰','123123'),(210,'奔驰','123123'),(211,'奔驰','123123'),(212,'奔驰','123123'),(213,'奔驰','123123'),(214,'奔驰','123123'),(215,'奥迪','玻璃'),(216,'123','123123'),(217,'奔驰','123123'),(218,'奔驰','123123'),(219,'奔驰','123123'),(220,'奔驰','123123'),(221,'奔驰','123123'),(222,'奔驰','123123'),(223,'奔驰','123123'),(224,'奔驰','123123'),(225,'奔驰','123123'),(226,'奔驰','123123'),(227,'奔驰','123123'),(228,'奔驰','123123'),(229,'奔驰','123123'),(230,'奔驰','123123'),(231,'奔驰','123123'),(232,'奔驰','123123'),(233,'奔驰','123123'),(234,'奔驰','123123'),(235,'奔驰','123123'),(236,'奔驰','123123'),(237,'奔驰','123123'),(238,'奥迪','123123'),(239,'奥迪','123123'),(240,'奔驰','123123'),(241,'奔驰','123123'),(242,'奔驰','玻璃'),(244,'213','213'),(245,'213','213'),(246,'213','213'),(247,'213','213'),(248,'213','213'),(249,'213','213'),(250,'213','213'),(251,'213','213'),(252,'213','213'),(253,'213','213'),(254,'奥迪','123123'),(255,'奥迪','123123'),(256,'奥迪','123123'),(257,'奔驰','玻璃'),(258,'123','123123'),(259,'123','123123'),(260,'奔驰','233'),(261,'奔驰','123123'),(262,'奔驰','123123'),(263,'奔驰','123123'),(264,'123','123123'),(265,'123','123123'),(269,'123','123'),(272,'奥迪','123123'),(273,'奔驰','123123'),(282,'123','玻璃'),(283,'奥迪','玻璃'),(284,'12313','玻璃'),(288,'奥迪','玻璃'),(291,'奔驰','all');
/*!40000 ALTER TABLE `carfix_car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carfix_fixlist`
--

DROP TABLE IF EXISTS `carfix_fixlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `carfix_fixlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` int(11) NOT NULL,
  `begin_fix_time` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  `worker_id` int(11) NOT NULL,
  `main_goods` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `carfix_fixlist_user_id_66c6aa8e_fk_carfix_user_id` (`user_id`),
  KEY `carfix_fixlist_worker_id_0d3e03ff_fk_carfix_worker_id` (`worker_id`),
  CONSTRAINT `carfix_fixlist_user_id_66c6aa8e_fk_carfix_user_id` FOREIGN KEY (`user_id`) REFERENCES `carfix_user` (`id`),
  CONSTRAINT `carfix_fixlist_worker_id_0d3e03ff_fk_carfix_worker_id` FOREIGN KEY (`worker_id`) REFERENCES `carfix_worker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carfix_fixlist`
--

LOCK TABLES `carfix_fixlist` WRITE;
/*!40000 ALTER TABLE `carfix_fixlist` DISABLE KEYS */;
INSERT INTO `carfix_fixlist` VALUES (5,123,'2018-10-28 00:56:44.112788',108,1,'3333'),(6,1231,'2018-10-28 00:57:43.684568',108,1,'123311'),(7,10000,'2018-10-28 00:59:36.529395',107,1,'轮胎'),(8,10000,'2018-10-28 01:01:06.900383',113,1,'123'),(9,123,'2018-10-28 03:30:29.287177',279,1,'23123'),(10,10000,'2018-10-28 03:30:52.665387',278,1,'零件'),(11,123,'2018-10-28 03:33:40.175117',268,1,'23123'),(12,123,'2018-10-28 03:35:04.871099',267,1,'123'),(13,10000,'2018-10-28 04:05:05.561475',264,1,'23123'),(14,123,'2018-10-28 04:08:49.867161',260,1,'23123'),(15,10000,'2018-10-28 07:27:28.771792',259,1,'23123'),(16,10000,'2018-10-28 07:38:07.056952',258,2,'yayya '),(17,123,'2018-10-28 07:38:23.606294',257,1,'111'),(18,123,'2018-10-28 07:38:33.745128',256,1,'123'),(19,10000,'2018-10-28 09:21:30.511951',255,2,'123'),(20,1231,'2018-10-28 09:21:53.519127',254,2,'123'),(21,10000,'2018-10-29 12:41:12.253445',283,2,'3'),(22,123,'2018-10-29 13:08:37.587199',253,2,'23123');
/*!40000 ALTER TABLE `carfix_fixlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carfix_goods`
--

DROP TABLE IF EXISTS `carfix_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `carfix_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(32) NOT NULL,
  `goods_price` int(11) NOT NULL,
  `goods_desciption` varchar(32) NOT NULL,
  `goods_count` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carfix_goods`
--

LOCK TABLES `carfix_goods` WRITE;
/*!40000 ALTER TABLE `carfix_goods` DISABLE KEYS */;
/*!40000 ALTER TABLE `carfix_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carfix_power`
--

DROP TABLE IF EXISTS `carfix_power`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `carfix_power` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(20) NOT NULL,
  `boss` tinyint(1) NOT NULL,
  `password` varchar(20) NOT NULL,
  `user_real_name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carfix_power`
--

LOCK TABLES `carfix_power` WRITE;
/*!40000 ALTER TABLE `carfix_power` DISABLE KEYS */;
INSERT INTO `carfix_power` VALUES (1,'6630050120',0,'12345678','王敏康'),(2,'chilly',1,'12345678','卫星');
/*!40000 ALTER TABLE `carfix_power` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carfix_user`
--

DROP TABLE IF EXISTS `carfix_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `carfix_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(32) NOT NULL,
  `user_tel` varchar(32) NOT NULL,
  `user_addr` varchar(32) NOT NULL,
  `user_car_id` int(11) NOT NULL,
  `is_made_order` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `carfix_user_user_car_id_e4b1f1ec_fk_carfix_car_id` (`user_car_id`),
  KEY `user_index` (`user_name`),
  CONSTRAINT `carfix_user_user_car_id_e4b1f1ec_fk_carfix_car_id` FOREIGN KEY (`user_car_id`) REFERENCES `carfix_car` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=287 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carfix_user`
--

LOCK TABLES `carfix_user` WRITE;
/*!40000 ALTER TABLE `carfix_user` DISABLE KEYS */;
INSERT INTO `carfix_user` VALUES (50,'chilly','10086','beijing',55,0),(51,'chilly','10086','beijing',56,0),(52,'chilly','10086','beijing',57,0),(53,'chilly','10086','beijing',58,0),(54,'chilly','10086','beijing',59,0),(55,'chilly','10086','beijing',60,0),(56,'chilly','10086','beijing',61,0),(57,'chilly','10086','beijing',62,0),(58,'chilly','10086','beijing',63,0),(59,'chilly','10086','beijing',64,0),(60,'chilly','10086','beijing',65,0),(61,'chilly','10086','beijing',66,0),(62,'chilly','10086','beijing',67,0),(63,'chilly','10086','beijing',68,0),(64,'chilly','10086','beijing',69,0),(65,'chilly','10086','beijing',70,0),(66,'chilly','10086','beijing',71,0),(67,'chilly','10086','beijing',72,0),(68,'chilly','10086','beijing',73,0),(69,'chilly','10086','beijing',74,0),(70,'chilly','10086','beijing',75,0),(71,'chilly','10086','beijing',76,0),(72,'chilly','10086','beijing',77,0),(73,'chilly','10086','beijing',78,0),(74,'chilly','10086','beijing',79,0),(75,'chilly','10086','beijing',80,0),(76,'chilly','10086','beijing',81,0),(77,'chilly','10086','beijing',82,0),(78,'chilly','10086','beijing',83,0),(79,'chilly','10086','beijing',84,0),(80,'chilly','10086','beijing',85,0),(81,'chilly','10086','beijing',86,0),(82,'chilly','10086','beijing',87,0),(83,'chilly','10086','beijing',88,0),(84,'chilly','10086','beijing',89,0),(85,'chilly','10086','beijing',90,0),(86,'chilly','10086','beijing',91,0),(87,'chilly','10086','beijing',92,0),(88,'chilly','10086','beijing',93,0),(89,'chilly','10086','beijing',94,0),(90,'chilly','10086','beijing',95,0),(91,'chilly','10086','beijing',96,0),(92,'chilly','10086','beijing',97,0),(93,'chilly','10086','beijing',98,0),(94,'chilly','10086','beijing',99,0),(95,'chilly','10086','beijing',100,0),(96,'chilly','10086','beijing',101,0),(97,'chilly','10086','beijing',102,0),(98,'chilly','10086','beijing',103,0),(99,'chilly','10086','beijing',104,0),(100,'chilly','10086','beijing',105,0),(101,'chilly','10086','beijing',106,0),(102,'chilly','10086','beijing',107,0),(103,'chilly','10086','beijing',108,0),(104,'chilly','10086','beijing',109,0),(105,'chilly','10086','beijing',110,0),(106,'chilly','10086','beijing',111,0),(107,'chilly','10086','beijing',112,1),(108,'chilly','10086','beijing',113,1),(113,'6630050120','测试用户2联系方式','深圳华强北',118,1),(114,'测试用户1','测试用户2联系方式','深圳华强北',119,0),(115,'6630050120','测试用户2联系方式','深圳华强北',120,0),(116,'123','测试用户2联系方式','深圳华强北',121,0),(117,'6630050120','测试用户2联系方式','深圳华强北',123,0),(118,'6630050120','测试用户2联系方式','深圳华强北',122,0),(119,'6630050120','测试用户2联系方式','深圳华强北',125,0),(120,'6630050120','测试用户2联系方式','深圳华强北',124,0),(121,'6630050120','测试用户2联系方式','深圳华强北',126,0),(122,'1231','123','123',127,0),(123,'1231','123','123',128,0),(124,'1231','123','123',129,0),(125,'1231','123','123',130,0),(126,'1231','123','123',131,0),(127,'6630050120','1231','123',132,0),(128,'6630050120','1231','123',133,0),(129,'6630050120','1231','123',134,0),(130,'6630050120','1231','123',135,0),(131,'6630050120','1231','123',136,0),(132,'6630050120','1231','123',137,0),(133,'6630050120','1231','123',138,0),(134,'6630050120','测试用户2联系方式','深圳华强北',140,0),(135,'6630050120','测试用户2联系方式','深圳华强北',139,0),(136,'123','123','深圳华强北',141,0),(137,'123','123','深圳华强北',142,0),(138,'123','123','深圳华强北',143,0),(139,'123','123','深圳华强北',144,0),(140,'123','123','深圳华强北',146,0),(141,'123','123','深圳华强北',145,0),(142,'123','123','深圳华强北',147,0),(143,'123','123','深圳华强北',148,0),(144,'123','123','123',149,0),(145,'123','123','123',150,0),(146,'123','123','123',152,0),(147,'123','123','123',151,0),(148,'123','123','123',153,0),(149,'123','123','123',154,0),(150,'123','123','123',155,0),(151,'123','123','123',156,0),(152,'123','123','123',157,0),(153,'123','123','123',158,0),(154,'123','123','123',159,0),(155,'123','123','123',161,0),(156,'123','123','123',160,0),(157,'123','123','123',162,0),(158,'123','123','123',163,0),(159,'123','123','123',165,0),(160,'123','123','123',164,0),(161,'1231','123','123',166,0),(162,'1231','123','123',167,0),(163,'1231','123','123',169,0),(164,'1231','123','123',168,0),(165,'123','15872998154','深圳华强北',170,0),(166,'123','15872998154','深圳华强北',171,0),(167,'123','123','123',173,0),(168,'123','123','123',172,0),(169,'123','123','123',174,0),(170,'123','123','123',175,0),(171,'123','123','123',176,0),(193,'1231','123','123',199,0),(195,'13','1231','123',200,0),(196,'13','1231','123',201,0),(197,'123','123','深圳华强北',203,0),(198,'123','123','深圳华强北',202,0),(199,'123','123','深圳华强北',205,0),(200,'123','123','深圳华强北',204,0),(201,'123','123','深圳华强北',206,0),(202,'123','123','深圳华强北',207,0),(203,'123','123','深圳华强北',209,0),(204,'123','123','深圳华强北',208,0),(205,'123','123','深圳华强北',210,0),(206,'123','123','深圳华强北',211,0),(207,'123','123','深圳华强北',213,0),(208,'123','123','深圳华强北',212,0),(209,'123','123','深圳华强北',214,0),(210,'123','123','123',215,0),(211,'123','123','123',216,0),(212,'6630050120','测试用户2联系方式','123',217,0),(213,'6630050120','测试用户2联系方式','123',218,0),(214,'6630050120','测试用户2联系方式','123',219,0),(215,'6630050120','测试用户2联系方式','123',220,0),(216,'6630050120','测试用户2联系方式','123',221,0),(217,'6630050120','测试用户2联系方式','123',222,0),(218,'6630050120','测试用户2联系方式','123',224,0),(219,'6630050120','测试用户2联系方式','123',223,0),(220,'6630050120','测试用户2联系方式','123',226,0),(221,'6630050120','测试用户2联系方式','123',225,0),(222,'6630050120','测试用户2联系方式','123',227,0),(223,'6630050120','测试用户2联系方式','123',228,0),(224,'6630050120','测试用户2联系方式','123',229,0),(225,'6630050120','测试用户2联系方式','123',230,0),(226,'6630050120','测试用户2联系方式','123',231,0),(227,'6630050120','测试用户2联系方式','123',232,0),(228,'6630050120','测试用户2联系方式','123',233,0),(229,'6630050120','测试用户2联系方式','深圳华强北',234,0),(230,'6630050120','测试用户2联系方式','深圳华强北',235,0),(231,'6630050120','测试用户2联系方式','深圳华强北',237,0),(232,'6630050120','测试用户2联系方式','深圳华强北',236,0),(233,'6630050120','123','深圳华强北',238,0),(234,'6630050120','123','深圳华强北',239,0),(235,'6630050120','123','深圳华强北',241,0),(236,'6630050120','123','深圳华强北',240,0),(237,'6630050120','123','123',242,0),(239,'123','123','123',244,0),(240,'123','123','123',245,0),(241,'123','123','123',247,0),(242,'123','123','123',246,0),(243,'123','123','123',248,0),(244,'123','123','123',249,0),(245,'123','123','123',250,0),(246,'123','123','123',251,0),(247,'123','123','123',252,0),(248,'123','123','123',253,0),(249,'6630050120','123','深圳华强北',254,0),(250,'6630050120','123','深圳华强北',255,0),(251,'6630050120','123','深圳华强北',256,0),(252,'123123','123','深圳华强北',257,0),(253,'123','123','123',258,1),(254,'123','123','123',259,1),(255,'6630050120','123','深圳华强北',260,1),(256,'6630050120','123','深圳华强北',261,1),(257,'6630050120','123','深圳华强北',262,1),(258,'6630050120','123','深圳华强北',263,1),(259,'123','123','123',264,1),(260,'123','123','123',265,1),(264,'123112','312312123','123',269,1),(267,'6630050120','123','深圳华强北',272,1),(268,'6630050120','测试用户2联系方式','深圳华强北',273,1),(277,'6630050120','123','深圳华强北',282,1),(278,'6630050120','测试用户2联系方式','深圳华强北',283,1),(279,'6630050120','123','深圳华强北',284,1),(283,'测试用户1','123','深圳华强北',288,1),(286,'chilly','15872998154','深圳华强北',291,0);
/*!40000 ALTER TABLE `carfix_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carfix_worker`
--

DROP TABLE IF EXISTS `carfix_worker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `carfix_worker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `worker_name` varchar(32) NOT NULL,
  `worker_tel` varchar(32) NOT NULL,
  `worker_addr` varchar(32) NOT NULL,
  `worker_positon` varchar(32) NOT NULL,
  `worker_type` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carfix_worker`
--

LOCK TABLES `carfix_worker` WRITE;
/*!40000 ALTER TABLE `carfix_worker` DISABLE KEYS */;
INSERT INTO `carfix_worker` VALUES (1,'王敏康','15872998154','北京市中关村','汽修员工',2),(2,'卫星','15788192351','北京市中关村','经理',1);
/*!40000 ALTER TABLE `carfix_worker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-10-27 06:46:26.293396','1','Power object (1)',1,'[{\"added\": {}}]',12,1),(2,'2018-10-27 06:47:03.973556','1','王敏康',1,'[{\"added\": {}}]',11,1),(3,'2018-10-27 06:47:28.730905','2','卫星',1,'[{\"added\": {}}]',11,1),(4,'2018-10-27 06:47:50.278395','1','奥迪',1,'[{\"added\": {}}]',7,1),(5,'2018-10-27 06:48:03.118219','2','奔驰',1,'[{\"added\": {}}]',7,1),(6,'2018-10-27 06:48:55.344804','1','测试用户1',1,'[{\"added\": {}}]',10,1),(7,'2018-10-27 06:49:14.979964','2','测试用户2',1,'[{\"added\": {}}]',10,1),(8,'2018-10-27 06:50:38.614007','2','Power object (2)',1,'[{\"added\": {}}]',12,1),(9,'2018-10-27 06:52:22.660169','2','6630050120',1,'[{\"added\": {}}]',4,1),(10,'2018-10-27 10:22:56.621051','1','2018-10-27 10:22:56.619051+00:00',1,'[{\"added\": {}}]',8,1),(11,'2018-10-27 12:17:15.035403','2','2018-10-27 12:17:15.034403+00:00',1,'[{\"added\": {}}]',8,1),(12,'2018-10-27 12:24:17.211666','3','2018-10-27 12:24:17.209666+00:00',1,'[{\"added\": {}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'carfix','car'),(8,'carfix','fixlist'),(9,'carfix','goods'),(12,'carfix','power'),(10,'carfix','user'),(11,'carfix','worker'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-10-27 06:42:10.461388'),(2,'auth','0001_initial','2018-10-27 06:42:13.472194'),(3,'admin','0001_initial','2018-10-27 06:42:14.267795'),(4,'admin','0002_logentry_remove_auto_add','2018-10-27 06:42:14.314595'),(5,'contenttypes','0002_remove_content_type_name','2018-10-27 06:42:14.813796'),(6,'auth','0002_alter_permission_name_max_length','2018-10-27 06:42:15.156997'),(7,'auth','0003_alter_user_email_max_length','2018-10-27 06:42:15.500197'),(8,'auth','0004_alter_user_username_opts','2018-10-27 06:42:15.531397'),(9,'auth','0005_alter_user_last_login_null','2018-10-27 06:42:15.812198'),(10,'auth','0006_require_contenttypes_0002','2018-10-27 06:42:15.843398'),(11,'auth','0007_alter_validators_add_error_messages','2018-10-27 06:42:15.874598'),(12,'auth','0008_alter_user_username_max_length','2018-10-27 06:42:16.623399'),(13,'auth','0009_alter_user_last_name_max_length','2018-10-27 06:42:16.997800'),(14,'carfix','0001_initial','2018-10-27 06:42:19.181804'),(15,'carfix','0002_auto_20181023_1131','2018-10-27 06:42:21.662208'),(16,'carfix','0003_remove_car_use_goods','2018-10-27 06:42:21.958609'),(17,'carfix','0004_remove_fixlist_car','2018-10-27 06:42:22.379809'),(18,'carfix','0005_fixlist_price','2018-10-27 06:42:22.520210'),(19,'carfix','0006_auto_20181023_1259','2018-10-27 06:42:22.551410'),(20,'carfix','0007_auto_20181023_1626','2018-10-27 06:42:23.643412'),(21,'carfix','0008_auto_20181023_1631','2018-10-27 06:42:25.251214'),(22,'carfix','0009_auto_20181023_1634','2018-10-27 06:42:26.358816'),(23,'carfix','0010_auto_20181023_1634','2018-10-27 06:42:27.888619'),(24,'carfix','0011_auto_20181023_1655','2018-10-27 06:42:28.029019'),(25,'carfix','0012_auto_20181023_1700','2018-10-27 06:42:28.294220'),(26,'carfix','0013_power_password','2018-10-27 06:42:28.403420'),(27,'carfix','0014_power_user_real_name','2018-10-27 06:42:28.543820'),(28,'carfix','0015_auto_20181023_2045','2018-10-27 06:42:29.152221'),(29,'sessions','0001_initial','2018-10-27 06:42:29.401822'),(30,'carfix','0016_user_is_made_order','2018-10-27 12:20:32.979793');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4v0ish75zn1s9gt6t3mg1cuzhjlmcc0l','ODJjZTBlYTYwZTA5ZjI3Mjk0YzNlMTI4YTk4NDRjNDkzNjRmOWNhODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxN2NiNzRlYzY3MmE1ZjgyN2E4OTI4ZTBjY2EyMWIxOGUzMmMxMGYxIn0=','2018-11-14 10:39:06.841956'),('maqchivw5ybcg6nwk9chcg8i1s6wyox1','ODJjZTBlYTYwZTA5ZjI3Mjk0YzNlMTI4YTk4NDRjNDkzNjRmOWNhODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxN2NiNzRlYzY3MmE1ZjgyN2E4OTI4ZTBjY2EyMWIxOGUzMmMxMGYxIn0=','2018-11-12 13:04:51.345608');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-31 18:49:42
