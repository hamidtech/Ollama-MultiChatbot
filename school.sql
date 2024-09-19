-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS school_chatbot;
USE school_chatbot;

-- Create PersonalInfo table
CREATE TABLE IF NOT EXISTS PersonalInfo (
    ID BIGINT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Gender ENUM('Male', 'Female'),
    Age INT,
    PostalCode VARCHAR(10)
);

-- Create Courses table
CREATE TABLE IF NOT EXISTS Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    CourseName VARCHAR(255) NOT NULL,
    Teacher VARCHAR(255)
);

-- Create Grades table with proper foreign key references
CREATE TABLE IF NOT EXISTS Grades (
    ID BIGINT,
    CourseID INT,
    Grade ENUM('A', 'B', 'C', 'D', 'E', 'F'),
    PRIMARY KEY (ID, CourseID),
    FOREIGN KEY (ID) REFERENCES PersonalInfo(ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Insert random data into PersonalInfo table
INSERT INTO PersonalInfo (ID, FirstName, LastName, Gender, Age, PostalCode) VALUES
(1234567890, 'John', 'Smith', 'Male', 17, '12345'),
(2345678901, 'Jane', 'Johnson', 'Female', 16, '23456'),
(3456789012, 'Alex', 'Williams', 'Male', 17, '34567'),
(4567890123, 'Chris', 'Jones', 'Male', 18, '45678'),
(5678901234, 'Katie', 'Brown', 'Female', 16, '56789'),
(6789012345, 'Michael', 'Davis', 'Male', 18, '12345'),
(7890123456, 'Sarah', 'Miller', 'Female', 17, '23456'),
(8901234567, 'David', 'Wilson', 'Male', 16, '34567'),
(9012345678, 'Emily', 'Moore', 'Female', 18, '45678'),
(1234567899, 'Daniel', 'Taylor', 'Male', 17, '56789');

-- Insert data into Courses table
INSERT INTO Courses (CourseName, Teacher) VALUES
('Mathematics', 'Dr. Smith'),
('Science', 'Dr. Johnson'),
('History', 'Dr. Brown'),
('Art', 'Dr. Wilson'),
('Physical Education', 'Coach Davis');

-- Insert random grades into Grades table
INSERT INTO Grades (ID, CourseID, Grade) VALUES
(1234567890, 1, 'A'),
(1234567890, 2, 'B'),
(1234567890, 3, 'C'),
(1234567890, 4, 'D'),
(1234567890, 5, 'A'),
(2345678901, 1, 'B'),
(2345678901, 2, 'C'),
(2345678901, 3, 'A'),
(2345678901, 4, 'B'),
(2345678901, 5, 'A');

-- Commit the transaction
COMMIT;
