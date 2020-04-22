-- Check sql server version
select @@version

-- Change database owner name
use [DatabaseName] exec sp_changedbowner 'sa'


-- Creating a new dams table
create table dams (
	DamID INT IDENTITY(1,1) PRIMARY KEY,
	DamName VARCHAR(100),
	Height DECIMAL(3,2),
	Storage INT,
	Storage_Prec DECIMAL(3,2),
	Longitude FLOAT,
	Latitude FLOAT
)
-------------------------------------

-- Creating a new stations table
create table stations (
	StationID INT IDENTITY(1,1) PRIMARY KEY,
	StationName VARCHAR(100),
	Longitude FLOAT,
	Latitude FLOAT
)
------------------------------------------

-- Selecting all distinct dam names from Dams_level
select distinct(dam_name)
from Dams_level 
order by dam_name
--------------------------------------------

-- Inserting dam names into dams, fro Dams_level table
insert into dams (DamName)
	select distinct(dam_name)
	from Dams_level 
	order by dam_name
--------------------------------------------

-- Adding a new column that's also a primary key
alter table population_sum
add PopulationID INT IDENTITY(1,1) PRIMARY KEY
----------------------------------------------------

--Deleting/Dropping a column
alter table tname drop column colname

-- Changing the column data type after a failed data insertion
alter table dams
alter column Height varchar(50)
----------------------------------

-- Inserting data into dams table from Dams_level table
insert into dams (Height, Storage, Storage_Prec)
	select DL.height, DL.storage, DL.storage_prec
	from Dams_level DL
	INNER JOIN dams D
	ON DL.dam_name = D.DamName 
--------------------------------

-- Deleting null values 
delete from dams
where DamName IS NULL
---------------------------------

-- Adding a new column to dams
alter table dams add Longitude varshar(50)

---------------------------------------

-- Updating column info from a different table
update dams
	set Latitude = DAL.Latitude
	from ( dams
	INNER JOIN df_all_locations DAL
	on dams.DamName = DAL.[name])
----------------------------------------------

-- Dropping a table
drop table df_all_locations
---------------------------------------

-- Updating DamID's in Dams_level
update Dams_level
	set Dams_level.DamID = dams.DamID
	from (Dams_level
	INNER JOIN dams
	on Dams_level.dam_name = dams.DamName
-----------------------------------

-- Changing a column name
exec sp_rename 'consumption_uct.column_1', 'ConsumptionID', 'COLUMN'
-------------------------------------------------


-- Queries from a test that used the 'tmdb' database -------------------

select m.title, gm.genre_id, g.genre_name, km.keyword_id, k.keyword_name
from movies m
inner join GenreMap gm
on m.movie_id = gm.movie_id
inner join Genres g
on g.genre_id = gm.genre_id


inner join KeywordMap km
on km.movie_id = m.movie_id
inner join Keywords k
on km.keyword_id = k.keyword_id

where g.genre_name = 'Adventure'
and k.keyword_name = 'superhero'

------------

select title, popularity
from movies
where release_date between '2006-08-01' and '2007-10-01'
and popularity > 40
------------------------

select distinct c.characters
from Actors a
inner join Casts c
on c.actor_id = a.actor_id

where a.actor_name = 'Sean Bean'

-------------

select m.title, g.genre_name
from Movies m
inner join GenreMap gm
on gm.movie_id = m.movie_id
inner join Genres g
on g.genre_id = gm.genre_id

where m.title = 'Skyfall'
-----------------

select m.title, k.keyword_name, pc.production_country_name
from Movies m
inner join KeywordMap km
on km.movie_id = m.movie_id
inner join Keywords k
on k.keyword_id = km.keyword_id
inner join ProductionCountryMap pcm
on pcm.movie_id = m.movie_id
inner join ProductionCountries pc
on pc.iso_3166_1 = pcm.iso_3166_1


where k.keyword_name like '%spy%'
and pc.production_country_name = 'Fran??aise'

------------------------
with PP as (
select *
from Oscars o
where (o.[year] between '1990' and '2009')
and o.winner = 1.0
and o.award = 'Best Picture')

select sum(m.budget)
from PP
inner join Movies m
on m.title = PP.[name]


-------

(m.budget), o.award
select avg(m.runtime) as avgr, pc.production_company_name
from Movies m
inner join ProductionCompanyMap pcm
on pcm.movie_id = m.movie_id
inner join ProductionCompanies pc
on pc.production_company_id = pcm.production_company_id

group by pc.production_company_name

order by avgr desc
---------------------

select count(m.title) as number, k.keyword_name
from Movies m
inner join KeywordMap km
on km.movie_id = m.movie_id
inner join Keywords k
on k.keyword_id = km.keyword_id

group by k.keyword_name

order by number desc
--------------------------------------------------

select avg(m.popularity) as avgp, g.genre_name
from Movies m
inner join GenreMap gm
on gm.movie_id = m.movie_id
inner join Genres g
on g.genre_id = gm.genre_id

group by g.genre_name

order by avgp desc

--------------

select avg(m.revenue) as avgr, o.award
from Movies m
inner join Oscars o
on o.film = m.title

group by o.award

order by avgr desc

-------------------

select count(m.title) as cT, pc.production_country_name
from Movies m
inner join ProductionCountryMap pcm
on pcm.movie_id = m.movie_id
inner join ProductionCountries pc
on pc.iso_3166_1 = pcm.iso_3166_1

group by pc.production_country_name

order by cT desc

------------------------------------------------------------