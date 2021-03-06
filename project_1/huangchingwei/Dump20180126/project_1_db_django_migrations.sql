-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: project_1_db
-- ------------------------------------------------------
-- Server version	5.7.19-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-01-08 06:34:48.933071'),(2,'auth','0001_initial','2018-01-08 06:34:53.811487'),(3,'admin','0001_initial','2018-01-08 06:34:55.413042'),(4,'admin','0002_logentry_remove_auto_add','2018-01-08 06:34:55.438106'),(5,'contenttypes','0002_remove_content_type_name','2018-01-08 06:34:56.143374'),(6,'auth','0002_alter_permission_name_max_length','2018-01-08 06:34:56.732630'),(7,'auth','0003_alter_user_email_max_length','2018-01-08 06:34:57.182886'),(8,'auth','0004_alter_user_username_opts','2018-01-08 06:34:57.200900'),(9,'auth','0005_alter_user_last_login_null','2018-01-08 06:34:57.770513'),(10,'auth','0006_require_contenttypes_0002','2018-01-08 06:34:57.803632'),(11,'auth','0007_alter_validators_add_error_messages','2018-01-08 06:34:57.879273'),(12,'auth','0008_alter_user_username_max_length','2018-01-08 06:34:58.995768'),(13,'auth','0009_alter_user_last_name_max_length','2018-01-08 06:34:59.500455'),(14,'sessions','0001_initial','2018-01-08 06:34:59.831147'),(15,'member','0001_initial','2018-01-12 06:41:36.588630'),(17,'beer','0002_brand','2018-01-18 12:57:09.381069'),(18,'beer','0003_auto_20180118_2055','2018-01-18 12:57:09.396730'),(19,'beer','0004_category','2018-01-18 13:30:16.435238'),(20,'beer','0001_initial','2018-01-19 02:45:21.308717'),(21,'beer','0002_comment','2018-01-22 02:55:34.271751'),(22,'beer','0003_comment_time','2018-01-23 05:59:39.190588'),(23,'beer','0004_order','2018-01-26 02:16:01.994610');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-26 11:17:16
