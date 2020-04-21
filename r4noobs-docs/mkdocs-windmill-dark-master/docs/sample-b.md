# Heading B

## Sub-Heading B 1

 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc fringilla volutpat odio, nec iaculis tortor laoreet vitae. Suspendisse dictum nibh nulla, non fringilla sapien mollis sed. Nunc vehicula facilisis tellus, ut tempor massa bibendum sed. Aenean non justo eu nulla luctus aliquam. Nullam eget arcu a urna ultrices volutpat lobortis ut sapien. Fusce vitae dapibus tellus, nec tincidunt metus. Etiam scelerisque orci ac ligula fermentum rhoncus. Ut at nisi quis tellus imperdiet porta. In semper mollis urna, nec ultricies purus bibendum non. 

## Sub-Heading B 2

* Lorem ipsum dolor sit amet, consectetur adipiscing elit.
* Aenean accumsan nulla iaculis enim fringilla consectetur.
* Fusce cursus risus ultrices ante placerat ullamcorper.
* Suspendisse eget ligula non mi suscipit eleifend eget ut neque.
* Duis nec dolor pharetra, pulvinar ante vel, tristique augue.
* Nulla semper ante gravida ex tempor commodo vel vitae elit.
* Nunc ultrices turpis et arcu placerat semper.
* Integer pellentesque sem luctus metus mattis imperdiet.
* Sed eget velit non nulla volutpat fermentum et sed nunc.
* Aenean at diam non magna dignissim iaculis.

## Sub-Heading B 3

```php
require_once 'Zend/Uri/Http.php';

namespace Location\Web;

interface Factory
{
    static function _factory();
}

abstract class URI extends BaseURI implements Factory
{
    abstract function test();

    public static $st1 = 1;
    const ME = "Yo";
    var $list = NULL;
    private $var;

    /**
     * Returns a URI
     *
     * @return URI
     */
    static public function _factory($stats = array(), $uri = 'http')
    {
        echo __METHOD__;
        $uri = explode(':', $uri, 0b10);
        $schemeSpecific = isset($uri[1]) ? $uri[1] : '';
        $desc = 'Multi
line description';

        // Security check
        if (!ctype_alnum($scheme)) {
            throw new Zend_Uri_Exception('Illegal scheme');
        }

        $this->var = 0 - self::$st;
        $this->list = list(Array("1"=> 2, 2=>self::ME, 3 => \Location\Web\URI::class));

        return [
            'uri'   => $uri,
            'value' => null,
        ];
    }
}

echo URI::ME . URI::$st1;

__halt_compiler () ; datahere
datahere
datahere */
datahere
```