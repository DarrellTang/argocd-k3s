from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Deployment, Pod
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.others import CRD
from diagrams.custom import Custom
from diagrams.onprem.gitops import Flux

with Diagram("pihole", show=False, direction="LR"):
    flux = Flux("Flux")
    with Cluster("networking Namespace"):
        ingress = Ingress("pihole.tang.local\n10.0.0.230")
        web = Service("Pihole-Web:80\nLoadBalancerIP\n10.0.0.231")
        dnsTcp = Service("Pihole-TCP:53\nLoadBalancerIP\n10.0.0.231")
        dnsUdp = Service("Pihole-UDP:53\nLoadBalancerIP\n10.0.0.231")
        helmRepo = CRD("HelmRepository")
        helmRelease = CRD("HelmRelease")
        pihole = Pod("pihole")
        deployment = Deployment("pihole")

        helmRepo >> helmRelease >> [web, dnsTcp, dnsUdp] >> pihole
        helmRelease >> deployment >> pihole
        ingress >> web
    flux >> helmRepo
