-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: job
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `applicants`
--

DROP TABLE IF EXISTS `applicants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `applicants` (
  `AID` int NOT NULL,
  `AName` varchar(20) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `DateApplied` date NOT NULL,
  `JobTitle` varchar(50) NOT NULL,
  `Qualification` varchar(50) DEFAULT NULL,
  `Experience` int DEFAULT NULL,
  `EmpStatus` varchar(30) NOT NULL,
  `CStatus` varchar(30) NOT NULL DEFAULT 'NEW',
  `City` varchar(50) NOT NULL,
  PRIMARY KEY (`AID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applicants`
--

LOCK TABLES `applicants` WRITE;
/*!40000 ALTER TABLE `applicants` DISABLE KEYS */;
INSERT INTO `applicants` VALUES (1580,'Sonakshi','sonakshis@gmail.com','F','2022-05-31','Accountant','B.Com',3,'Y','NEW','Mumbai'),(4010,'Pranjal','pranja32l@gmail.com','M','2023-05-30','Graphic Designer','B.Tech',2,'N','Hired','Delhi'),(4376,'Aadarsh Singh','aadarshsin@outlook.in','M','2023-05-30','Editor','BCA',3,'N','NEW','Mumbai'),(7347,'Priya','priya09@gmail.com','F','2020-08-05','Business Admin','B.com',1,'N','Hired','Lucknow');
/*!40000 ALTER TABLE `applicants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `applied`
--

DROP TABLE IF EXISTS `applied`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `applied` (
  `ApID` int NOT NULL,
  `ApName` varchar(50) NOT NULL,
  `CoID` int NOT NULL,
  `JT` varchar(50) NOT NULL,
  `Loc` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applied`
--

LOCK TABLES `applied` WRITE;
/*!40000 ALTER TABLE `applied` DISABLE KEYS */;
INSERT INTO `applied` VALUES (7347,'Priya',11022,'Business Admin','Lucknow'),(4010,'Pranjal',37846,'Graphic Designer','Delhi');
/*!40000 ALTER TABLE `applied` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `CID` int NOT NULL,
  `CName` varchar(50) NOT NULL,
  `CEmail` varchar(50) NOT NULL,
  `Qualification` varchar(50) DEFAULT NULL,
  `CJobTitle` varchar(50) NOT NULL,
  `Exp` int DEFAULT NULL,
  `Vacancy` int DEFAULT NULL,
  `City` varchar(50) NOT NULL,
  PRIMARY KEY (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (11022,'Hpt Com','hptcom@hotmail.com','B.Com','Business Admin',1,0,'Lucknow'),(30287,'Webgen','webgen12@outlook.in','M.Tech','Web Designer',3,2,'Bhopal'),(37846,'Pro Designers','prodesigners@outlook.in','B.Tech','Graphic Designer',1,1,'Delhi'),(48866,'Pilote','pilote@yahoo.com','M.Tech','Cyber Security',4,2,'New Delhi'),(48876,'Lenovo','lenovo123@gmail.com','B.Tech','Web Developer',3,29,'Delhi');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-31  1:11:09
