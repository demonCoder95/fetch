# URL Fetcher based on Python3

This is a simple URL fetcher based on python3.
All the requirements have been noted in the ``requirements.txt`` file.

To run the CLI program, run the driver program ``src/main.py``.
You can use the ``-h`` switch to see the help on the CLI.

Example run:

``` bash
    python3 src/main.py https://google.com https://example.com
```

You can specify the ``--metadata`` flag to get some metadata information
of the URl as well. Example:

``` bash
    python3 src/main.py --metadata https://google.com
```

``` bash
    site: google.com
    num_links: 20
    images: 1
    last_fetch: Mon Oct 25 16:52:20 2021
```

## Future Improvements

Add multithreading to accelerate the URL fetching with a new class that
operates on ``ThreadPoolExecutor`` objects.

Fix the ``src=`` field of ``img`` tags to point to local cache dir.
