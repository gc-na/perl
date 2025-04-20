# [লিনাক্স] C Shell (csh) case ব্যবহার: শর্ত অনুযায়ী নির্দেশনা নির্বাচন

## Overview
`case` কমান্ডটি C Shell-এ শর্ত অনুযায়ী বিভিন্ন নির্দেশনা নির্বাচন করতে ব্যবহৃত হয়। এটি একটি নির্দিষ্ট প্যাটার্নের উপর ভিত্তি করে বিভিন্ন বিকল্পের মধ্যে নির্বাচন করতে সাহায্য করে।

## Usage
`case` কমান্ডের মৌলিক সিনট্যাক্স হলো:

```
case [options] [arguments]
```

## Common Options
- `in`: প্যাটার্নের শুরুতে ব্যবহৃত হয়, যা নির্দেশ করে কোন প্যাটার্নগুলোর সাথে মেলানো হবে।
- `esac`: `case` ব্লকটি শেষ করার জন্য ব্যবহৃত হয়।

## Common Examples
নিচে কিছু সাধারণ উদাহরণ দেওয়া হলো:

### উদাহরণ 1: সংখ্যা চেক করা
```csh
set num = 3
switch ($num)
case 1:
    echo "Number is one"
    breaksw
case 2:
    echo "Number is two"
    breaksw
case 3:
    echo "Number is three"
    breaksw
default:
    echo "Number is not one, two, or three"
endsw
```

### উদাহরণ 2: ফাইলের এক্সটেনশন চেক করা
```csh
set file = "document.txt"
case ($file)
(*.txt):
    echo "This is a text file."
    breaksw
(*.jpg):
    echo "This is a JPEG image."
    breaksw
(*):
    echo "Unknown file type."
endsw
```

### উদাহরণ 3: ব্যবহারকারীর ইনপুট চেক করা
```csh
echo "Enter a command (start/stop):"
set command = $<

switch ($command)
case start:
    echo "Starting the process..."
    breaksw
case stop:
    echo "Stopping the process..."
    breaksw
default:
    echo "Invalid command."
endsw
```

## Tips
- `case` কমান্ডটি ব্যবহার করার সময় নিশ্চিত করুন যে প্রতিটি `case` ব্লক সঠিকভাবে `breaksw` দিয়ে শেষ হচ্ছে।
- প্যাটার্নগুলি সঠিকভাবে চিহ্নিত করুন যাতে ভুল ফলাফল না আসে।
- `default` বিকল্পটি ব্যবহার করুন যাতে অপ্রত্যাশিত ইনপুটের জন্য একটি ডিফল্ট আউটপুট প্রদান করা যায়।