-- Switch to the target database
USE home_db;

-- Table: Property
CREATE TABLE Property (
  property_id INT AUTO_INCREMENT PRIMARY KEY,
  address VARCHAR(255),
  sale_date DATE,
  building_area DECIMAL(12,2),
  lot_area DECIMAL(12,2),
  year_built INT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table: HOA
CREATE TABLE HOA (
  hoa_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  fee DECIMAL(10,2),
  contact_email VARCHAR(255),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Link Property to HOA
ALTER TABLE Property
  ADD COLUMN hoa_id INT,
  ADD FOREIGN KEY (hoa_id) REFERENCES HOA(hoa_id);

-- Table: Valuation
CREATE TABLE Valuation (
  valuation_id INT AUTO_INCREMENT PRIMARY KEY,
  property_id INT NOT NULL,
  valuation_amount DECIMAL(12,2),
  valuation_date DATE,
  source VARCHAR(255),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (property_id) REFERENCES Property(property_id)
);

-- Table: RehabEstimate
CREATE TABLE RehabEstimate (
  rehab_id INT AUTO_INCREMENT PRIMARY KEY,
  property_id INT NOT NULL,
  estimated_cost DECIMAL(12,2),
  description TEXT,
  estimate_date DATE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (property_id) REFERENCES Property(property_id)
);
