# [লিনাক্স] C Shell (csh) sqlite3 ব্যবহার: SQLite ডেটাবেস পরিচালনা করা

## Overview
sqlite3 কমান্ডটি SQLite ডেটাবেসের সাথে কাজ করার জন্য ব্যবহৃত হয়। এটি একটি লাইটওয়েট ডেটাবেস ইঞ্জিন যা SQL (Structured Query Language) ব্যবহার করে ডেটাবেস তৈরি, পড়া, আপডেট এবং মুছে ফেলার জন্য ব্যবহৃত হয়।

## Usage
sqlite3 কমান্ডের মৌলিক সিনট্যাক্স নিম্নরূপ:

```csh
sqlite3 [options] [arguments]
```

## Common Options
- `-help`: সাহায্য তথ্য প্রদর্শন করে।
- `-version`: sqlite3 এর সংস্করণ তথ্য দেখায়।
- `-init <file>`: একটি নির্দিষ্ট ফাইল থেকে কমান্ডগুলি লোড করে।
- `-batch`: ব্যাচ মোডে কাজ করে, যেখানে কমান্ড লাইনের আউটপুট সরাসরি প্রদর্শিত হয়।

## Common Examples
1. একটি নতুন SQLite ডেটাবেস তৈরি করা:
   ```csh
   sqlite3 mydatabase.db
   ```

2. একটি টেবিল তৈরি করা:
   ```csh
   sqlite3 mydatabase.db "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);"
   ```

3. ডেটা সন্নিবেশ করা:
   ```csh
   sqlite3 mydatabase.db "INSERT INTO users (name) VALUES ('Alice');"
   ```

4. টেবিল থেকে ডেটা নির্বাচন করা:
   ```csh
   sqlite3 mydatabase.db "SELECT * FROM users;"
   ```

5. একটি টেবিল মুছে ফেলা:
   ```csh
   sqlite3 mydatabase.db "DROP TABLE users;"
   ```

## Tips
- ডেটাবেস ফাইলের ব্যাকআপ নেওয়া নিশ্চিত করুন, বিশেষ করে যখন আপনি গুরুত্বপূর্ণ ডেটা পরিচালনা করছেন।
- SQL কমান্ডগুলি একাধিক লাইনে লিখতে পারেন, তবে প্রতিটি লাইনের শেষে সেমিকোলন (`;`) রাখতে ভুলবেন না।
- `-init` অপশন ব্যবহার করে প্রাথমিক স্ক্রিপ্ট চালানোর মাধ্যমে ডেটাবেস সেটআপ সহজতর করুন।