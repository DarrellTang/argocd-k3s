from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Deployment
from diagrams.k8s.network import Ingress
from diagrams.onprem.gitops import Flux
from diagrams.onprem.dns import Coredns
from diagrams.onprem.monitoring import Prometheus,Grafana
from diagrams.onprem.vcs import Gitlab

with Diagram("Flux k3s Lab", show=False, direction="TB"):
    with Cluster("k3s"):
        with Cluster("flux-system"):
            flux = Flux("flux")
        with Cluster("networking"):
            coredns = Coredns("Coredns\n10.0.0.237")
            pihole = Deployment("Pihole\n10.0.0.235")
            metalLB = Deployment("metalLB\n10.0.0230")
        with Cluster("monitoring"):
            grafana = Grafana("Grafana\n10.0.0.234")
            prometheus = Prometheus("Prometheus\n10.0.0.233")
            alertmanager = Deployment("Alertmanager\n10.0.0.232")
        with Cluster("home automation"):
            magicmirror = Deployment("Magic Mirror\n10.0.0.236")
    gitlab = Gitlab("Gitlab\nhttps://gitlab.com/darrelltang/flux-k3s/")
    gitlab >> flux
    flux >> [metalLB, coredns, pihole, alertmanager, grafana, prometheus, magicmirror]
