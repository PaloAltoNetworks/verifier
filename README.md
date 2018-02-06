# Request Code Injection with Istio Route Rules

Istio route rules can be used to redirect arbitrary service requests to an intermediary that
performs custom logic (e.g., validation or transformation) on a request and/or response body,
before forwarding the request/response. This can be accomplished without modifying any of
the application services themselves.

To demonstrate, this sample injects a simple verifier in front of calls to the `details` service
of the `Bookinfo` sample. The verifier is a simple python service that verifies (actually, just pretends to verify)
one of the fields of the `details` response, before returning it to the caller.

## Before you begin

1. Install Istio by following the [istio install instructions](https://istio.io/docs/setup/kubernetes/quick-start.html).

2. Start the [Bookinfo sample](https://istio.io/docs/guides/bookinfo.html).

3. Set the default version routing for the bookinfo sample.

   ```bash
   istioctl create -f samples/bookinfo/kube/route-rule-all-v1.yaml
   ```

At this point you should be able to point your browser to the BookInfo URL (http://$GATEWAY_URL/productpage)
to see the v1 version of the application.

## Running the verifier

1. Run the verifier.

   ```bash
   kubectl create -f <(istioctl kube-inject -f deploy.yaml)
   ```

2. Set the route rules to inject the verifier into the request path.

   ```bash
   istioctl create -f route-details-verified.yaml
   ```

3. Refresh the Bookinfo URL in your browser.

You should now see the string `(verified)` appended to the end of the `Publisher` property in the `Book Details` section,
indicating that the verifier was invoked during the GET request on the `details` service.

## Cleanup

```
kubectl delete -f deploy.yaml
kubectl delete routerules --all
```
