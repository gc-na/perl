# [লিনাক্স] C Shell (csh) scp ব্যবহার: ফাইল স্থানান্তর করা

## Overview
`scp` কমান্ডটি নিরাপদ কপি করার জন্য ব্যবহৃত হয়। এটি SSH প্রোটোকল ব্যবহার করে একটি কম্পিউটার থেকে অন্য কম্পিউটারে ফাইল স্থানান্তর করতে সাহায্য করে।

## Usage
`scp` কমান্ডের মৌলিক সিনট্যাক্স হলো:

```bash
scp [options] [source] [destination]
```

## Common Options
- `-r`: ডিরেক্টরি এবং এর সমস্ত বিষয়বস্তু রিকার্সিভলি কপি করতে ব্যবহৃত হয়।
- `-P`: SSH পোর্ট নম্বর নির্দিষ্ট করতে ব্যবহৃত হয় (মৌলিক পোর্ট 22)।
- `-i`: নির্দিষ্ট SSH কী ফাইল ব্যবহার করতে ব্যবহৃত হয়।
- `-v`: ডিবাগ তথ্য দেখানোর জন্য ব্যবহৃত হয়, যা সমস্যা সমাধানে সহায়ক।

## Common Examples
- একটি ফাইল স্থানান্তর করা:
```bash
scp /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
```

- একটি ডিরেক্টরি স্থানান্তর করা:
```bash
scp -r /path/to/local/directory user@remote_host:/path/to/remote/directory/
```

- একটি নির্দিষ্ট পোর্ট ব্যবহার করে ফাইল স্থানান্তর করা:
```bash
scp -P 2222 /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
```

- SSH কী ফাইল ব্যবহার করে ফাইল স্থানান্তর করা:
```bash
scp -i /path/to/private_key.pem /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
```

## Tips
- স্থানান্তরের আগে নিশ্চিত করুন যে আপনি সঠিক ব্যবহারকারীর নাম এবং হোস্ট ঠিকানা ব্যবহার করছেন।
- বড় ফাইল স্থানান্তরের সময় `-v` অপশন ব্যবহার করে প্রক্রিয়ার অগ্রগতি পর্যবেক্ষণ করুন।
- নিরাপত্তার জন্য SSH কী ব্যবহার করা সবসময় ভাল অভ্যাস।