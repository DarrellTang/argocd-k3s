from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Deployment, Pod
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.others import CRD
from diagrams.custom import Custom
from diagrams.onprem.gitops import Flux

with Diagram("metallb", show=False, direction="LR"):
    flux = Flux("Flux")
    with Cluster("networking Namespace"):
        helmRepo = CRD("HelmRepository")
        helmRelease = CRD("HelmRelease")
        metallb = [Pod("metallb-speaker"), Pod("metallb-controller")]
        deployment = Deployment("metallb")

        helmRepo >> helmRelease >> deployment >> metallb
    flux >> helmRepo

