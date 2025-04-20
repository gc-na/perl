# [লিনাক্স] C Shell (csh) psql ব্যবহার: PostgreSQL ডেটাবেসের সাথে যোগাযোগ করা

## Overview
`psql` হল PostgreSQL ডেটাবেসের জন্য একটি ইন্টারেক্টিভ টার্মিনাল। এটি ব্যবহারকারীদের ডেটাবেসের সাথে যোগাযোগ করতে, প্রশ্ন করতে এবং ডেটা পরিচালনা করতে সক্ষম করে।

## Usage
`psql` কমান্ডের মৌলিক সিনট্যাক্স হল:

```bash
psql [options] [arguments]
```

## Common Options
- `-U username`: নির্দিষ্ট ব্যবহারকারীর নাম দিয়ে লগইন করে।
- `-d database`: নির্দিষ্ট ডেটাবেসে সংযোগ করে।
- `-h hostname`: নির্দিষ্ট হোস্টে সংযোগ করে।
- `-p port`: নির্দিষ্ট পোর্ট নম্বর ব্যবহার করে সংযোগ করে।
- `-c command`: একটি নির্দিষ্ট SQL কমান্ড চালায় এবং তারপর বেরিয়ে আসে।

## Common Examples
- PostgreSQL ডেটাবেসে সংযোগ করা:

```bash
psql -U myuser -d mydatabase
```

- একটি SQL কমান্ড চালানো:

```bash
psql -U myuser -d mydatabase -c "SELECT * FROM mytable;"
```

- একটি নির্দিষ্ট হোস্টে সংযোগ করা:

```bash
psql -U myuser -h localhost -d mydatabase
```

- ডেটাবেসের সমস্ত টেবিলের তালিকা দেখা:

```bash
psql -U myuser -d mydatabase -c "\dt"
```

## Tips
- `\q` কমান্ড ব্যবহার করে psql থেকে বেরিয়ে আসুন।
- SQL কমান্ডগুলি চালানোর সময় সঠিক সিনট্যাক্স নিশ্চিত করুন।
- ডেটাবেসের সাথে কাজ করার আগে ব্যাকআপ নেওয়া একটি ভাল অভ্যাস।