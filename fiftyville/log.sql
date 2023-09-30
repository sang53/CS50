-- 28/07/21 Humphrey Street
-- Look at tables & relations
.schema

-- find description of robbery
SELECT description
  FROM crime_scene_reports
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND street LIKE "Humphrey%";
-- Robbery took place 10:15am, 3 witness interviews

-- find interviews mentioned by witnesses
SELECT transcript
  FROM interviews
 WHERE year = 2021
   AND month = 7
   AND day = 28;
-- Exit from bakery 10:15-10:25
-- <1min call leaving bakery to purchase earliest flight ticket 29/7
-- withdraw some money from ATM on Legget Street earlier 29/7

-- find license plates at time of robbery (10:15-10:25)
SELECT license_plate
  FROM bakery_security_logs
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND hour = 10
   AND minute BETWEEN 15 AND 25
   AND activity = "exit";

-- find phone call after robbery
SELECT caller
  FROM phone_calls
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND duration < 60;

-- find account number from ATM earlier 28/7/21 on Leggett Street
SELECT account_number, atm_location
  FROM atm_transactions
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND atm_location LIKE "Leggett%"
   AND transaction_type = "withdraw";

-- get person_id from account_number
SELECT person_id
  FROM bank_accounts
 WHERE account_number IN
       (SELECT account_number
          FROM atm_transactions
         WHERE year = 2021
           AND month = 7
           AND day = 28
           AND atm_location LIKE "Leggett%"
           AND transaction_type = "withdraw");

-- Find person_id & name from license & phone number
SELECT id, name, phone_number, passport_number
  FROM people
 WHERE phone_number IN
       (SELECT caller
          FROM phone_calls
         WHERE year = 2021
           AND month = 7
           AND day = 28
           AND duration < 60)
   AND license_plate IN
       (SELECT license_plate
          FROM bakery_security_logs
         WHERE year = 2021
           AND month = 7
           AND day = 28
           AND hour = 10
           AND minute BETWEEN 15 AND 25
           AND activity = "exit")
   AND id IN
       (SELECT person_id
          FROM bank_accounts
         WHERE account_number IN
                (SELECT account_number
                   FROM atm_transactions
                  WHERE year = 2021
                    AND month = 7
                    AND day = 28
                    AND atm_location LIKE "Leggett%"
                    AND transaction_type = "withdraw"));
-- 2 suspects:
-- Name: Diana, Ph: (770) 555-1861, ID: 514354, Passport: 3592750733
-- Name: Bruce, Ph: (367) 555-5533, ID: 686048, Passport: 5773159633

-- Look for flight
SELECT flight_id, passport_number
  FROM passengers
 WHERE passport_number = 3592750733
    OR passport_number = 5773159633;
-- Diana - 18, 24, 54
-- Bruce - 36

-- find these flights that are on 29/7 and their destinations
SELECT destination_airport_id, hour, minute, id, origin_airport_id
  FROM flights
 WHERE (id = 18
    OR id = 24
    OR id = 36
    OR id = 54)
   AND year = 2021
   AND month = 7
   AND day = 29;
-- Diana - origin: 8, destination: 6, time: 4pm
-- Bruce - origin: 8, destination: 4, time: 8:20am

-- find name of origin & destination airports
SELECT full_name, city, id
  FROM airports
 WHERE id = 8
    OR id = 4
    OR id = 6;
-- 8: Fiftyville Regional Airport, Fiftyville
-- 6: Logan International Airport, Boston
-- 4: LaGuardia Airport, New York City

-- find if these flights are the earliest to destination
SELECT id, hour, minute, destination_airport_id
  FROM flights
 WHERE year = 2021
   AND month = 7
   AND day = 29
   AND origin_airport_id = 8
 ORDER BY hour, minute;
-- flight 36 is the earliest flight from airport 8
-- flight 18 is earliest flight to airport 6 from 8

-- Look for the ph of their accomplice
SELECT receiver, caller
  FROM phone_calls
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND duration < 60
   AND (caller = '(770) 555-1861' OR caller = '(367) 555-5533');
-- Diana - (725) 555-3243
-- Bruce - (375) 555-8161

-- find name of accomplice
SELECT name, phone_number
  FROM people
 WHERE phone_number IN
      (SELECT receiver
         FROM phone_calls
        WHERE year = 2021
          AND month = 7
          AND day = 28
          AND duration < 60
          AND (caller = '(770) 555-1861' OR caller = '(367) 555-5533'));
-- Diana - Philiip
-- Bruce - Robin

-- Most likely suspect (as flight is first of 29/08/21) -
-- Suspect: Bruce, Accomplice: Robin, Destination: LaGuardia Airport