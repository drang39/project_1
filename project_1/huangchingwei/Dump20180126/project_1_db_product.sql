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
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `productname` varchar(40) NOT NULL,
  `rating` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `description` varchar(500) NOT NULL,
  `productimg` varchar(100) DEFAULT NULL,
  `brand_id_id` int(11) NOT NULL,
  `category_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_brand_id_id_3a15f341_fk_brand_id` (`brand_id_id`),
  KEY `product_category_id_id_4b7bb083_fk_category_id` (`category_id_id`),
  CONSTRAINT `product_brand_id_id_3a15f341_fk_brand_id` FOREIGN KEY (`brand_id_id`) REFERENCES `brand` (`id`),
  CONSTRAINT `product_category_id_id_4b7bb083_fk_category_id` FOREIGN KEY (`category_id_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (3,'Omnipollo ,\"Nebuchadnezzar\" Imperial IPA',5,189,' 以巴比倫空中庭園建造者：尼布甲尼撒（Nebuchadnezzar）為名，雞師傅締造了帝國IPA（Imperial IPA）的輝煌神蹟！2012年，斯德哥爾摩啤酒暨威士忌大賞金牌獎；2013年，Ratebeer評選瑞典最佳啤酒；2013年瑞典啤酒評選，30個你人生必喝的最棒IPA。','omnipollo iipa.jpg',4,2),(6,'Omnipollo ,\"Nebuchadnezzar\" Imperial IPA',5,189,' 以巴比倫空中庭園建造者：尼布甲尼撒（Nebuchadnezzar）為名，雞師傅締造了帝國IPA（Imperial IPA）的輝煌神蹟！2012年，斯德哥爾摩啤酒暨威士忌大賞金牌獎；2013年，Ratebeer評選瑞典最佳啤酒；2013年瑞典啤酒評選，30個你人生必喝的最棒IPA。\r\n\r\n 開瓶只有松針跟草，些許柑橘，但那濃得化不開的香氣迷霧，就算海市蜃樓也非跳進去不可！高強度的麥芽甜感充斥口腔，絲毫沒有凝滯的酒精感，就是要你鏘的徹底。','omnipollo iipa.jpg',4,2),(7,'Mirror Pond',4,149,'Since 1988, this refreshingly uncomplicated ale has inspired the simple moments that become extraordinary when shared. Crisp and clean with subtle hints of caramel, Mirror Pond is a delicious everyday ale whose straightforward single-hop character and smooth maltiness combine to deliver a timeless pale ale that’s best served in the moment and paired with a few good friends.','MirrorPond_New.png',3,7),(8,'Pacific Wonderland',3,149,'We’ve always believed the best way to respect tradition is to brew the unexpected. So when we set out to create a sessionable lager befitting of the Pacific Northwest, our sense of exploration led us to this dry-hopped wonder befitting of everyday adventure. Citrusy Mandarina Bavaria hops combine with the crisp, bright character of a traditional lager to deliver a beer that is truly refreshing, and undoubtedly worth sharing.','PacificWonderland.png',3,6),(9,'Black Mountain',3,149,'This is the beer that started it all. A rich, creamy mouthfeel complements a layered depth, revealing distinctive chocolate and coffee notes. Full of flavor, yet easy to drink','BlackButte_12oz_composite.png',3,3),(10,'Fresh squeezed',5,159,'his mouthwateringly delicious IPA gets its flavor from a heavy helping of citra and mosaic hops. Don’t worry, no fruit was harmed in the making of this beer.','36644_Deschutes_FreshSqueezed12_Comp_R5_SMP.png',3,2),(11,'Jubel Ale',4,159,'Warm spiciness and tradition grace this bold, complex winter ale. The deep garnet color pairs perfectly with holiday celebrations. To celebrate the 30th bottling, for the first time ever, this year’s packaging features not one, but a series of custom snowflake themed illustrations. ','jubelale-2017-with-ingredients.png',3,3);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
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
