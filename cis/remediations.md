# Remediations

This section deals only with the steps required to ensure compliance with the
CIS Kubernetes benchmark as it applies to a fresh install of Canonical
Kubernetes. The steps listed here are those suggested by the status as
highlighted in the {doc}`status` section.



#### Control 1.1.1

Description: 
`Ensure that the API server pod specification file permissions are set to 600 or more restrictive (Automated)`

Audit:
```
/bin/sh -c 'if test -e /var/snap/k8s/common/args/kube-apiserver; then stat -c permissions=%a /var/snap/k8s/common/args/kube-apiserver; fi'
```

Remediation:
```
Run the below command (based on the file location on your system) on the
control plane node.
For example, chmod 600 /var/snap/k8s/common/args/kube-apiserver
```

Expected output:
```
test_items:
- compare:
    op: bitmask
    value: '600'
  flag: permissions
```

#### Control 1.1.2

Description: `Ensure that the API server pod specification file ownership is set to root:root (Automated)`

Audit:
```
/bin/sh -c 'if test -e /var/snap/k8s/common/args/kube-apiserver; then stat -c %U:%G /var/snap/k8s/common/args/kube-apiserver; fi'
```

Remediation:
```
Run the below command (based on the file location on your system) on the control plane node.
For example, chown root:root /var/snap/k8s/common/args/kube-apiserver
```

Expected output:
```
test_items:
- flag: root:root
```

#### Control 1.1.3

Description: `Ensure that the controller manager pod specification file permissions are set to 600 or more restrictive (Automated)`

Audit:
```
/bin/sh -c 'if test -e /var/snap/k8s/common/args/kube-controller-manager; then stat -c permissions=%a /var/snap/k8s/common/args/kube-controller-manager; fi'
```

Remediation:
```
Run the below command (based on the file location on your system) on the control plane node.
For example, chmod 600 /var/snap/k8s/common/args/kube-controller-manager
```

Expected output:
```
test_items:
- compare:
    op: bitmask
    value: '600'
  flag: permissions
```

#### Control 1.1.4

Description: `Ensure that the controller manager pod specification file ownership is set to root:root (Automated)`

Audit:
```
/bin/sh -c 'if test -e /var/snap/k8s/common/args/kube-controller-manager; then stat -c %U:%G /var/snap/k8s/common/args/kube-controller-manager; fi'
```

Remediation:
```
Run the below command (based on the file location on your system) on the control plane node.
For example, chown root:root /var/snap/k8s/common/args/kube-controller-manager
```

Expected output:
```
test_items:
- flag: root:root
```

#### Control 1.1.5

Description: `Ensure that the scheduler pod specification file permissions are set to 600 or more restrictive (Automated)`

Audit:
```
/bin/sh -c 'if test -e /var/snap/k8s/common/args/kube-scheduler; then stat -c permissions=%a /var/snap/k8s/common/args/kube-scheduler; fi'
```

Remediation:
```
Run the below command (based on the file location on your system) on the control plane node.
For example, chmod 600 /var/snap/k8s/common/args/kube-scheduler
```

Expected output:
```
test_items:
- compare:
    op: bitmask
    value: '600'
  flag: permissions
```

#### Control 1.1.6

Description: `Ensure that the scheduler pod specification file ownership is set to root:root (Automated)`

Audit:
```
/bin/sh -c 'if test -e /var/snap/k8s/common/args/kube-scheduler; then stat -c %U:%G /var/snap/k8s/common/args/kube-scheduler; fi'
```

Remediation:
```
Run the below command (based on the file location on your system) on the control plane node.
For example, chown root:root /var/snap/k8s/common/args/kube-scheduler
```

Expected output:
```
test_items:
- flag: root:root
```

#### Control 1.1.7

Description: `Ensure that the etcd pod specification file permissions are set to 644 or more restrictive (Automated)`

Audit:
```
/bin/sh -c 'if test -e /etc/default/etcd; then find /etc/default/etcd -name '*etcd*' | xargs stat -c permissions=%a; fi'
```

Remediation:
```
Run the below command (based on the file location on your system) on the control plane node.
For example,
chmod 644 /etc/default/etcd
```

Expected output:
```
test_items:
- compare:
    op: bitmask
    value: '644'
  flag: permissions
```

#### Control 1.1.8

Description: `Ensure that the etcd pod specification file ownership is set to root:root (Automated)`

Audit:
```
/bin/sh -c 'if test -e /etc/default/etcd; then find /etc/default/etcd -name '*etcd*' | xargs stat -c %U:%G; fi'
```

Remediation:
```
Run the below command (based on the file location on your system) on the control plane node.
For example,
chown root:root /etc/default/etcd
```

Expected output:
```
test_items:
- flag: root:root
```

#### Control 1.1.9

Description: `Ensure that the Container Network Interface file permissions are set to 600 or more restrictive (Manual)`

Audit:
```
ps -ef | grep kubelet | grep -- --cni-conf-dir | sed 's%.*cni-conf-dir[= ]\([^ ]*\).*%\1%' | xargs -I{} find {} -mindepth 1 | xargs --no-run-if-empty stat -c permissions=%a
find /etc/cni/net.d/10-calico.conflist -type f 2> /dev/null | xargs --no-run-if-empty stat -c permissions=%a
```

Remediation:
```
Run the below command (based on the file location on your system) on the control plane node.
For example, chmod 644 <path/to/cni/files>
```

Expected output:
```
test_items:
- compare:
    op: bitmask
    value: '644'
  flag: permissions
```

