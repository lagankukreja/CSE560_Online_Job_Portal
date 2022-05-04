--Company Tables

CREATE TABLE public."Country"(
 country_id INTEGER PRIMARY KEY NOT NULL
 ,country_name VARCHAR(100) NOT NULL
 );
CREATE TABLE public."State"(
 country_id INTEGER NOT NULL REFERENCES public."Country" ON DELETE CASCADE ON UPDATE CASCADE
 ,state_id INTEGER PRIMARY KEY NOT NULL
 ,state_name VARCHAR(50) NOT NULL
 ,FOREIGN KEY(country_id) REFERENCES public."Country"(country_id)
 );
CREATE TABLE public."Skill"(
 skill_id INTEGER PRIMARY KEY NOT NULL
 ,skill_name VARCHAR(50) NOT NULL
 ); 
CREATE TABLE public."Experience"(
 experience_id INTEGER PRIMARY KEY NOT NULL
 ,experience_name VARCHAR(100) NOT NULL
 );
CREATE TABLE public."Company"(
 company_id INTEGER PRIMARY KEY NOT NULL
 ,company_name VARCHAR(100) NOT NULL
 ,company_email VARCHAR(100) NOT NULL
 ,state_id INTEGER NOT NULL REFERENCES public."State" ON DELETE CASCADE ON UPDATE CASCADE
 ,country_id INTEGER NOT NULL REFERENCES public."Country" ON DELETE CASCADE ON UPDATE CASCADE
 ,FOREIGN KEY(state_id) REFERENCES public."State"(state_id)
 ,FOREIGN KEY(country_id) REFERENCES public."Country"(country_id)
 );
CREATE TABLE public."Salary"(
 salary_id INTEGER PRIMARY KEY NOT NULL
 ,salary_group VARCHAR(100) NOT NULL
 );
CREATE TABLE public."Jobs"(
 job_id SERIAL PRIMARY KEY NOT NULL
 ,job_title VARCHAR(50) NOT NULL
 ,job_desc VARCHAR(50) NOT NULL
 ,company_id INTEGER NOT NULL REFERENCES public."Company" ON DELETE CASCADE ON UPDATE CASCADE
 ,salary_id INTEGER NOT NULL REFERENCES public."Salary" ON DELETE CASCADE ON UPDATE CASCADE 
 ,job_state INTEGER NOT NULL REFERENCES public."State" ON DELETE CASCADE ON UPDATE CASCADE 
 ,job_country INTEGER NOT NULL REFERENCES public."Country" ON DELETE CASCADE ON UPDATE CASCADE 
 ,experience_id INTEGER NOT NULL REFERENCES public."Experience" ON DELETE CASCADE ON UPDATE CASCADE 
 ,FOREIGN KEY(company_id) REFERENCES public."Company"(company_id)
 ,FOREIGN KEY(salary_id) REFERENCES public."Salary"(salary_id)
 ,FOREIGN KEY(job_state) REFERENCES public."State"(state_id)
 ,FOREIGN KEY(job_country) REFERENCES public."Country"(country_id)
 ,FOREIGN KEY(experience_id) REFERENCES public."Experience"(experience_id)
 );
 
 --Applicant Tables
 
CREATE TABLE public."Gender"(
 gender_id INTEGER PRIMARY KEY NOT NULL
 ,gender_name VARCHAR(100) NOT NULL
 );
 CREATE TABLE public."Race"(
 race_id INTEGER PRIMARY KEY NOT NULL
 ,race_name VARCHAR(100) NOT NULL
 );
 CREATE TABLE public."Education"(
 education_id INTEGER PRIMARY KEY NOT NULL
 ,education_level VARCHAR(100) NOT NULL
 );
 CREATE TABLE public."Applicant"(
 applicant_id SERIAL PRIMARY KEY NOT NULL
 ,applicant_name  VARCHAR(100) NOT NULL
 ,applicant_email VARCHAR(100) NOT NULL
 ,education_id INTEGER NOT NULL REFERENCES public."Education" ON DELETE CASCADE ON UPDATE CASCADE
 ,age INTEGER NOT NULL
 ,gender_id INTEGER NOT NULL REFERENCES public."Gender" ON DELETE CASCADE ON UPDATE CASCADE
 ,race_id INTEGER NOT NULL REFERENCES public."Race" ON DELETE CASCADE ON UPDATE CASCADE
 ,skill_id INTEGER NOT NULL REFERENCES public."Skill" ON DELETE CASCADE ON UPDATE CASCADE
 ,work_authorization VARCHAR(10) NOT NULL
 ,state_id INTEGER NOT NULL REFERENCES public."State" ON DELETE CASCADE ON UPDATE CASCADE
 ,country_id INTEGER NOT NULL REFERENCES public."Country" ON DELETE CASCADE ON UPDATE CASCADE  
 ,job_state_id INTEGER NOT NULL REFERENCES public."State" ON DELETE CASCADE ON UPDATE CASCADE
 ,job_country_id INTEGER NOT NULL REFERENCES public."Country" ON DELETE CASCADE ON UPDATE CASCADE
 ,expected_salary_id INTEGER NOT NULL REFERENCES public."Salary" ON DELETE CASCADE ON UPDATE CASCADE
 ,FOREIGN KEY(education_id) REFERENCES public."Education"(education_id)
 ,FOREIGN KEY(gender_id) REFERENCES public."Gender"(gender_id)
 ,FOREIGN KEY(race_id) REFERENCES public."Race"(race_id)
 ,FOREIGN KEY(skill_id) REFERENCES public."Skill"(skill_id)
 ,FOREIGN KEY(state_id) REFERENCES public."State"(state_id)
 ,FOREIGN KEY(country_id) REFERENCES public."Country"(country_id)
 ,FOREIGN KEY(job_state_id) REFERENCES public."State"(state_id)
 ,FOREIGN KEY(job_country_id) REFERENCES public."Country"(country_id)
 ,FOREIGN KEY(expected_salary_id) REFERENCES public."Salary"(salary_id)
 );
