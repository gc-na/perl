# [লিনাক্স] C Shell (csh) switch ব্যবহার: একটি শর্ত পরিবর্তন করার জন্য

## Overview
`switch` কমান্ডটি C Shell-এ একটি শর্ত পরিবর্তন করার জন্য ব্যবহৃত হয়। এটি বিভিন্ন শর্তের ভিত্তিতে বিভিন্ন কার্যকলাপ সম্পাদন করতে সহায়তা করে।

## Usage
`switch` কমান্ডের মৌলিক সিনট্যাক্স হলো:

```csh
switch (expression)
    case pattern1:
        commands1
        breaksw
    case pattern2:
        commands2
        breaksw
    default:
        default_commands
endsw
```

## Common Options
- `case pattern:`: নির্দিষ্ট প্যাটার্নের জন্য শর্ত নির্ধারণ করে।
- `breaksw`: বর্তমান `switch` ব্লক থেকে বেরিয়ে আসে।
- `default:`: যদি কোন প্যাটার্ন মিলে না যায়, তাহলে এই অংশ কার্যকর হয়।

## Common Examples

### উদাহরণ 1: মৌলিক switch ব্যবহার
```csh
set var = "apple"
switch ($var)
    case "apple":
        echo "This is an apple."
        breaksw
    case "banana":
        echo "This is a banana."
        breaksw
    default:
        echo "Unknown fruit."
endsw
```

### উদাহরণ 2: সংখ্যা যাচাই করা
```csh
set num = 2
switch ($num)
    case 1:
        echo "Number is one."
        breaksw
    case 2:
        echo "Number is two."
        breaksw
    case 3:
        echo "Number is three."
        breaksw
    default:
        echo "Number is not one, two, or three."
endsw
```

### উদাহরণ 3: ফাইলের এক্সটেনশন চেক করা
```csh
set filename = "document.txt"
switch ($filename)
    case "*.txt":
        echo "This is a text file."
        breaksw
    case "*.jpg":
        echo "This is an image file."
        breaksw
    default:
        echo "Unknown file type."
endsw
```

## Tips
- `switch` ব্যবহার করার সময় নিশ্চিত করুন যে প্রতিটি `case` এর জন্য `breaksw` ব্যবহার করা হয়েছে, অন্যথায় এটি পরবর্তী `case` গুলিতে চলে যাবে।
- `default` অংশটি সর্বদা অন্তর্ভুক্ত করা উচিত যাতে অপ্রত্যাশিত ইনপুটের জন্য একটি সঠিক প্রতিক্রিয়া পাওয়া যায়।
- কেস প্যাটার্নের জন্য wildcard ব্যবহার করা যেতে পারে, যা শর্তগুলিকে আরও নমনীয় করে।