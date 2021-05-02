package com.openfaas.function;

import io.vertx.ext.web.RoutingContext;
import io.vertx.core.json.JsonObject;

public class Handler implements io.vertx.core.Handler<RoutingContext> {

  public void handle(RoutingContext routingContext) {
    routingContext.response()
      .putHeader("content-type", "application/json;charset=UTF-8")
      .end(
        new JsonObject()
          .put("status", "ok")
          .encodePrettily()
      );
  }
}
