# AurumIQ Next.js frontend.
#
# Sprint 0 skeleton: installs the locked workspace dependencies. The Next.js
# build and server entrypoint arrive in the sprint that scaffolds apps/web.

FROM node:24-alpine

ENV PNPM_HOME="/pnpm" \
    PATH="/pnpm:$PATH"

RUN corepack enable

WORKDIR /srv

COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY apps/web/package.json ./apps/web/
COPY packages/contracts/package.json ./packages/contracts/
RUN pnpm install --frozen-lockfile

COPY . .

USER node

EXPOSE 3000

CMD ["node", "-e", "console.log('AurumIQ web image built. Next.js entrypoint arrives in a later sprint.')"]
