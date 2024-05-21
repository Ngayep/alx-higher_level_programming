-- This script converts the hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- Convert the database character set and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the hbtn_0c_0 database
USE hbtn_0c_0;

-- Convert the character set and collation of the table first_table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the character set and collation of the field name in the table first_table
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
