# python-concurrent-patterns
Single Queue: single writer single reader

  Time (ms)  TPS (requests/second)
0     100.94               99072.04
1     184.32              119920.86
2     292.88               92118.53
3     385.53              107938.71
4     497.70               89147.76
5     589.51              108924.85
6     681.57              108619.08
7     775.84              106083.93
8     863.33              114297.74
9     951.04              114010.97

Single Queue: 2 writers and single reader
   Time (ms)  TPS (requests/second)
0     272.47               36701.29
1     547.76               36325.08
2     800.65               39542.87
3    1078.04               36050.48
4    1350.75               36669.46
5    1648.27               33611.19
6    1902.95               39264.68
7    2176.35               36576.63
8    2435.16               38638.45
9    2666.46               43233.96

Single Queue: 3 writer and single reader

  Time (ms)  TPS (requests/second)
0     324.54               30813.08
1     583.02               38686.99
2    1068.18               20611.96
3    1573.65               19783.55
4    1984.80               24321.83
5    2459.01               21087.85
6    2931.49               21164.94
7    3395.34               21558.50
8    3804.82               24421.11
9    4256.67               22131.59
