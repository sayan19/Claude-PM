from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class NotifyResult:
    success: bool
    detail: str = ""
    dry_run: bool = False
    payload: Any = None


class Notifier(ABC):
    @abstractmethod
    def send(self, *args, **kwargs) -> NotifyResult: ...

    @abstractmethod
    def ping(self) -> bool: ...


__all__ = ["Notifier", "NotifyResult"]
