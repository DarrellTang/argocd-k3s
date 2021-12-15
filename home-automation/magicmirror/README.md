# **MagicMirror²**

is an open source modular smart mirror platform. For more info visit the [project website](https://github.com/MichMich/MagicMirror).

# Introduction

This helm chart bootstraps a MagicMirror instance.

> 👉 The project is very young so don't expect everything works already ...

# Restrictions

A normal MagicMirror setup uses a raspberry pi as hardware. If you want to run the application without output on the screen of the pi, you can run it [server only](https://docs.magicmirror.builders/getting-started/installation.html#usage) and open MagicMirror with a web browser.

As most k8s clusters are not running on raspberry pi's, here the `server only` setup of MagicMirror is used.

> ❌ This implies that no modules can be used which need raspberry pi specific hardware (e.g. GPIO).

# Prerequisites

* Running Kubernetes Cluster
* Helm

# Installing the chart

To install the chart:

```bash
$ git clone https://gitlab.com/khassel/magicmirror-helm.git
$ cd magicmirror-helm
$ helm upgrade magicmirror -i .
```

The above command deploys MagicMirror on the Kubernetes cluster in a default configuration (with default modules).

# Uninstalling the chart

To uninstall/delete the deployment:

```bash
$ helm ls
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                   APP VERSION
magicmirror     default         3               2020-06-03 21:27:57.417308079 +0000 UTC deployed        magicmirror-1.0.0       1.0

$ helm delete magicmirror
```

This code is a direct copy of the MagicMirror Helm Chart listed above by
khassel. Using flux as a syncing mechanism was stymied by this not being
a formal helm repository, so the files are here as reference for manual
Helm management with the modified values.yaml file.
