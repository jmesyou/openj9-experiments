#!/usr/bin/python3

import subprocess

OPT_LEVELS = [
    "cold",
    "warm",
    "hot",
    "veryHot",
    "scorching"
]

OPT_OPTIONS = [
    "AutoSIMD",
    "BasicBlockExtension",
    "BasicBlockPeephole",
    "BlockVersioner",
    "BlockSplitter",
    "CFGSimplification",
    "CompactLocals",
    "CompactNullChecks",
    "DeadTreeElimination",
    "EscapeAnalysis",
    "GlobalCopyPropagation",
    "GlobalDSE",
    "GlobalVP",
    "GLU",
    "Inlining",
    "IPA",
    "LocalCSE",
    "LocalDSE",
    "LocalVP",
    "LocalReordering",
    "LoopCanonicalization",
    "LoopUnroller",
    "OSR",
    "PartialInlining",
    "Peephole",
    "PRBE",
    "PRE",
    "SequenceSimplification"
    "StoreSinking",
    "SwitchAnalyzer",
    "TailRecursion",
    "TreeCleansing",
   #  "TreeSimplification",
    "VirtualInlining",
    "VirtualGuardTailSplitter",
]


def run_renaissance():
    process = subprocess.run(["java", "-jar", "bin/renaissance.jar", "--raw-list"], capture_output=True)
    process.check_returncode()

    benchmarks = process.stdout.decode().splitlines()

    for benchmark in benchmarks:
        for opt in [None] + OPT_OPTIONS:
            jvm_opts = ["-jar"]
            if opt is not None:
                jvm_opts.append("-Xjit:disable{opt}".format(opt=opt))
            file_name = "data/renaissance/renaissance_{benchmark}_disable{opt}.csv".format(benchmark=benchmark, opt=opt)
            benchmark_opts = ["--csv", file_name, benchmark]
            subprocess.run(["java"] + jvm_opts + ["bin/renaissance.jar"] + benchmark_opts)

if __name__ == "__main__":
    run_renaissance()
