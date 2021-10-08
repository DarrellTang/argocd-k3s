from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Deployment
from diagrams.k8s.network import Ingress
from diagrams.onprem.gitops import Flux
from diagrams.onprem.dns import Coredns
from diagrams.onprem.monitoring import Prometheus,Grafana
from diagrams.onprem.vcs import Gitlab
from diagrams.custom import Custom

with Diagram("Flux k3s Lab", show=False, direction="TB"):
    with Cluster("k3s"):
        with Cluster("flux-system"):
            flux = Flux("flux")
        with Cluster("networking"):
            coredns = Coredns("Coredns\n10.0.0.232")
            pihole = Custom("Pihole\n10.0.0.231", "../networking/pihole/diagram/Pi-hole_Logo.png")
            metalLB = Custom("metalLB\n10.0.0230", "../networking/metallb/diagram/metallb-blue.png")
        with Cluster("monitoring"):
            grafana = Grafana("Grafana\n10.0.0.235")
            prometheus = Prometheus("Prometheus\n10.0.0.233")
            alertmanager = Prometheus("Alertmanager\n10.0.0.234")
        with Cluster("home automation"):
            magicmirror = Custom("Magic Mirror\n10.0.0.236", "../home-automation/magicmirror/diagram/mirror.png")
    gitlab = Gitlab("Gitlab\nhttps://gitlab.com/darrelltang/flux-k3s/")
    gitlab >> flux
    flux >> [metalLB, coredns, pihole, prometheus, grafana, alertmanager, magicmirror]
