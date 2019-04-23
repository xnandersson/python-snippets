Docs
----

- https://elasticsearch-py.readthedocs.io/en/master/
- https://elasticsearch-dsl.readthedocs.io/en/latest/

Youtube
-------

- https://www.youtube.com/watch?v=kNWwFq49YPA
- https://www.youtube.com/watch?v=FM2e2J7OJpM
- https://www.youtube.com/watch?v=90BPstUKOMU&list=PLZyZs2Ld646MBucOp122TSI3wSpUCwcsd
- https://www.youtube.com/watch?v=QMs-v-z0-as

Docker-Compose
--------------

.. code:: bash

  environment:
   - bootstrap.memory_lock=true
   - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
  ulimits:
    memlock:
      soft: -1
      hard: -1

  $ /etc/sysctl.conf

  vm.max_map_count=262144

  $ sudo sysctl -w vm.max_map_count=262144
  $ sudo sysctl -a | grep max_map_count
