from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Deployment, Pod
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.others import CRD
from diagrams.custom import Custom
from diagrams.onprem.gitops import Flux

with Diagram("coredns", show=False, direction="LR"):
    flux = Flux("Flux")
    with Cluster("networking Namespace"):
        dnsTcp = Service("coredns-TCP:53\nLoadBalancerIP\n10.0.0.231")
        dnsUdp = Service("coredns-UDP:53\nLoadBalancerIP\n10.0.0.231")
        coredns = [Pod("coredns"), Pod("coredns"), Pod("coredns")]
        deployment = Deployment("coredns")

        dnsTcp >> coredns
        dnsUdp >> coredns
        deployment >> coredns
    flux >> [dnsTcp, dnsUdp, deployment]
