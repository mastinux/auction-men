-- MySQL dump 10.13  Distrib 5.6.19, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: auctions_db
-- ------------------------------------------------------
-- Server version	5.6.19-0ubuntu0.14.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(22,'Can add category',8,'add_category'),(23,'Can change category',8,'change_category'),(24,'Can delete category',8,'delete_category'),(25,'Can add product',9,'add_product'),(26,'Can change product',9,'change_product'),(27,'Can delete product',9,'delete_product'),(28,'Can add bid',10,'add_bid'),(29,'Can change bid',10,'change_bid'),(30,'Can delete bid',10,'delete_bid');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'',NULL,0,'mastinux','','','',0,1,'2015-07-01 17:08:36.215889'),(2,'',NULL,0,'neuro17','','','',0,1,'2015-07-01 17:15:50.961026'),(3,'pbkdf2_sha256$20000$Dx6z03mlBC4O$OUJ2ReiOjHyYybD6SB+v4437CDRil9DpYLxnuSSzcX0=','2015-07-19 07:17:40.225746',1,'auctionsuperuser','','','andrea.pantaleo.93@gmail.com',1,1,'2015-07-02 12:12:43.847264'),(4,'pbkdf2_sha256$20000$FnDb3mUjnSaL$9LR6qZzpzbmPuKECBx+0v18iJ3AP+3GqznRMAA/5/NU=',NULL,0,'alecot','','','',0,1,'2015-07-04 09:43:18.000000'),(5,'pbkdf2_sha256$20000$dwOwKdu8JqIp$gL3sZaPMqLsRB9rx5S0Yiw7zxbXwwdI5SGY1lNXj7Bk=',NULL,0,'annric','','','',0,1,'2015-07-04 09:43:49.500844'),(6,'pbkdf2_sha256$20000$4k8s3qXNmW6h$4avI1SujaJT/stS4QzRMGHsW4+nShURiF8LM0rZr6Ok=',NULL,0,'fedfra','','','',0,1,'2015-07-04 09:44:07.220565'),(7,'pbkdf2_sha256$20000$IbML165m3p2y$n6wC7Y4xFXu2RBLi2B4rSsqzYuGpzAQC7e8Ij7m8Sy8=',NULL,0,'hasben','','','',0,1,'2015-07-04 09:44:36.623047');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bidplacing_bid`
--

DROP TABLE IF EXISTS `bidplacing_bid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bidplacing_bid` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `bidding_time` datetime(6) NOT NULL,
  `bidder_id` int(11) NOT NULL,
  `product_name_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bidplacing_bid_c3db7c31` (`product_name_id`),
  KEY `bidplacing_bid_bidder_id_2d0f0f487c7a6fe9_fk_auth_user_id` (`bidder_id`),
  KEY `bidplacing_bid_product_name_id_5523526fb3a5e66e_uniq` (`product_name_id`),
  CONSTRAINT `bidplacing_bid_bidder_id_2d0f0f487c7a6fe9_fk_auth_user_id` FOREIGN KEY (`bidder_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `bidpla_product_name_id_5523526fb3a5e66e_fk_bidplacing_product_id` FOREIGN KEY (`product_name_id`) REFERENCES `bidplacing_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bidplacing_bid`
--

LOCK TABLES `bidplacing_bid` WRITE;
/*!40000 ALTER TABLE `bidplacing_bid` DISABLE KEYS */;
INSERT INTO `bidplacing_bid` VALUES (7,400,'2015-07-16 10:27:18.000000',4,5),(33,440,'2015-07-16 13:33:26.000000',7,5),(36,465,'2015-07-16 13:35:16.000000',6,5),(37,563,'2015-07-16 13:37:29.000000',4,9),(38,515,'2015-07-09 13:53:50.000000',4,6),(39,26,'2015-07-02 12:39:26.000000',4,6),(41,26,'2015-07-17 14:22:48.000000',5,5),(42,38,'2015-07-17 14:23:04.000000',5,8),(43,6,'2015-07-17 14:59:59.000000',4,20),(44,7,'2015-07-17 15:00:59.000000',7,20),(45,18,'2015-07-17 15:06:45.000000',7,7),(46,17,'2015-07-17 15:07:13.000000',7,11),(47,19,'2015-07-17 15:30:59.080364',6,11),(48,62,'2015-07-17 16:01:12.127282',5,7);
/*!40000 ALTER TABLE `bidplacing_bid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bidplacing_category`
--

DROP TABLE IF EXISTS `bidplacing_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bidplacing_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(255) NOT NULL,
  `level` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bidplacing_category_category_name_63a95a67ee9da101_uniq` (`category_name`),
  KEY `bidplacing__parent_id_1eee237a7df5300d_fk_bidplacing_category_id` (`parent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bidplacing_category`
--

LOCK TABLES `bidplacing_category` WRITE;
/*!40000 ALTER TABLE `bidplacing_category` DISABLE KEYS */;
INSERT INTO `bidplacing_category` VALUES (7,'Unlimited Instant Videos',0,NULL),(8,'Digital & Prime Music',0,NULL),(9,'Appstore for Android',0,NULL),(10,'Fire TV',0,NULL),(11,'Echo',0,NULL),(12,'Books & Audible',0,NULL),(13,'Amazon Cloud Drive',0,NULL),(14,'Movies, Music & Games',0,NULL),(15,'Kindle E-readers & Books',0,NULL),(16,'Electronics & Computers',0,NULL),(17,'Fire Tablets and Phone',0,NULL),(18,'Clothing, Shoes & Jewelry',0,NULL),(19,'Credit & Payment Products',0,NULL),(20,'Amazon Home Services',0,NULL),(21,'Toys, Kids & Baby',0,NULL),(22,'Automotive & Industrial',0,NULL),(23,'Beauty, Health & Grocery',0,NULL),(24,'Sports & Outdoors',0,NULL),(25,'Home, Garden & Tools',0,NULL),(26,'Books',1,12),(27,'Kindle Books',1,12),(28,'Children\'s Books',1,12),(29,'Textbooks',1,12),(30,'Magazines',1,12),(31,'Sell Us Your Books',1,12),(32,'Audible Membership',1,12),(33,'Audible Audiobooks & More',1,12),(34,'Whispersync for Voice',1,12),(35,'Women',1,18),(36,'Men',1,18),(37,'Girls',1,18),(38,'Boys',1,18),(39,'Baby',1,18),(40,'Luggage',1,18),(41,'Apps',1,9),(42,'Games',1,9),(43,'Free App of the Day',1,9),(44,'Amazon Coins',1,9),(45,'Download Amazon Appstore',1,9);
/*!40000 ALTER TABLE `bidplacing_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bidplacing_product`
--

DROP TABLE IF EXISTS `bidplacing_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bidplacing_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `start_price` double NOT NULL,
  `deadline_time` datetime(6) NOT NULL,
  `category_id` int(11) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `insertion_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bidplacin_category_id_3e431972bc8d3e87_fk_bidplacing_category_id` (`category_id`),
  KEY `bidplacing_product_seller_id_397504dc9830eaec_fk_auth_user_id` (`seller_id`),
  CONSTRAINT `bidplacing_product_seller_id_397504dc9830eaec_fk_auth_user_id` FOREIGN KEY (`seller_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `bidplacin_category_id_3e431972bc8d3e87_fk_bidplacing_category_id` FOREIGN KEY (`category_id`) REFERENCES `bidplacing_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bidplacing_product`
--

LOCK TABLES `bidplacing_product` WRITE;
/*!40000 ALTER TABLE `bidplacing_product` DISABLE KEYS */;
INSERT INTO `bidplacing_product` VALUES (5,'Cards Against Humanity','',25,'2015-07-17 09:46:22.000000',21,6,'2015-07-16 15:19:32.981809'),(6,'Cards Against Humanity: First Expansion','',10,'2015-07-09 09:48:16.000000',21,5,'2015-07-16 15:19:32.981809'),(7,'Crazy Balloons','',13,'2015-07-18 09:48:48.000000',21,4,'2015-07-16 15:19:32.981809'),(8,'Fujifilm Instax Mini Instant Film','',37.95,'2015-07-18 09:49:24.000000',16,4,'2015-07-16 15:19:32.981809'),(9,'GoPro HERO','',129.99,'2015-07-18 23:59:59.000000',16,3,'2015-07-16 15:19:32.981809'),(10,'GoPro HERO4 SILVER','',399.99,'2015-07-25 09:50:33.000000',16,2,'2015-07-16 15:19:32.981809'),(11,'Humans of New York: Stories','',15.7,'2015-07-29 09:51:15.000000',12,1,'2015-07-16 15:19:32.981809'),(12,'Go Set a Watchman: A Novel','',14.49,'2015-07-18 09:51:42.000000',12,6,'2015-07-16 15:19:32.981809'),(13,'Grey: Fifty Shades of Grey as Told by Christian','',9.89,'2015-07-18 09:52:10.000000',12,5,'2015-07-16 15:19:32.981809'),(14,'Ray-Ban RB2132 New Wayfarer Sunglasses','',81.9,'2015-07-25 09:52:41.000000',18,4,'2015-07-16 15:19:32.981809'),(15,'U.S. Polo Assn. Men\'s Solid Polo Shirt with Small Pony','',13.41,'2015-07-18 09:53:07.000000',18,3,'2015-07-16 15:19:32.981809'),(16,'Dockers Men\'s Alpha Khaki Slim Flat-Front Pant','',21.99,'2015-07-31 09:55:05.000000',18,2,'2015-07-16 15:19:32.981809'),(17,'Title (Deluxe)','',12.99,'2015-07-15 10:20:07.000000',8,4,'2015-07-16 15:19:32.981809'),(18,'Uptown Special [Explicit]','',7.99,'2015-07-16 09:21:16.000000',8,1,'2015-07-16 15:19:32.981809'),(19,'Talking Is Hard','',12.99,'2015-07-10 09:22:04.000000',8,5,'2015-07-16 15:19:32.981809'),(20,'Popular Science','',5,'2015-07-16 15:24:31.000000',30,6,'2015-07-16 15:24:52.657343'),(21,'National Geographic','',19,'2015-07-18 15:28:54.000000',30,7,'2015-07-16 15:29:03.871440'),(26,'prodotto non scaduto','',1,'2015-07-19 14:48:00.000000',8,4,'2015-07-18 14:47:05.667878');
/*!40000 ALTER TABLE `bidplacing_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-07-02 13:24:31.041036','4','Accessori',3,'',8,3),(2,'2015-07-02 13:25:58.495264','6','Music Store',1,'',8,3),(5,'2015-07-02 13:38:11.908836','1','Motosega',1,'',9,3),(6,'2015-07-02 13:38:27.003065','1','Motosega',2,'Changed description.',9,3),(7,'2015-07-02 13:51:26.619670','2','CD FooFighers',1,'',9,3),(8,'2015-07-02 13:51:57.300794','3','ktm 125',1,'',9,3),(9,'2015-07-02 13:52:57.366037','4','Pala meccanica',1,'',9,3),(10,'2015-07-04 09:30:37.706135','6','Music Store',3,'',8,3),(11,'2015-07-04 09:30:37.771600','5','Moto',3,'',8,3),(12,'2015-07-04 09:30:37.805644','2','Giardinaggio',3,'',8,3),(13,'2015-07-04 09:30:37.850058','1','Musica Digitale',3,'',8,3),(14,'2015-07-04 09:34:53.048989','7','Unlimited Instant Videos',1,'',8,3),(15,'2015-07-04 09:35:17.623084','8','Digital & Prime Music',1,'',8,3),(16,'2015-07-04 09:35:27.475152','9','Appstore for Android',1,'',8,3),(17,'2015-07-04 09:35:35.762046','10','Fire TV',1,'',8,3),(18,'2015-07-04 09:35:41.770348','11','Echo',1,'',8,3),(19,'2015-07-04 09:35:50.554592','12','Books & Audible',1,'',8,3),(20,'2015-07-04 09:35:58.918826','13','Amazon Cloud Drive',1,'',8,3),(21,'2015-07-04 09:36:05.973975','14','Movies, Music & Games',1,'',8,3),(22,'2015-07-04 09:36:12.902060','15','Kindle E-readers & Books',1,'',8,3),(23,'2015-07-04 09:36:22.043156','16','Electronics & Computers',1,'',8,3),(24,'2015-07-04 09:36:28.068734','17','Fire Tablets and Phone',1,'',8,3),(25,'2015-07-04 09:36:47.208008','18','Clothing, Shoes & Jewelry',1,'',8,3),(26,'2015-07-04 09:36:52.640042','19','Credit & Payment Products',1,'',8,3),(27,'2015-07-04 09:36:57.736882','20','Amazon Home Services',1,'',8,3),(28,'2015-07-04 09:37:03.471793','21','Toys, Kids & Baby',1,'',8,3),(29,'2015-07-04 09:37:14.398400','22','Automotive & Industrial',1,'',8,3),(30,'2015-07-04 09:37:20.275778','23','Beauty, Health & Grocery',1,'',8,3),(31,'2015-07-04 09:37:27.562809','24','Sports & Outdoors',1,'',8,3),(32,'2015-07-04 09:37:33.339908','25','Home, Garden & Tools',1,'',8,3),(33,'2015-07-04 09:43:18.595662','4','alecot',1,'',4,3),(34,'2015-07-04 09:43:32.320279','4','alecot',2,'No fields changed.',4,3),(35,'2015-07-04 09:43:49.529788','5','annric',1,'',4,3),(36,'2015-07-04 09:44:07.250199','6','fedfra',1,'',4,3),(37,'2015-07-04 09:44:36.654534','7','hasben',1,'',4,3),(42,'2015-07-04 09:47:41.118926','5','Cards Against Humanity',1,'',9,3),(43,'2015-07-04 09:48:28.521966','6','Cards Against Humanity: First Expansion',1,'',9,3),(44,'2015-07-04 09:48:55.400292','7','Crazy Balloons',1,'',9,3),(45,'2015-07-04 09:49:52.885368','8','Fujifilm Instax Mini Instant Film',1,'',9,3),(46,'2015-07-04 09:50:17.198602','9','GoPro HERO',1,'',9,3),(47,'2015-07-04 09:50:40.273534','10','GoPro HERO4 SILVER',1,'',9,3),(48,'2015-07-04 09:51:24.453229','11','Humans of New York: Stories',1,'',9,3),(49,'2015-07-04 09:51:53.724996','12','Go Set a Watchman: A Novel',1,'',9,3),(50,'2015-07-04 09:52:18.446569','13','Grey: Fifty Shades of Grey as Told by Christian',1,'',9,3),(51,'2015-07-04 09:52:51.782868','14','Ray-Ban RB2132 New Wayfarer Sunglasses',1,'',9,3),(52,'2015-07-04 09:53:14.881612','15','U.S. Polo Assn. Men\'s Solid Polo Shirt with Small Pony',1,'',9,3),(53,'2015-07-04 09:55:13.093894','16','Dockers Men\'s Alpha Khaki Slim Flat-Front Pant',1,'',9,3),(54,'2015-07-15 07:38:24.491477','26','Books',1,'',8,3),(55,'2015-07-15 07:38:46.137707','27','Kindle Books',1,'',8,3),(56,'2015-07-15 07:38:58.777981','28','Children\'s Books',1,'',8,3),(57,'2015-07-15 07:39:09.122739','29','Textbooks',1,'',8,3),(58,'2015-07-15 07:39:19.046394','30','Magazines',1,'',8,3),(59,'2015-07-15 07:39:29.480764','31','Sell Us Your Books',1,'',8,3),(60,'2015-07-15 07:39:38.492531','32','Audible Membership',1,'',8,3),(61,'2015-07-15 07:39:48.478420','33','Audible Audiobooks & More',1,'',8,3),(62,'2015-07-15 07:39:58.910101','34','Whispersync for Voice',1,'',8,3),(63,'2015-07-15 07:52:24.106194','35','Women',1,'',8,3),(64,'2015-07-15 07:52:32.316393','36','Men',1,'',8,3),(65,'2015-07-15 07:52:41.417075','37','Girls',1,'',8,3),(66,'2015-07-15 07:52:48.276835','38','Boys',1,'',8,3),(67,'2015-07-15 07:52:56.474131','39','Baby',1,'',8,3),(68,'2015-07-15 07:53:06.469008','40','Luggage',1,'',8,3),(69,'2015-07-15 07:53:34.472726','41','Apps',1,'',8,3),(70,'2015-07-15 07:53:39.946534','42','Games',1,'',8,3),(71,'2015-07-15 07:53:50.436032','43','Free App of the Day',1,'',8,3),(72,'2015-07-15 07:54:02.139169','44','Amazon Coins',1,'',8,3),(73,'2015-07-15 07:54:13.646487','45','Download Amazon Appstore',1,'',8,3),(74,'2015-07-15 08:15:08.185598','11','Humans of New York: Stories',2,'Changed deadline_time.',9,3),(75,'2015-07-15 08:15:19.342904','16','Dockers Men\'s Alpha Khaki Slim Flat-Front Pant',2,'Changed deadline_time.',9,3),(76,'2015-07-15 09:20:52.024155','17','Title (Deluxe)',1,'',9,3),(77,'2015-07-15 09:21:43.011998','18','Uptown Special [Explicit]',1,'',9,3),(78,'2015-07-15 09:22:11.895977','19','Talking Is Hard',1,'',9,3),(79,'2015-07-16 10:27:20.224839','7','Cards Against Humanity alecot 400.0 2015-07-16 10:27:18+00:00',1,'',10,3),(80,'2015-07-16 10:27:51.571678','8','Cards Against Humanity: First Expansion annric 62.0 2015-07-16 10:27:50+00:00',1,'',10,3),(81,'2015-07-16 10:37:54.314965','12','Humans of New York: Stories fedfra 500.0 2015-07-16 10:34:25+00:00',1,'',10,3),(82,'2015-07-16 12:07:27.743107','16','Crazy Balloons annric 440.0 2015-07-16 12:04:04+00:00',1,'',10,3),(83,'2015-07-16 12:07:43.197883','16','Crazy Balloons annric 440.0 2015-07-16 12:04:04+00:00',3,'',10,3),(84,'2015-07-16 12:07:43.245103','12','Humans of New York: Stories fedfra 500.0 2015-07-16 10:34:25+00:00',3,'',10,3),(85,'2015-07-16 12:07:43.278707','8','Cards Against Humanity: First Expansion annric 62.0 2015-07-16 10:27:50+00:00',3,'',10,3),(86,'2015-07-16 12:28:50.780062','22','Title (Deluxe) annric 440.0 2015-07-16 12:23:58.691603+00:00',3,'',10,3),(87,'2015-07-16 13:33:27.077703','33','5 hasben 6165.0 2015-07-16 13:33:26+00:00',1,'',10,3),(88,'2015-07-16 13:34:45.076426','33','Cards Against Humanity hasben 440.0 2015-07-16 13:33:26+00:00',2,'Changed amount.',10,3),(89,'2015-07-16 13:35:01.752642','34','Cards Against Humanity annric 460.0 2015-07-16 13:35:00+00:00',1,'',10,3),(90,'2015-07-16 13:35:21.335968','35','Cards Against Humanity fedfra 465.0 2015-07-16 13:35:16+00:00',1,'',10,3),(91,'2015-07-16 13:35:40.218261','36','Cards Against Humanity fedfra 465.0 2015-07-16 13:35:16+00:00',1,'',10,3),(92,'2015-07-16 13:36:01.012898','35','Cards Against Humanity fedfra 465.0 2015-07-16 13:35:16+00:00',3,'',10,3),(93,'2015-07-16 13:37:31.053166','37','GoPro HERO alecot 561.0 2015-07-16 13:37:29+00:00',1,'',10,3),(94,'2015-07-16 13:53:52.951840','38','Cards Against Humanity: First Expansion alecot 515.0 2015-07-09 13:53:50+00:00',1,'',10,3),(95,'2015-07-16 14:13:59.565848','6','Cards Against Humanity: First Expansion',2,'Changed deadline_time.',9,3),(96,'2015-07-16 15:24:52.659099','20','Popular Science 5.0 2015-07-16 15:24:31+00:00 fedfra',1,'',9,3),(97,'2015-07-16 15:29:03.873314','21','National Geographic 19.0 2015-07-30 15:28:54+00:00 hasben',1,'',9,3),(98,'2015-07-17 12:39:31.770175','39','Cards Against Humanity: First Expansion [start_price=10.0 deadline=2015-07-09 09:48:16+00:00 seller=annric] bidder=alecot amount=26.0 bidding_time=2015-07-02 12:39:26+00:00',1,'',10,3),(99,'2015-07-17 14:17:45.921013','40','National Geographic [start_price=19.0 deadline=2015-07-30 15:28:54+00:00 seller=hasben] bidder=annric amount=20.0 bidding_time=2015-07-17 14:17:43+00:00',1,'',10,3),(100,'2015-07-17 14:22:36.589704','40','National Geographic [start_price=19.0 deadline=2015-07-30 15:28:54+00:00 seller=hasben] bidder=annric amount=20.0 bidding_time=2015-07-17 14:17:43+00:00',3,'',10,3),(101,'2015-07-17 14:22:36.623272','34','Cards Against Humanity [start_price=25.0 deadline=2015-07-18 09:46:22+00:00 seller=fedfra] bidder=annric amount=460.0 bidding_time=2015-07-16 13:35:00+00:00',3,'',10,3),(102,'2015-07-17 14:22:49.607071','41','Cards Against Humanity [start_price=25.0 deadline=2015-07-18 09:46:22+00:00 seller=fedfra] bidder=annric amount=26.0 bidding_time=2015-07-17 14:22:48+00:00',1,'',10,3),(103,'2015-07-17 14:23:05.549771','42','Fujifilm Instax Mini Instant Film [start_price=37.95 deadline=2015-07-18 09:49:24+00:00 seller=alecot] bidder=annric amount=38.0 bidding_time=2015-07-17 14:23:04+00:00',1,'',10,3),(104,'2015-07-17 15:00:00.541440','43','Popular Science [start_price=5.0 deadline=2015-07-16 15:24:31+00:00 seller=fedfra] bidder=alecot amount=6.0 bidding_time=2015-07-17 14:59:59+00:00',1,'',10,3),(105,'2015-07-17 15:01:00.715272','44','Popular Science [start_price=5.0 deadline=2015-07-16 15:24:31+00:00 seller=fedfra] bidder=hasben amount=7.0 bidding_time=2015-07-17 15:00:59+00:00',1,'',10,3),(106,'2015-07-17 15:03:46.904232','5','Cards Against Humanity [start_price=25.0 deadline=2015-07-17 09:46:22+00:00 seller=fedfra]',2,'Changed deadline_time.',9,3),(107,'2015-07-17 15:06:56.650829','45','Crazy Balloons [start_price=13.0 deadline=2015-07-18 09:48:48+00:00 seller=alecot] bidder=hasben amount=18.0 bidding_time=2015-07-17 15:06:45+00:00',1,'',10,3),(108,'2015-07-17 15:07:14.588222','46','Humans of New York: Stories [start_price=15.7 deadline=2015-07-29 09:51:15+00:00 seller=mastinux] bidder=hasben amount=17.0 bidding_time=2015-07-17 15:07:13+00:00',1,'',10,3),(109,'2015-07-17 15:15:47.267016','22','prodotto prova [start_price=25.0 deadline=2015-07-17 15:15:38+00:00 seller=mastinux]',1,'',9,3),(110,'2015-07-17 15:21:46.486890','None','prodotto prova 2 [start_price=65.0 deadline=2015-07-17 15:21:40+00:00 seller=annric]',1,'',9,3),(111,'2015-07-17 15:24:15.881375','10','Fire TV [parent:None, level=0]',2,'No fields changed.',8,3),(112,'2015-07-17 15:24:25.606910','None','prodotto prova 2 [start_price=-1.0 deadline=2015-07-17 15:23:55+00:00 seller=fedfra]',1,'',9,3),(113,'2015-07-17 15:24:53.542460','None','prodotto prova 2 [start_price=65.0 deadline=2015-07-17 15:24:45+00:00 seller=fedfra]',1,'',9,3),(114,'2015-07-17 15:25:40.551662','23','prodotto prova 2 [start_price=20.0 deadline=2015-07-18 15:25:29+00:00 seller=fedfra]',1,'',9,3),(115,'2015-07-17 15:30:59.084217','47','Humans of New York: Stories [start_price=15.7 deadline=2015-07-29 09:51:15+00:00 seller=mastinux] bidder=fedfra amount=19.0 bidding_time=2015-07-17 15:30:59.080364+00:00',1,'',10,3),(116,'2015-07-17 16:01:12.129551','48','Crazy Balloons [start_price=13.0 deadline=2015-07-18 09:48:48+00:00 seller=alecot] bidder=annric amount=62.0 bidding_time=2015-07-17 16:01:12.127282+00:00',1,'',10,3),(117,'2015-07-17 16:03:53.262699','49','GoPro HERO [start_price=129.99 deadline=2015-07-18 09:50:10+00:00 seller=auctionsuperuser] bidder=mastinux amount=560.0 bidding_time=2015-07-17 16:03:53.260198+00:00',1,'',10,3),(118,'2015-07-17 16:04:12.881004','49','GoPro HERO [start_price=129.99 deadline=2015-07-18 09:50:10+00:00 seller=auctionsuperuser] bidder=mastinux amount=560.0 bidding_time=2015-07-17 16:03:53.260198+00:00',3,'',10,3),(119,'2015-07-17 16:04:42.633054','None','GoPro HERO [start_price=129.99 deadline=2015-07-18 09:50:10+00:00 seller=auctionsuperuser] bidder=neuro17 amount=560.0 bidding_time=None',1,'',10,3),(120,'2015-07-18 13:17:13.997207','24','prodotto prova 3 [start_price=0.0 deadline=2015-07-22 13:17:08+00:00 seller=annric]',1,'',9,3),(121,'2015-07-18 13:20:25.817976','24','prodotto prova 3 [start_price=0.0 deadline=2015-07-22 13:17:08+00:00 seller=annric]',3,'',9,3),(122,'2015-07-18 13:20:25.870672','23','prodotto prova 2 [start_price=20.0 deadline=2015-07-18 15:25:29+00:00 seller=fedfra]',3,'',9,3),(123,'2015-07-18 13:20:25.903942','22','prodotto prova [start_price=25.0 deadline=2015-07-17 15:15:38+00:00 seller=mastinux]',3,'',9,3),(124,'2015-07-18 13:20:57.790111','9','GoPro HERO [start_price=129.99 deadline=2015-07-18 23:59:59+00:00 seller=auctionsuperuser]',2,'Changed deadline_time.',9,3),(125,'2015-07-18 13:48:46.141914','37','GoPro HERO [start_price=129.99 deadline=2015-07-18 23:59:59+00:00 seller=auctionsuperuser] bidder=alecot amount=563.0 bidding_time=2015-07-16 13:37:29+00:00',2,'Changed amount.',10,3),(126,'2015-07-18 14:39:17.785994','25','prodotto prova [start_price=15.0 deadline=2015-07-24 14:39:11+00:00 seller=annric]',1,'',9,3),(127,'2015-07-18 14:42:48.796238','21','National Geographic [start_price=19.0 deadline=2015-07-18 15:28:54+00:00 seller=hasben]',2,'Changed deadline_time.',9,3),(128,'2015-07-18 14:47:05.668722','26','prodotto scaduto [start_price=1.0 deadline=2015-07-18 14:48:00+00:00 seller=alecot]',1,'',9,3),(129,'2015-07-18 14:48:29.481125','26','prodotto non scaduto [start_price=1.0 deadline=2015-07-19 14:48:00+00:00 seller=alecot]',2,'Changed product_name and deadline_time.',9,3),(130,'2015-07-18 14:49:48.587720','25','prodotto prova [start_price=15.0 deadline=2015-07-24 14:39:11+00:00 seller=annric]',3,'',9,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(10,'bidplacing','bid'),(8,'bidplacing','category'),(9,'bidplacing','product'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-07-01 15:42:35.334065'),(2,'auth','0001_initial','2015-07-01 15:42:41.835556'),(3,'admin','0001_initial','2015-07-01 15:42:43.538124'),(4,'contenttypes','0002_remove_content_type_name','2015-07-01 15:42:44.671046'),(5,'auth','0002_alter_permission_name_max_length','2015-07-01 15:42:45.276416'),(6,'auth','0003_alter_user_email_max_length','2015-07-01 15:42:45.916490'),(7,'auth','0004_alter_user_username_opts','2015-07-01 15:42:45.965526'),(8,'auth','0005_alter_user_last_login_null','2015-07-01 15:42:46.510842'),(9,'auth','0006_require_contenttypes_0002','2015-07-01 15:42:46.544165'),(10,'bidplacing','0001_initial','2015-07-01 15:42:51.309689'),(11,'bidplacing','0002_auto_20150701_1541','2015-07-01 15:42:55.544127'),(12,'bidplacing','0003_auto_20150701_1542','2015-07-01 15:42:56.419282'),(13,'sessions','0001_initial','2015-07-01 15:42:56.946482'),(14,'bidplacing','0004_auto_20150701_1554','2015-07-01 15:54:36.172487'),(15,'bidplacing','0005_auto_20150701_1633','2015-07-01 16:33:13.992378'),(16,'bidplacing','0006_auto_20150704_1026','2015-07-04 10:26:30.353423'),(17,'bidplacing','0007_auto_20150716_1332','2015-07-16 13:32:21.805829'),(18,'bidplacing','0008_auto_20150716_1334','2015-07-16 13:34:10.671748'),(19,'bidplacing','0009_product_insertion_time','2015-07-16 15:20:43.691693'),(20,'bidplacing','0010_auto_20150716_1520','2015-07-16 15:20:43.790724'),(21,'bidplacing','0011_auto_20150717_1528','2015-07-17 15:28:11.827079');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('hyrk88yl8yorv7pi6brqvkyabrjwehzs','N2E0MmIyZDc1Mjk2NmJjZDMwNDMyYTRkZjNlNjc3YTI3NThmZDg1Nzp7Il9hdXRoX3VzZXJfaGFzaCI6ImRmYzA1MjE4YzMwNDk1Yzk1MjdlMDdiYzQ1ZTZkYWU5ZWE2MTc3ZWUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2015-07-18 09:04:35.003981');
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

-- Dump completed on 2015-07-19  9:35:25
