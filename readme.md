Facebook Watchman trigger Example
=========

```
> git clone https://github.com/phate334/watchman-trigger-example
> cd watchman-trigger-example
> watchman watch-project .
> watchman -- trigger . jsonfile test.json -- trigger.py
```

## Reference

1. [watch-project](https://facebook.github.io/watchman/docs/cmd/watch-project.html)
2. [trigger](https://facebook.github.io/watchman/docs/cmd/trigger.html)