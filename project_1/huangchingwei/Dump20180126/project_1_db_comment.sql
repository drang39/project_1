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
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` int(11) NOT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `food` varchar(100) DEFAULT NULL,
  `fan` int(11) NOT NULL,
  `product_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  `time` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `comment_product_id_id_20338de4_fk_product_id` (`product_id_id`),
  KEY `comment_user_id_id_fef6a1a2_fk_auth_user_id` (`user_id_id`),
  CONSTRAINT `comment_product_id_id_20338de4_fk_product_id` FOREIGN KEY (`product_id_id`) REFERENCES `product` (`id`),
  CONSTRAINT `comment_user_id_id_fef6a1a2_fk_auth_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (8,2,'2222','2',1,3,20,NULL),(12,1,'1','1',1,3,20,NULL),(13,5,'213','None',1,3,19,NULL),(14,0,'it\'s good','None',1,3,19,NULL),(15,5,'213214','None',1,3,19,'2018-01-23'),(16,4,'rr34','None',1,3,19,'2018-01-23'),(17,2,'good','None',1,8,18,'2018-01-23'),(18,2,'very good','None',1,9,18,'2018-01-23'),(20,4,'it\'s perfect to drink with friends','None',1,8,19,'2018-01-25'),(21,5,'1231','None',1,8,19,'2018-01-25'),(22,0,'12321','None',-1,8,19,'2018-01-25'),(23,5,'very good','None',1,6,19,'2018-01-25'),(24,5,'1231','None',1,3,20,'2018-01-25'),(25,5,'2313','None',1,7,20,'2018-01-25');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-26 11:17:14
