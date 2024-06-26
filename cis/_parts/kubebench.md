## Summary 

```{eval-rst}
.. role:: statusfail
.. role:: statusinfo
.. role:: statuswarn
.. role:: statuspass
```


- 54 checks {statuspass}`PASS`
- 24 checks {statusfail}`FAIL`
- 37 checks {statuswarn}`WARN`
- 0 checks {statusinfo}`INFO`


## Kube-bench report

```{table} Output generated from Kube-bench
:widths: auto
:align: left


| Status | Descriptor |
|--------|------------|
|{statusinfo}`INFO` | 1 Master Node Security Configuration |
|{statusinfo}`INFO` | 1.1 Master Node Configuration Files |
|{statusfail}`FAIL` | 1.1.1 Ensure that the API server pod specification file permissions are set to 644 or more restrictive (Automated)|
|{statusfail}`FAIL` |  1.1.2 Ensure that the API server pod specification file ownership is set to root:root (Automated)|
|{statusfail}`FAIL` |  1.1.3 Ensure that the controller manager pod specification file permissions are set <br> to 644 or more restrictive (Automated)
|{statusfail}`FAIL` |  1.1.4 Ensure that the controller manager pod specification file ownership is set to root:root (Automated)
|{statusfail}`FAIL` |  1.1.5 Ensure that the scheduler pod specification file permissions are set to 644 or more restrictive (Automated)
|{statusfail}`FAIL` |  1.1.6 Ensure that the scheduler pod specification file ownership is set to root:root (Automated)
|{statusfail}`FAIL` |  1.1.7 Ensure that the etcd pod specification file permissions are set to 644 or more restrictive (Automated)
|{statusfail}`FAIL` |  1.1.8 Ensure that the etcd pod specification file ownership is set to root:root (Automated)
|{statuswarn}`WARN` | 1.1.9 Ensure that the Container Network Interface file permissions are set to 644 or more restrictive (Manual) 
|{statuswarn}`WARN` | 1.1.10 Ensure that the Container Network Interface file ownership is set to root:root (Manual)
|{statusfail}`FAIL` |  1.1.11 Ensure that the etcd data directory permissions are set to 700 or more restrictive (Automated)
|{statusfail}`FAIL` |  1.1.12 Ensure that the etcd data directory ownership is set to etcd:etcd (Automated)
|{statuspass}`PASS` | 1.1.13 Ensure that the admin.conf file permissions are set to 644 or more restrictive (Automated)
|{statuspass}`PASS` | 1.1.14 Ensure that the admin.conf file ownership is set to root:root (Automated)
|{statuspass}`PASS` | 1.1.15 Ensure that the scheduler.conf file permissions are set to 644 or more restrictive (Automated)
|{statuspass}`PASS` | 1.1.16 Ensure that the scheduler.conf file ownership is set to root:root (Automated)
|{statusfail}`FAIL` |  1.1.17 Ensure that the controller-manager.conf file permissions are set to 644 or more restrictive (Automated)
|{statusfail}`FAIL` |  1.1.18 Ensure that the controller-manager.conf file ownership is set to root:root (Automated)
|{statuspass}`PASS` | 1.1.19 Ensure that the Kubernetes PKI directory and file ownership is set to root:root (Automated)
|{statuspass}`PASS` | 1.1.20 Ensure that the Kubernetes PKI certificate file permissions are set to 644 or more restrictive (Manual)
|{statuspass}`PASS` | 1.1.21 Ensure that the Kubernetes PKI key file permissions are set to 600 (Manual)
|{statuspass}`ÌNFO` | 1.2 API Server
|{statuspass}`PASS` | 1.2.1 Ensure that the --anonymous-auth argument is set to false (Manual)
|{statuspass}`PASS` | 1.2.2 Ensure that the --basic-auth-file argument is not set (Automated)
|{statuspass}`PASS` | 1.2.3 Ensure that the --token-auth-file parameter is not set (Automated)
|{statuspass}`PASS` | 1.2.4 Ensure that the --kubelet-https argument is set to true (Automated)
|{statuspass}`PASS` | 1.2.5 Ensure that the --kubelet-client-certificate and --kubelet-client-key arguments are set as appropriate (Automated)
|{statuspass}`PASS` | 1.2.6 Ensure that the --kubelet-certificate-authority argument is set as appropriate (Automated)
|{statuspass}`PASS` | 1.2.7 Ensure that the --authorization-mode argument is not set to AlwaysAllow (Automated)
|{statuspass}`PASS` | 1.2.8 Ensure that the --authorization-mode argument includes Node (Automated)
|{statuspass}`PASS` | 1.2.9 Ensure that the --authorization-mode argument includes RBAC (Automated)
|{statuswarn}`WARN` | 1.2.10 Ensure that the admission control plugin EventRateLimit is set (Manual)
|{statuspass}`PASS` | 1.2.11 Ensure that the admission control plugin AlwaysAdmit is not set (Automated)
|{statuswarn}`WARN` | 1.2.12 Ensure that the admission control plugin AlwaysPullImages is set (Manual)
|{statuswarn}`WARN` | 1.2.13 Ensure that the admission control plugin SecurityContextDeny is set if PodSecurityPolicy is not used (Manual)
|{statuspass}`PASS` | 1.2.14 Ensure that the admission control plugin ServiceAccount is set (Automated)
|{statuspass}`PASS` | 1.2.15 Ensure that the admission control plugin NamespaceLifecycle is set (Automated)
|{statusfail}`FAIL` |  1.2.16 Ensure that the admission control plugin PodSecurityPolicy is set (Automated)
|{statuspass}`PASS` | 1.2.17 Ensure that the admission control plugin NodeRestriction is set (Automated)
|{statuspass}`PASS` | 1.2.18 Ensure that the --insecure-bind-address argument is not set (Automated)
|{statusfail}`FAIL` |  1.2.19 Ensure that the --insecure-port argument is set to 0 (Automated)
|{statuspass}`PASS` | 1.2.20 Ensure that the --secure-port argument is not set to 0 (Automated)
|{statuspass}`PASS` | 1.2.21 Ensure that the --profiling argument is set to false (Automated)
|{statusfail}`FAIL` |  1.2.22 Ensure that the --audit-log-path argument is set (Automated)
|{statusfail}`FAIL` |  1.2.23 Ensure that the --audit-log-maxage argument is set to 30 or as appropriate (Automated)
|{statusfail}`FAIL` |  1.2.24 Ensure that the --audit-log-maxbackup argument is set to 10 or as appropriate (Automated)
|{statusfail}`FAIL` |  1.2.25 Ensure that the --audit-log-maxsize argument is set to 100 or as appropriate (Automated)
|{statuswarn}`WARN` | 1.2.26 Ensure that the --request-timeout argument is set as appropriate (Automated)
|{statuspass}`PASS` | 1.2.27 Ensure that the --service-account-lookup argument is set to true (Automated)
|{statuspass}`PASS` | 1.2.28 Ensure that the --service-account-key-file argument is set as appropriate (Automated)
|{statusfail}`FAIL` |  1.2.29 Ensure that the --etcd-certfile and --etcd-keyfile arguments are set as appropriate (Automated)
|{statuspass}`PASS` | 1.2.30 Ensure that the --tls-cert-file and --tls-private-key-file arguments are set as appropriate (Automated) |
|{statuspass}`PASS` | 1.2.31 Ensure that the --client-ca-file argument is set as appropriate (Automated)
|{statusfail}`FAIL` |  1.2.32 Ensure that the --etcd-cafile argument is set as appropriate (Automated)
|{statuswarn}`WARN` | 1.2.33 Ensure that the --encryption-provider-config argument is set as appropriate (Manual)
|{statuswarn}`WARN` | 1.2.34 Ensure that encryption providers are appropriately configured (Manual)
|{statuswarn}`WARN` | 1.2.35 Ensure that the API Server only makes use of Strong Cryptographic Ciphers (Manual)
|{statusinfo}`INFO` | 1.3 Controller Manager
|{statuspass}`PASS` | 1.3.1 Ensure that the --terminated-pod-gc-threshold argument is set as appropriate (Manual)
|{statuspass}`PASS` | 1.3.2 Ensure that the --profiling argument is set to false (Automated)
|{statuspass}`PASS` | 1.3.3 Ensure that the --use-service-account-credentials argument is set to true (Automated)
|{statuspass}`PASS` | 1.3.4 Ensure that the --service-account-private-key-file argument is set as appropriate (Automated)
|{statuspass}`PASS` | 1.3.5 Ensure that the --root-ca-file argument is set as appropriate (Automated)
|{statuspass}`PASS` | 1.3.6 Ensure that the RotateKubeletServerCertificate argument is set to true (Automated)
|{statuspass}`PASS` | 1.3.7 Ensure that the --bind-address argument is set to 127.0.0.1 (Automated)
|{statusinfo}`INFO` | 1.4 Scheduler
|{statuspass}`PASS` | 1.4.1 Ensure that the --profiling argument is set to false (Automated)
|{statuspass}`PASS` | 1.4.2 Ensure that the --bind-address argument is set to 127.0.0.1 (Automated)
|{statusinfo}`INFO` | 4 Worker Node Security Configuration
|{statusinfo}`INFO` | 4.1 Worker Node Configuration Files
|{statusfail}`FAIL` |  4.1.1 Ensure that the kubelet service file permissions are set to 644 or more restrictive (Automated)
|{statuspass}`PASS` | 4.1.2 Ensure that the kubelet service file ownership is set to root:root (Automated)
|{statuspass}`PASS` | 4.1.3 If proxy kubeconfig file exists ensure permissions are set to 644 or more restrictive (Manual)
|{statuspass}`PASS` | 4.1.4 Ensure that the proxy kubeconfig file ownership is set to root:root (Manual)
|{statuspass}`PASS` | 4.1.5 Ensure that the --kubeconfig kubelet.conf file permissions are set to 644 or more restrictive (Automated)
|{statuspass}`PASS` | 4.1.6 Ensure that the --kubeconfig kubelet.conf file ownership is set to root:root (Manual)
|{statuspass}`PASS` | 4.1.7 Ensure that the certificate authorities file permissions are set to 644 or more restrictive (Manual)
|{statuspass}`PASS` | 4.1.8 Ensure that the client certificate authorities file ownership is set to root:root (Manual)
|{statusfail}`FAIL` |  4.1.9 Ensure that the kubelet --config configuration file has permissions set to 644 or more restrictive (Automated)
|{statusfail}`FAIL` |  4.1.10 Ensure that the kubelet --config configuration file ownership is set to root:root (Automated)
|{statusinfo}`INFO` | 4.2 Kubelet
|{statuspass}`PASS` | 4.2.1 Ensure that the anonymous-auth argument is set to false (Automated)
|{statuspass}`PASS` | 4.2.2 Ensure that the --authorization-mode argument is not set to AlwaysAllow (Automated)
|{statuspass}`PASS` | 4.2.3 Ensure that the --client-ca-file argument is set as appropriate (Automated)
|{statuspass}`PASS` | 4.2.4 Ensure that the --read-only-port argument is set to 0 (Manual)
|{statuspass}`PASS` | 4.2.5 Ensure that the --streaming-connection-idle-timeout argument is not set to 0 (Manual)
|{statusfail}`FAIL` |  4.2.6 Ensure that the --protect-kernel-defaults argument is set to true (Automated)
|{statuspass}`PASS` | 4.2.7 Ensure that the --make-iptables-util-chains argument is set to true (Automated)
|{statuspass}`PASS` | 4.2.8 Ensure that the --hostname-override argument is not set (Manual)
|{statuswarn}`WARN` | 4.2.9 Ensure that the --event-qps argument is set to 0 or a level which ensures appropriate event capture (Manual)
|{statuspass}`PASS` | 4.2.10 Ensure that the --tls-cert-file and --tls-private-key-file arguments are set as appropriate (Manual)
|{statuspass}`PASS` | 4.2.11 Ensure that the --rotate-certificates argument is not set to false (Manual)
|{statuspass}`PASS` | 4.2.12 Verify that the RotateKubeletServerCertificate argument is set to true (Manual)
|{statuspass}`PASS` | 4.2.13 Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers (Manual)
|{statusinfo}`INFO` | 5 Kubernetes Policies
|{statusinfo}`INFO` | 5.1 RBAC and Service Accounts
|{statuswarn}`WARN` | 5.1.1 Ensure that the cluster-admin role is only used where required (Manual)
|{statuswarn}`WARN` | 5.1.2 Minimize access to secrets (Manual)
|{statuswarn}`WARN` | 5.1.3 Minimize wildcard use in Roles and ClusterRoles (Manual)
|{statuswarn}`WARN` | 5.1.4 Minimize access to create pods (Manual)
|{statuswarn}`WARN` | 5.1.5 Ensure that default service accounts are not actively used. (Manual)
|{statuswarn}`WARN` | 5.1.6 Ensure that Service Account Tokens are only mounted where necessary (Manual)
|{statusinfo}`INFO` | 5.2 Pod Security Policies
|{statuswarn}`WARN` | 5.2.1 Minimize the admission of privileged containers (Manual)
|{statuswarn}`WARN` | 5.2.2 Minimize the admission of containers wishing to share the host process ID namespace (Manual)
|{statuswarn}`WARN` | 5.2.3 Minimize the admission of containers wishing to share the host IPC namespace (Manual)
|{statuswarn}`WARN` | 5.2.4 Minimize the admission of containers wishing to share the host network namespace (Manual)
|{statuswarn}`WARN` | 5.2.5 Minimize the admission of containers with allowPrivilegeEscalation (Manual)
|{statuswarn}`WARN` | 5.2.6 Minimize the admission of root containers (Manual)
|{statuswarn}`WARN` | 5.2.7 Minimize the admission of containers with the NET_RAW capability (Manual)
|{statuswarn}`WARN` | 5.2.8 Minimize the admission of containers with added capabilities (Manual)
|{statuswarn}`WARN` | 5.2.9 Minimize the admission of containers with capabilities assigned (Manual)
|{statusinfo}`INFO` | 5.3 Network Policies and CNI
|{statuswarn}`WARN` | 5.3.1 Ensure that the CNI in use supports Network Policies (Manual)
|{statuswarn}`WARN` | 5.3.2 Ensure that all Namespaces have Network Policies defined (Manual)
|{statusinfo}`INFO` | 5.4 Secrets Management
|{statuswarn}`WARN` | 5.4.1 Prefer using secrets as files over secrets as environment variables (Manual)
|{statuswarn}`WARN` | 5.4.2 Consider external secret storage (Manual)
|{statusinfo}`INFO` | 5.5 Extensible Admission Control
|{statuswarn}`WARN` | 5.5.1 Configure Image Provenance using ImagePolicyWebhook admission controller (Manual)
|{statusinfo}`INFO` | 5.7 General Policies
|{statuswarn}`WARN` | 5.7.1 Create administrative boundaries between resources using namespaces (Manual)
|{statuswarn}`WARN` | 5.7.2 Ensure that the seccomp profile is set to docker/default in your pod definitions (Manual)
|{statuswarn}`WARN` | 5.7.3 Apply Security Context to Your Pods and Containers (Manual)
|{statuswarn}`WARN` | 5.7.4 The default namespace should not be used (Manual)

```
