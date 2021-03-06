#!/usr/bin/env julia
println("including ntuple.jl on pid=", myid())
include("kinematics.jl")

module Analysis

using Kinematics, HEP, Histograms, ROOT, ROOTDataFrames, ROOTHistograms, DataFrames

const LUMI = 10000.0

function process_sl!(results, ev, prefix, syst)
    if ev.numJets == 4
        if ev.nBCSVM == 2
            fill_histograms_sl!(results, ev, (prefix, :sl_j4_t2, ), syst)
        elseif ev.nBCSVM == 3
            fill_histograms_sl!(results, ev, (prefix, :sl_j4_t3, ), syst)
        end
    elseif ev.numJets == 5
        if ev.nBCSVM == 2
            fill_histograms_sl!(results, ev, (prefix, :sl_j5_t2, ), syst)
        elseif ev.nBCSVM == 3
            fill_histograms_sl!(results, ev, (prefix, :sl_j5_t3, ), syst)
        elseif ev.nBCSVM >= 4
            fill_histograms_sl!(results, ev, (prefix, :sl_j5_tge4, ), syst)
        end
    elseif ev.numJets >= 6
        if ev.nBCSVM == 2
            fill_histograms_sl!(results, ev, (prefix, :sl_jge6_t2, ), syst)
        elseif ev.nBCSVM == 3
            fill_histograms_sl!(results, ev, (prefix, :sl_jge6_t3, ), syst)
        elseif ev.nBCSVM >= 4
            fill_histograms_sl!(results, ev, (prefix, :sl_jge6_tge4, ), syst)
        end
    end
end

function process_dl!(results, ev, prefix, syst)
    if ev.numJets >= 3
        if ev.nBCSVM == 2 && ev.numJets == 3
            fill_histograms_dl!(results, ev, (prefix, :dl_j3_t2, ), syst)
        elseif ev.nBCSVM == 3
            fill_histograms_dl!(results, ev, (prefix, :dl_jge3_t3, ), syst)
        elseif ev.nBCSVM == 2 && ev.numJets >= 4
            fill_histograms_dl!(results, ev, (prefix, :dl_jge4_t2, ), syst)
        elseif ev.nBCSVM >= 4 && ev.numJets >= 4
            fill_histograms_dl!(results, ev, (prefix, :dl_jge4_tge4, ), syst)
        end
    end
end

function process_event!(results, ev, prefix, syst)
    if ev.is_sl
        process_sl!(results, ev, prefix, syst)
    elseif ev.is_dl
        process_dl!(results, ev, prefix, syst)
    end
end

function make_results(prefix, syst)

    jet_pt_bins = [-Inf, linspace(0, 500, 100)..., Inf]
    mem_bins = [-Inf, linspace(0, 1, 7)..., Inf]
    btag_lr_logit_bins = [-Inf, linspace(-20, 20, 40)..., Inf]

    results = Dict{Any, ErrorHistogram}()
    for k in [:sl_j4_t2, :sl_j4_t3, :sl_j5_t2, :sl_j5_t3, :sl_j5_tge4, :sl_jge6_t2, :sl_jge6_t3, :sl_jge6_tge4]
        results[tuple(prefix, k, :jet0_pt, syst)] = ErrorHistogram(jet_pt_bins)
        results[tuple(prefix, k, :mem_SL_0w2h2t, syst)] = ErrorHistogram(mem_bins)
        #results[tuple(prefix, k, :mem_SL_2w2h2t, syst)] = ErrorHistogram(mem_bins)
        #results[tuple(prefix, k, :mem_SL_0w2h2t_sj, syst)] = ErrorHistogram(mem_bins)
        #results[tuple(prefix, k, :mem_SL_2w2h2t_sj, syst)] = ErrorHistogram(mem_bins)
        results[tuple(prefix, k, :btag_LR_4b_2b_logit, syst)] = ErrorHistogram(btag_lr_logit_bins)
        for b in [:blr095]
            results[tuple(prefix, k, b, :jet0_pt, syst)] = ErrorHistogram(jet_pt_bins)
            results[tuple(prefix, k, b, :mem_SL_0w2h2t, syst)] = ErrorHistogram(mem_bins)
            #results[tuple(prefix, k, :mem_SL_2w2h2t, syst)] = ErrorHistogram(mem_bins)
            #results[tuple(prefix, k, :mem_SL_0w2h2t_sj, syst)] = ErrorHistogram(mem_bins)
            #results[tuple(prefix, k, :mem_SL_2w2h2t_sj, syst)] = ErrorHistogram(mem_bins)
            results[tuple(prefix, k, b, :btag_LR_4b_2b_logit, syst)] = ErrorHistogram(btag_lr_logit_bins)
        end
    end
    for k in [:dl_j3_t2, :dl_jge3_t3, :dl_jge4_t2, :dl_jge4_tge4]
        results[tuple(prefix, k, :jet0_pt, syst)] = ErrorHistogram(jet_pt_bins)
        results[tuple(prefix, k, :mem_DL_0w2h2t, syst)] = ErrorHistogram(mem_bins)
        results[tuple(prefix, k, :btag_LR_4b_2b_logit, syst)] = ErrorHistogram(btag_lr_logit_bins)
        for b in [:blr095]
            results[tuple(prefix, k, b, :jet0_pt, syst)] = ErrorHistogram(jet_pt_bins)
            results[tuple(prefix, k, b, :mem_DL_0w2h2t, syst)] = ErrorHistogram(mem_bins)
            results[tuple(prefix, k, b, :btag_LR_4b_2b_logit, syst)] = ErrorHistogram(btag_lr_logit_bins)
        end
    end
    return results
end

function fill_histograms_1!(results, ev, key, syst)
    push!(
        results[tuple(key..., :jet0_pt, syst)],
        pt(ev.jets[1]),
        weight(ev, LUMI)
    )
    push!(
        results[tuple(key..., :btag_LR_4b_2b_logit, syst)],
        ev.btag_LR_4b_2b_logit,
        weight(ev, LUMI)
    )
end

function fill_histograms_dl!(results, ev, key, syst)
    fill_histograms_1!(results, ev, key, syst)

    push!(
        results[tuple(key..., :mem_DL_0w2h2t, syst)],
        mem_p(ev, 2, 0.02),
        weight(ev, LUMI)
    )
    if ev.btag_LR_4b_2b > 0.95
        fill_histograms_1!(results, ev, tuple(key..., :blr095), syst)
        push!(
            results[tuple(key..., :blr095, :mem_DL_0w2h2t, syst)],
            mem_p(ev, 2, 0.02),
            weight(ev, LUMI)
        )
    end
end

function fill_histograms_sl!(results, ev, key, syst)
    fill_histograms_1!(results, ev, key, syst)
    push!(
        results[tuple(key..., :mem_SL_0w2h2t, syst)],
        mem_p(ev, 1, 0.02),
        weight(ev, LUMI)
    )
    if ev.btag_LR_4b_2b > 0.95
        fill_histograms_1!(results, ev, tuple(key..., :blr095), syst)
        push!(
            results[tuple(key..., :blr095, :mem_SL_0w2h2t, syst)],
            mem_p(ev, 1, 0.02),
            weight(ev, LUMI)
        )
    end
end

const ResultDict = Dict{Any, ErrorHistogram}
function process_sample(fn, prefix;range=nothing, do_cache=true, nprint=0, systematics=[:nominal])
    #println("processing $fn")
    isfile(fn) || error("file not found: $fn")
    df = TreeDataFrame([fn]; treename="tree")
    if range == nothing
        range = 1:length(df)
    end
    results = ResultDict()
    for syst in systematics
        results += make_results(prefix, syst)
    end

    if do_cache
        SetCacheSize(df.tt, 0)
        SetCacheSize(df.tt, 16 * 1024 * 1024)
        brs = ["jets_*", "njets", "is_*", "numJets*", "nBCSVM*", "weight_xs", "genWeight", "mem_tt*", "btag_LR*"]
        enable_branches(df, brs)
        for b in brs
            AddBranchToCache(df.tt, b)
        end
    end #do_cache

    const t0 = time()
    #for i=1:nrow(df)

    ntot = 0
    nloaded = 0

    fail_lep = 0
    idx1 = 1
    idx2 = 1
    #println("looping $range")
    for idx1 in range

        #idx1%10000==0 && println("ev=$idx1 dt(10k)=", Int64(round(idx1/(time()-t0))))

        #Load the TTree row
        nloaded += load_row(df, idx1)
        if idx1<=nprint
            println("---")
            println("read event")
        end

        df.row.numJets() >= 3 || continue
        df.row.nBCSVM() >= 1 || continue

        #const ev_JESUp = parse_event(df, Val{:JESUp})
        #const ev_JESDown = parse_event(df, Val{:JESDown})
        const evd = Dict{Symbol, Event}()
        for syst in systematics
            evd[syst] = parse_event(df, Val{syst})
        end

        if idx1<=nprint
            for (syst, ev) in evd
                println("syst=$syst ", string(ev))
            end
        end
        for (syst, ev) in evd
            process_event!(results, ev, prefix, syst)
        end

        ntot += 1
        idx2 += 1
    end
    const t1 = time()
    dt = t1 - t0
    nloaded = nloaded / 1024 / 1024
    const speed = length(range) / dt
    #println("processed $range total, $idx2 passed, $(round(speed, 0)) ev/s, $(round(nloaded/dt)) Mb/s")
    return results
end

#Define a way to add two result dictionaries together
import Base.+
function +(d1::Dict, d2::Dict)
    s1 = Set(keys(d1))
    s2 = Set(keys(d2))
    ret = Dict()

    #is common in both, add both
    for k in intersect(s1, s2)
        ret[k] = d1[k]+d2[k]
    end

    #is in d1 only
    for k in setdiff(s1, s2)
        ret[k] = d1[k]
    end

    #is in d2 only
    for k in setdiff(s2, s1)
        ret[k] = d2[k]
    end
    return ret
end

export process_sample
end #module Analysis
