-- task3/tourism_db.sql
-- Таблицы-справочники
CREATE TABLE Country (
    CountryID INT PRIMARY KEY AUTO_INCREMENT,
    CountryName VARCHAR(100) NOT NULL
);

CREATE TABLE City (
    CityID INT PRIMARY KEY AUTO_INCREMENT,
    CityName VARCHAR(100) NOT NULL,
    CountryID INT,
    FOREIGN KEY (CountryID) REFERENCES Country(CountryID)
);

CREATE TABLE Hotel (
    HotelID INT PRIMARY KEY AUTO_INCREMENT,
    HotelName VARCHAR(100),
    CityID INT,
    Stars INT CHECK (Stars BETWEEN 1 AND 5),
    FOREIGN KEY (CityID) REFERENCES City(CityID)
);

CREATE TABLE Service (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,
    ServiceName VARCHAR(100),
    Price DECIMAL(10,2)
);

-- Таблица переменной информации
CREATE TABLE TourOrder (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    HotelID INT,
    ServiceID INT,
    CustomerName VARCHAR(100),
    OrderDate DATE,
    TotalCost DECIMAL(10,2),
    FOREIGN KEY (HotelID) REFERENCES Hotel(HotelID),
    FOREIGN KEY (ServiceID) REFERENCES Service(ServiceID)
);