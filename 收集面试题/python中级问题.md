### python多线程在IO密集型情况下为什么会更快

- io是分为网络io和磁盘io，一般情况下，io有发送数据bai（output）和返回数据（input）两个过程。比如以浏览器为主体，浏览器发送请求给服务器（output），服务器再将请求结果返回给浏览器（input）。python在io阻塞的情况下，会释放GIL（global interpreter lock）锁，其他线程会在当前线程等待返回值（阻塞）的情况下继续执行发送请求（output），第三个线程又会在第二个线程等待返回值（阻塞）的情况下发送请求（output），即在同一时间片段，会有一个线程在等待数据，也会有一个线程在发数据。这就减少了io传输的时间。

- 但是，由于python在用cpu执行计算任务的时候，GIL锁不会被释放，python多线程其实还是使用的单核在进行cpu计算。一个cpu时间片只会分给一个线程，因此，cpu密集型的情况下，多线程并不会加快计算速度。
- 如果计算任务加锁了，cpu时间片调度机制会在一个cpu时间片（python默认是处理完1000个字节码）结束后，去释放GIL锁，并查看其他线程是否可以执行，由于任务被加锁，会在第二个cpu时间片继续把时间片分给第一个线程，这会让cpu调度时间白白浪费，反而导致多线程比单线程耗时更久。
- 自我总结
  - ​	在cpu进行数据计算时由于GIL机制导致python在计算时会导致开启GIL锁 导致其他线程需要等待计算 并且会在 抢计算机会的时候大量浪费(线程颠簸)切换时的资源 但在进行网络IO密集型情况下 有充足的时间要可以进行切换(网络延迟) 	