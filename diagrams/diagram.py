from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Pod, StatefulSet, Deployment
from diagrams.k8s.network import Service, Ingress
from diagrams.k8s.storage import PV, PVC, StorageClass
from diagrams.onprem.gitops import Flux
from diagrams.onprem.dns import Coredns
from diagrams.onprem.monitoring import Prometheus,Grafana
from diagrams.onprem.vcs import Gitlab
from diagrams.generic.blank import Blank

with Diagram("Flux k3s Lab", show=True, direction="TB"):
    with Cluster("k3s"):
        fluxApps = ["helmController", "kustomizeController", "sourceController", "notificationController"]
        networkingApps = ["metallb", "coredns", "pihole"]
        monitoringApps = ["prometheus", "alertmanager", "grafana"]
        homeAutomationApps = ["magicmirror"]
        with Cluster("flux-system"):
            flux = Flux("flux")
        with Cluster("networking"):
            coredns = Coredns("Coredns")
            pihole = Deployment("Pihole")
            metalLB = Deployment("metalLB")
            coredns >> pihole
        with Cluster("monitoring"):
            grafana = Grafana("Grafana")
            prometheus = Prometheus("Prometheus")
        with Cluster("home automation"):
            magicmirror = Deployment("Magic Mirror")
        piholeIngress = Ingress("Pihole")
        piholeIngress >> pihole
        grafanaIngress = Ingress("Grafana")
        grafanaIngress >> grafana
        prometheusIngress = Ingress("Prometheus")
        prometheusIngress >> prometheus
        magicmirrorIngress = Ingress("Magic Mirror")
        magicmirrorIngress >> magicmirror
    gitlab = Gitlab("Gitlab")
    gitlab >> flux
    flux >> [coredns, pihole, grafana, prometheus, magicmirror]
    ingresses = ["Pihole", "Grafana", "Prometheus", "Magic Mirror"]
