# CHANGELOG

<!-- version list -->

## v0.8.0 (2025-10-04)

### ✨ Features

- Implement deferred event bus
  ([`ef43ab9`](https://github.com/adriamontoto/domain-event-pattern/commit/ef43ab9f9db31a0c8d957b94ea2bc17b673e94c2))


## v0.7.0 (2025-10-03)

### 🐛 Bug Fixes

- Conditional import of 'override' for Python < 3.12
  ([`468ab83`](https://github.com/adriamontoto/domain-event-pattern/commit/468ab8351686546dc2972f16664b4962c5cc9155))

### ✨ Features

- Delete unused classes
  ([`4c5542c`](https://github.com/adriamontoto/domain-event-pattern/commit/4c5542cd131c374b3bdce1e0bf5250a996af9a05))

- Ensure subscriber name is defined with the subscriber subclasses
  ([`0464a71`](https://github.com/adriamontoto/domain-event-pattern/commit/0464a713445e7180b6c664677568596ea8409361))

- Implement event handler class property to obtain subscribed events
  ([`1aea69b`](https://github.com/adriamontoto/domain-event-pattern/commit/1aea69b2807019949df6eb957b39518d76c51fa3))

- Rename domain event event name to name
  ([`e53195a`](https://github.com/adriamontoto/domain-event-pattern/commit/e53195a40bc4ccbe47364479607bdcd6f4fb7e02))

- Replace DomainEventHandler with DomainEventSubscriber
  ([`daf3ee1`](https://github.com/adriamontoto/domain-event-pattern/commit/daf3ee14e39aa0f881f04196f43cf95e4552c593))


## v0.6.0 (2025-09-13)

### ✨ Features

- Implement aggregate_identifier property in DomainEvent
  ([`9500ef5`](https://github.com/adriamontoto/domain-event-pattern/commit/9500ef5542b7d01601a1e2e2f87b34db112e823f))

- Implement logging for failed event handler retries in RetryEventBus
  ([`1296c74`](https://github.com/adriamontoto/domain-event-pattern/commit/1296c74d887f260fb5d9c2a0e637580a1ef81423))


## v0.5.0 (2025-09-12)

### ✨ Features

- Implement retry event bus and generic package errors
  ([`2da1387`](https://github.com/adriamontoto/domain-event-pattern/commit/2da1387934a82782ca52bc7a4ddfd2a0d972011c))


## v0.4.0 (2025-09-12)

### ✨ Features

- Implement deferred event bus
  ([`0cc6dc3`](https://github.com/adriamontoto/domain-event-pattern/commit/0cc6dc3db26e4309eb67154f2e6e0897552386df))


## v0.1.0 (2025-09-11)

### ✨ Features

- Implement domain event model, its value objects and tests
  ([`df20336`](https://github.com/adriamontoto/domain-event-pattern/commit/df2033672eab66916d6fb9e45582a5489f9d1485))

- Project setup
  ([`5b3e77c`](https://github.com/adriamontoto/domain-event-pattern/commit/5b3e77caccefe844ca0586fc88d7910c4723c37b))
