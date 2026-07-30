import { spawn } from 'node:child_process';

const npmCommand = process.platform === 'win32' ? 'npm.cmd' : 'npm';

const commands = [
  ['Backend', ['--workspace', 'Backend', 'run', 'dev']],
  ['Frontend', ['--workspace', 'Frontend', 'run', 'dev']],
];

const children = commands.map(([name, args]) => {
  const child = spawn(npmCommand, args, {
    cwd: process.cwd(),
    stdio: 'inherit',
    shell: false,
  });

  child.on('exit', (code) => {
    if (code && code !== 0) {
      console.error(`${name} stopped with exit code ${code}`);
    }
  });

  return child;
});

const stopChildren = () => {
  for (const child of children) {
    if (!child.killed) {
      child.kill();
    }
  }
};

process.on('SIGINT', () => {
  stopChildren();
  process.exit(0);
});

process.on('SIGTERM', () => {
  stopChildren();
  process.exit(0);
});
