USE aicra

CREATE TABLE review_history(
 id INT IDENTITY(1,1) PRIMARY KEY,
 code NVARCHAR(MAX),
 message NVARCHAR(200),
 context_score INT,
 fragility_score INT,
 prediction NVARCHAR(200)
)