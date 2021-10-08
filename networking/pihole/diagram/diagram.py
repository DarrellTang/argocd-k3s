from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Deployment, Pod
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.others import CRD
from diagrams.custom import Custom

with Diagram("pihole", show=False, direction="LR"):
    with Cluster("networking Namespace"):
        ingress = Ingress("pihole.tang.local\n10.0.0.230")
        service = Service("LoadBalancerIP\n10.0.0.231")
        helmRepo = CRD("HelmRepository")
        helmRelease = CRD("HelmRelease")
        pihole = Pod("pihole")
        deployment = Deployment("pihole")

        helmRepo >> helmRelease >> [ingress >> service, deployment] >>  pihole
