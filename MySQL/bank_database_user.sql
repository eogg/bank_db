-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: bank_database
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `accountid` int NOT NULL,
  `accountname` varchar(100) NOT NULL,
  `dob` varchar(45) DEFAULT NULL,
  `pin_code` int NOT NULL,
  `balance` int DEFAULT NULL,
  PRIMARY KEY (`accountid`),
  UNIQUE KEY `accountid_UNIQUE` (`accountid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (153907,'Jacob Lesifko','03/13/2006',153909,150909),(192496,'Elian ghavdsakdlas','05/292/2909',5544,6555),(268441,'Joey flooooowers','05/21/2006',4455,7000),(290726,'Elai   ndsan',NULL,77616,1002),(349377,'Elian Garciaaaa','05/29/2006',4455,6000),(360835,'ndslkad dnskdlsa','05/29/2006',5544,5000),(368739,'Eldnsadnkals ','05/29/2006',9900,9900),(383306,'Elian GG','05/29/2006',4455,6000),(398441,'Rebbeca Fuentes','06/26/2006',483221,444),(426527,'Joey Flores','05/21/2006',1234,40),(443704,'Yugi','04/04/2044',4455,10000),(446957,'bdjskadb dbsjkdbjkas','05/29/2006',4455,445555),(504591,'dnskald dnskldas','05/29/2006',4455,6000),(546782,'Elian Garcia Part 2','05/29/2005',4455,6000),(691115,'Elian gdjabdksa',NULL,776633,1002),(729331,'Joey Flowers','05/21/2006',4321,6000),(766380,'Joseph Nathaniel Flores','05/21/2006',319628,3),(785065,' ','05/29/2006',8899,1400),(790361,'Elian GGGGG','05/29/2006',113377,1000),(794562,'dnskalda dsnakldlsank','05/29/2006',5544,6000),(808379,'Elian Garcia','05/29/2006',4455,500),(930535,'Riddick Carlson','08/29/2006',3232,6969),(936694,'Arctic Monkeys','05/29/2006',6655,-700);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-30 13:28:02
