# WP-plugin-scanner
Scan any wordpress-powered website and find out which plugins it is using

##Requirements
+ [`lxml`](http://lxml.de/) is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.


## Usage
    wp-plugin-scan.py [options]

    Options:
    -h, --help                      show this help message and exit
    -s, --scan      <website url>   scan website at the specified url
    -u, --update    <page number>   update the list of popular plugins from wordpress.org

### Scanning a wordpress powered website
To scan a website simply use `-s` or `--scan` parameter and specify the url to wordpress directory.

    wp-plugin-scan.py -s http://example.com/blog/
    
or

    wp-plugin-scan.py --scan http://example.com/blog/

### Updating the list of popular plugins
If you want to update the list of popular plugins simply use -u or --update parameter and specify the end page for the range.

    wp-plugin-scan.py -u 15

or

    wp-plugin-scan.py --update 15
