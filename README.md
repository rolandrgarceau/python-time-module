# python-time-module

This recap (for some) will explain:

* Working with dates and times, such as epochs, time zones, and daylight savings time.

* Code examples as representations using floats, tuples, and struct_time.

* Explain how to convert between the representations

* Suspend thread representations

* Show code performance using perf_counter()

## Using a floating point number to represent time

To measure Epoch from 1970 in seconds require looking at the math (I know it hurts sometimes...):

```py
# seconds * minutes * hours * days * years = today in seconds, right?
60 * 60 * 24 * 50 # wow what an anniversary 50 years later...

```
* what about leap year, that was this year, right?
* what about 1918's last flu outbreak? Just go negative, already and it works:)

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

gmtime() and struct_time are also ways to measure using `time` to measure and discover this:

```sh
% ipython
Python 3.7.4 (default, Aug 13 2019, 15:17:50)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.8.0 -- An enhanced Interactive Python. Type '?' for help.

In [4]: import time

In [5]: time.gmtime(0)
Out[5]: time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

```

Keep in mind this is reference points that are on your machine. Python 3.7 has [time_ns()](https://realpython.com/python37-new-features/#timing-precision) which returns an integer value in nanoseconds.

Don't forget If we are going over the wire we need information to be [serializable](https://en.wikipedia.org/wiki/Serialization). We can use a float to calculate the difference between two points in time, which can be easliy stored for the web use.