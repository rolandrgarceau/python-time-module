# python-time-module

This recap (for some) will explain:

* Working with dates and times, such as epochs, time zones, and daylight savings time.

* Code examples as representations using floats, tuples, and struct_time.

* Explain how to convert between the representations

* Suspend thread representations

* Show code performance using perf_counter()

## Quick investigation on MBP and man for date

Watch using bash and cli $(date) as it can display OR SET date. /var/log/messages may need further investigation on an accidental set. man the pages and notice -v for also changing the date from current machine date. 

Linux has a flag --iso8601 which doesn't work on mac-out-the-box:) [GNU man](https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html). If needed use full path to date /bin/date or go search brew. Same holds for Python interpreters. Know which one and where.

RFC 2822 is another standard listed in BSD General Commons man page, though.

RFC 3339 is a newer revision for both ISO 8601 AND RFC 2822

Check [this](https://www.cyberciti.biz/faq/linux-unix-formatting-dates-for-display/) for more cross platform examples.

```sh
# not on a MBP
echo $(date --iso-8601)

# time only
date +"%T"
# time only with 12 hr AM/PM out
date +"%r"

# save to shell variable for later
$NOW=$(date +"%Y-%m-%d")
```

$NOW, for Python...

## Using a floating point number to represent time

To measure Epoch from 1970 in seconds require looking at the math (I know it hurts sometimes...):

```py
# seconds * minutes * hours * days * years = today in seconds, right?
60 * 60 * 24 * 50 # wow what an anniversary 50 years later...

```
* what about leap year, that was this year, right?
* what about 1918's last flu outbreak? Just go negative, already, and it works:)

I'm glad we are not blazing a new patent path here and someone was kind enough to share. time.time() returns the number of seconds that have passed since the epoch:

```py
# in order for the REPL to call time easier it needs to be specifically imported
In [1]: time()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-40ab0602927b> in <module>
----> 1 time()

TypeError: 'module' object is not callable

In [2]: from time import time

In [3]: time()
Out[3]: 1585478144.089322
```

gmtime() and struct_time are also ways using `time` to measure and discover this:

```sh
% ipython
Python 3.7.4 (default, Aug 13 2019, 15:17:50)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.8.0 -- An enhanced Interactive Python. Type '?' for help.

In [4]: import time

# to discover the epoch actual starting point
In [5]: time.gmtime(0) # seconds argument is optional, zero is epoch
Out[5]: time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)


# tm_yday is the day of year from 1-365, it may be 0-364...
# tm_isdst is the daylight savings time flag.

# get the current

In [2]: time.gmtime()
Out[2]: time.struct_time(tm_year=2020, tm_mon=3, tm_mday=30, tm_hour=17, tm_min=59, tm_sec=15, tm_wday=0, tm_yday=90, tm_isdst=0)
```

Keep in mind this is reference points that are on your machine. Python 3.7 has [time_ns()](https://realpython.com/python37-new-features/#timing-precision) which returns an integer value in nanoseconds.

Don't forget If we are going over the wire we need information to be [serializable](https://en.wikipedia.org/wiki/Serialization). We can use a float to calculate the difference between two points in time, which can be easily stored for web use later.

String representations are cool too. We can use that to quickly display time to a user on a website instead of trying to be a data scientist. But being any kinda scientist, we ask- "just where are we trying to grab this magical time from?"- create a native react app and we are processing ***JavaScript*** on the device, right? What does it matter, this is Python:) Just notice our red-neck engineering at work here...

```py

In [6]: from time import ctime

# this records it in a object, then, there, and at that moment:)
In [7]: t  = time()

In [8]: ctime(t)

# here is the 24-hour clock timestamp output
Out[8]: 'Sun Mar 29 06:59:53 2020'

```

## 'Local Time' in Sydney, Australia?

Well for us on USEast-1 this works. Just know the time zone corrections and all is well. Timestamps should take this into account, but if we are say, designing a log-in clock for remote work, this might become an issue ***real quick***. 

## UTC, GMT, don't be forgetting...

Sticking to UTC in general practice is better (as it is a standard) than having to deal with DST, time zone, or locale information. But there are plenty of times using local is good.

Coordinated Universal Time might CUT you if you don't pay attention to the acronym! In France it is TUC. How about a control - f + UCT? Sydney's ***time zone*** is AET. It's 10-11 hours off UTC (daylight savings) and is great to call data-centers at 4 am when I'm up coding- or talking to Apple Support on a DR call. In the fall we drop back to standard time in NC. CT is for us here in the south, which is 6 hours off UTC. Grand scheme of things is this may report 16 hours off between the two. Now what does one do to make a time clock to clock in properly? Which one is that company that hires you to work remote use? Just check your billable hours, that's all I have to say.

## How do you build a time clock in Python you ask? 

With lots of patience my patawan...

## Python primitives

Try a [tuple](https://realpython.com/python-lists-tuples/#defining-and-using-tuples) or two. Its like a marriage. Abstract data = disconnect. Don't share right? Wind up on the couch!

```py

In [9]: ctime()
Out[9]: 'Sun Mar 29 07:29:14 2020'

```
Watch the struct_time import and recount gmtime(0) functionality. Go back and type in the REPL to convince us this works:

```py
# passing zero is the base starting point
# gmtime() converts the number of elapsed seconds since the epoch to a struct_time in UTC.

time.gmtime(0)
Out[2]: time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

```

### Try not to confuse another language

C structs and objects are clearly different topics. 

### [struct_time](https://docs.python.org/3/library/time.html)

Struct-time is derived from the C based time library, where that is actually a struct, but remember in python we use objects. The time module uses the struct directly, as it is implemented in C, and includes the header file times.h

```py
In [5]: from time import struct_time

# tuples are specific to python
In [6]: time_tuple = (1,2,3,4,5,6,7,8,9)

In [7]: time_obj = struct_time(t_t)

In [8]: time_obj
Out[8]: time.struct_time(tm_year=1, tm_mon=2, tm_mday=3, tm_hour=4, tm_min=5, tm_sec=6, tm_wday=7, tm_yday=8, tm_isdst=9)
```

## Conversions

Is dependent oof UTC or local time. Epoch uses UTC instead of a time zone. So seconds will not matter by geographic location.

### struct_time might not be correct

Object representation in Python of time may or may not take your time zone into account.

struct_time can be used to convert a float representing seconds, in either of two ways: UTC or local time.

UTC uses gmtime(), and gmtime() converts the number of elapsed seconds since the epoch to a struct_time in UTC. The daylight savings flag will always be zero. There is no inverse for this function within time, however.

```py
In [1]: import time

In [2]: time.gmtime()
Out[2]: time.struct_time(tm_year=2020, tm_mon=3, tm_mday=30, tm_hour=17, tm_min=59, tm_sec=15, tm_wday=0, tm_yday=90, tm_isdst=0)
```

### [calendar](https://docs.python.org/3/library/calendar.html) module
timegm() takes a tuple (or struct_time, since it is a subclass of tuple) and returns the corresponding number of seconds since the epoch. 
