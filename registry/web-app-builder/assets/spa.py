"""Starlette static files with a conservative browser-history SPA fallback.

Copy into the generated app and mount after API routes. Configure reserved prefixes
for any additional backend route families owned by the application.
"""
from pathlib import PurePosixPath

from starlette.datastructures import Headers
from starlette.exceptions import HTTPException
from starlette.staticfiles import StaticFiles


class SPAStaticFiles(StaticFiles):
    def __init__(self, *args, reserved=("api", "webhook", "webhooks", "health", "assets"), **kwargs):
        super().__init__(*args, **kwargs)
        self.reserved = frozenset(reserved)

    def navigation(self, path, scope):
        parts = PurePosixPath(path).parts
        return (
            scope["method"] in {"GET", "HEAD"}
            and "text/html" in Headers(scope=scope).get("accept", "").lower()
            and (not parts or parts[0] not in self.reserved)
            and not PurePosixPath(path).suffix
            and ".." not in parts
        )

    async def get_response(self, path, scope):
        try:
            response = await super().get_response(path, scope)
        except HTTPException as error:
            if error.status_code != 404 or not self.navigation(path, scope):
                raise
        else:
            if response.status_code != 404 or not self.navigation(path, scope):
                return response
        return await super().get_response("index.html", scope)
