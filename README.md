# singleton_tests
Example repo that shows how to mess up with importing in python.
Key things:
 - sys.path is shared across all scrip parts. If changed in one file, other files are influenced
 - importing module with different path loads it under different name in module cache
 - Singleton instances (well, anything) are part of the loaded module data, so could be duplicated

# Details
`main` script imports both proxy library and helloworld module
When `module_helloworld.py` is loaded, it mess up with sys.path. Adds `proxis` folder.

Such action affects `main` script. Now it is able to load proxy library using both ways:
 - from proxy_lib import ProxySingleton
 - from proxies.proxy_lib import ProxySingleton

Both will work, but each will be saved in module cache under different name. Any could be safely used
while its name in consistence with other imports (in `module_helloworld.py`).

The `main_good.py` covers same module import name (`proxies.proxy_lib` and `proxies.proxy_lib`)
The `main_bad.py` covers different module import name (`proxies.proxy_lib` and `proxy_lib`)

In the outputs of the commands you can see that `sys.modules` will contain different results and singleton behavior
as well as `id` will be different


As an extra, `main.py` contains execution of the `get_fake_module` method that will load module code into different module object
that also show that objects will be different