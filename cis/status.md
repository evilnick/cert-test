# Status

This indicates the level of compliance with the relevant CIS Benchmark for an
***as shipped*** install of Canonical Kubernetes. Regardless of whether users
have changed settings or configuration, we highly reccomend that an audit is
performed on the installed software to ensure compliance.

The {doc}`reference` section includes audit steps for every part of the CIS
benchmark. We also reccomend the [Kube-bench][] tool for automated testing of
some aspects of the benchmark.

```{include} ./_parts/kubebench.md
```

```{eval-rst}
.. raw:: latex

    \clearpage
```


<!--LINKS -->

[Kube-bench]: https://github.com/aquasecurity/kube-bench