# Import all the modules

## The public libraries
import os, sys, math

## The local libraries

## The typo generator
from ok.generator import addDash
from ok.generator import addDynamicDns
from ok.generator import addition
from ok.generator import addTld
from ok.generator import changeDotDash
from ok.generator import changeOrder
from ok.generator import commonMisspelling
from ok.generator import doubleReplacement
from ok.generator import homoglyph
from ok.generator import homophones
from ok.generator import missingDot
from ok.generator import numeralSwap
from ok.generator import omission
from ok.generator import repetition
from ok.generator import replacement
from ok.generator import singularPluralize
from ok.generator import stripDash
from ok.generator import subdomain
from ok.generator import vowelSwap
from ok.generator import wrongTld
from ok.generator import wrongSld

## The format function
from ok.format.output import formatOutput

from ok.generator.omission import omission
from ok.generator.addDash import addDash
from ok.generator.addDynamicDns import addDynamicDns
from ok.generator.addition import addition
from ok.generator.addTld import addTld
from ok.generator.changeDotDash import changeDotDash
from ok.generator.changeOrder import changeOrder
from ok.generator.commonMisspelling import commonMisspelling
from ok.generator.doubleReplacement import doubleReplacement
from ok.generator.homoglyph import homoglyph
from ok.generator.homophones import homophones
from ok.generator.missingDot import missingDot
from ok.generator.numeralSwap import numeralSwap
from ok.generator.omission import omission
from ok.generator.repetition import repetition
from ok.generator.replacement import replacement
from ok.generator.singularPluralize import singularPluralize
from ok.generator.stripDash import stripDash
from ok.generator.subdomain import subdomain
from ok.generator.vowelSwap import vowelSwap
from ok.generator.wrongSld import wrongSld
from ok.generator.wrongTld import wrongTld

## The dns resolving function
from ok.dns_local.resolving import dnsResolving # named "dns_local" to avoid conflict with the dns library

## The utils
from ok.utils.parser import getArguments
from ok.generator.utils.get_pathetc import get_path_etc
sys.path.append(get_path_etc())


# Here are stored all the constants used in the project
# The constants are stored in a separate file to make it easier to change them

SIMILAR_CHAR = {
    '0': ['o'],
    '1': ['l', 'i', 'ı'],
    '2': ['ƻ'],
    '5': ['ƽ'],
    'a': ['à', 'á', 'à', 'â', 'ã', 'ä', 'å', 'ɑ', 'ạ', 'ǎ', 'ă', 'ȧ', 'ą', 'ə'],
    'b': ['d', 'ʙ', 'ɓ', 'ḃ', 'ḅ', 'ḇ', 'ƅ'],
    'c': ['e', 'ƈ', 'ċ', 'ć', 'ç', 'č', 'ĉ', 'ᴄ'],
    'd': ['b', 'cl', 'ɗ', 'đ', 'ď', 'ɖ', 'ḑ', 'ḋ', 'ḍ', 'ḏ', 'ḓ'],
    'e': ['c', 'é', 'è', 'ê', 'ë', 'ē', 'ĕ', 'ě', 'ė', 'ẹ', 'ę', 'ȩ', 'ɇ', 'ḛ'],
    'f': ['ƒ', 'ḟ'],
    'g': ['q', 'ɢ', 'ɡ', 'ġ', 'ğ', 'ǵ', 'ģ', 'ĝ', 'ǧ', 'ǥ'],
    'h': ['ĥ', 'ȟ', 'ħ', 'ɦ', 'ḧ', 'ḩ', 'ⱨ', 'ḣ', 'ḥ', 'ḫ', 'ẖ'],
    'i': ['1', 'l', 'í', 'ì', 'ï', 'ı', 'ɩ', 'ǐ', 'ĭ', 'ỉ', 'ị', 'ɨ', 'ȋ', 'ī', 'ɪ'],
    'j': ['ʝ', 'ǰ', 'ɉ', 'ĵ'],
    'k': ['lc', 'ḳ', 'ḵ', 'ⱪ', 'ķ', 'ᴋ'],
    'l': ['1', 'i', 'ɫ', 'ł', 'ı', 'ɩ'],
    'm': ['n', 'nn', 'rn', 'rr', 'ṁ', 'ṃ', 'ᴍ', 'ɱ', 'ḿ'],
    'n': ['m', 'r', 'ń', 'ṅ', 'ṇ', 'ṉ', 'ñ', 'ņ', 'ǹ', 'ň', 'ꞑ'],
    'o': ['0', 'ȯ', 'ọ', 'ỏ', 'ơ', 'ó', 'ö', 'ᴏ'],
    'p': ['ƿ', 'ƥ', 'ṕ', 'ṗ'],
    'q': ['g', 'ʠ'],
    'r': ['ʀ', 'ɼ', 'ɽ', 'ŕ', 'ŗ', 'ř', 'ɍ', 'ɾ', 'ȓ', 'ȑ', 'ṙ', 'ṛ', 'ṟ'],
    's': ['ʂ', 'ś', 'ṣ', 'ṡ', 'ș', 'ŝ', 'š', 'ꜱ'],
    't': ['ţ', 'ŧ', 'ṫ', 'ṭ', 'ț', 'ƫ'],
    'u': ['ᴜ', 'ǔ', 'ŭ', 'ü', 'ʉ', 'ù', 'ú', 'û', 'ũ', 'ū', 'ų', 'ư', 'ů', 'ű', 'ȕ', 'ȗ', 'ụ'],
    'v': ['ṿ', 'ⱱ', 'ᶌ', 'ṽ', 'ⱴ', 'ᴠ'],
    'w': ['vv', 'ŵ', 'ẁ', 'ẃ', 'ẅ', 'ⱳ', 'ẇ', 'ẉ', 'ẘ', 'ᴡ'],
    'x': ['ẋ', 'ẍ'],
    'y': ['ʏ', 'ý', 'ÿ', 'ŷ', 'ƴ', 'ȳ', 'ɏ', 'ỿ', 'ẏ', 'ỵ'],
    'z': ['ʐ', 'ż', 'ź', 'ᴢ', 'ƶ', 'ẓ', 'ẕ', 'ⱬ']
}

NUMERAL = [
    ["0", "zero"],
    ["1", "one", "first"],
    ["2", "two", "second"],
    ["3", "three", "third"],
    ["4", "four", "fourth", "for"],
    ["5", "five", "fifth"],
    ["6", "six", "sixth"],
    ["7", "seven", "seventh"],
    ["8", "eight", "eighth"],
    ["9", "nine", "ninth"]
]

ALGO_NAME_LIST = [
    "omission", "repetition", "changeOrder", "replacement", "doubleReplacement", 
    "addition", "missingDot", "stripDash", "vowelSwap", "addDash", "homoglyph", 
    "commonMisspelling", "homophones", "wrongTld", "addTld", "subdomain", 
    "singularPluralize", "changeDotDash", "wrongSld", "numeralSwap", "addDynamicDns"
]

EXCLUDED_TLD = ["gov.pl"] # why not ?


# Getters for constants
def const_get_similar_chars():
    """
    Return the dictionary of similar characters
    """
    return SIMILAR_CHAR

def const_get_numeral():
    """
    Return the list of numeral
    """
    return NUMERAL

def const_get_algo_name_list():
    """
    Return the list of algorithm names
    """
    return ALGO_NAME_LIST

def const_get_excluded_tld():
    """
    Return the list of excluded TLD
    """
    return EXCLUDED_TLD

# Import all the constants of data from the file const/main.py
# If you wanna add a new algorithm, you have to add it in the list algo_list
numerals = const_get_numeral()
algo_list = const_get_algo_name_list()


## [START] Final treatment

def runAll(domain, limit, formatoutput, pathOutput, verbose=False, givevariations=False, keeporiginal=False, all_homoglyph=False):
    """Run all algo on each domain contain in domainList"""

    resultList = list()
    print(algo_list)
    for algo in algo_list:
        if algo == "omission":
            resultList = omission(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "addDash":
            resultList = addDash(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "addDynamicDns":
            resultList = addDynamicDns(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "numeralSwap":
            resultList = numeralSwap(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "wrongSld":
            resultList = wrongSld(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "changeDotDash":
            resultList = changeDotDash(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "singularPluralize":
            resultList = singularPluralize(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "subdomain":
            resultList = subdomain(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "addTld":
            resultList = addTld(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "wrongTld":
            resultList = wrongTld(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "homophones":
            resultList = homophones(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "commonMisspelling":
            resultList = commonMisspelling(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "homoglyph":
            resultList = homoglyph(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "vowelSwap":
            resultList = vowelSwap(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "stripDash":
            resultList = stripDash(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "missingDot":
            resultList = missingDot(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "addition":
            resultList = addition(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "doubleReplacement":
            resultList = doubleReplacement(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "replacement":
            resultList = replacement(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "changeOrder":
            resultList = changeOrder(domain, resultList, verbose, limit, givevariations, keeporiginal)
        if algo == "repetition":
            resultList = repetition(domain, resultList, verbose, limit, givevariations, keeporiginal)
    if verbose:
        print(f"Total: {len(resultList)}")

    formatOutput(formatoutput, resultList, domain, pathOutput, givevariations)

    return resultList

## [END] Final treatment

# Main file function
if __name__ == "__main__":

    # Step 1: Get the arguments
    parser = getArguments()
    args = parser.parse_args()

    resultList = list()

    # Step 2: Assign some variables
    verbose = args.v
    givevariations = args.givevariations
    dns_limited = args.dnslimited
    keeporiginal = args.keeporiginal

    limit = math.inf
    if args.limit: # If the user has specified a limit
        limit = int(args.limit)

    pathOutput = args.output

    if pathOutput and not pathOutput == "-":
        try:
            os.makedirs(pathOutput)
        except:
            pass # If the directory already exist

    # Step 3: Check the format output
    if args.formatoutput:
        if args.formatoutput == "text" or args.formatoutput == "yara" or args.formatoutput == "yaml" or args.formatoutput == "regex":
            formatoutput = args.formatoutput
        else:
            print("[-] Format type error")
            exit(-1)
    else:
        formatoutput = "text" # Default format

    # Verify that a domain name is receive
    if args.domainName:
        domainList = args.domainName
    elif args.filedomainName:
        with open(args.filedomainName, "r") as read_file:
            domainList = read_file.readlines()
    else:
        print("[-] No Entry")
        exit(-1)

    # Step 4: Check the domain name
    for domain in domainList:
        if domain[0] == '.':
            domain = domain[1:]
        if pathOutput:
            print(f"\n\t[*****] {domain} [*****]")

        # Go to the dedicated function
        if args.combo:
            base_result = list()
            for arg in vars(args):
                for algo in algo_list:
                    if algo.lower() == arg:
                        if getattr(args, arg):
                            if verbose:
                                print(f"[+] {algo}")

                            func = globals()[algo]
                            # First Iteration
                            if not base_result:
                                if algo == "homoglyph":
                                    base_result = func(domain, resultList, False, limit, givevariations, keeporiginal, all=args.all_homoglyph)
                                else:
                                    base_result = func(domain, resultList, False, limit, givevariations, keeporiginal)
                                resultList = base_result.copy()
                                
                                if verbose:
                                    print(f"{len(resultList)}\n")
                            else:
                                loc_result = list()
                                loc_result = base_result.copy()
                                for r in loc_result:
                                    if type(r) == list:
                                        r = r[0]

                                    if algo == "homoglyph":
                                        loc_result = func(r, loc_result, False, limit, givevariations, keeporiginal, all=args.all_homoglyph, combo=True)
                                    else:
                                        loc_result = func(r, loc_result, False, limit, givevariations, keeporiginal, True)
                                resultList = resultList + loc_result
                                base_result = loc_result

                                if verbose:
                                    print(f"{len(loc_result)}\n")                                 
        elif args.all:
            for algo in algo_list:
                func = globals()[algo]
                if algo == "homoglyph":
                    resultList = func(domain, resultList, verbose, limit, givevariations, keeporiginal, all=args.all_homoglyph)
                else:
                    resultList = func(domain, resultList, verbose, limit, givevariations, keeporiginal)
        else:
            for arg in vars(args):
                for algo in algo_list:
                    if algo.lower() == arg:
                        if getattr(args, arg):
                            func = globals()[algo]
                            if algo == "homoglyph":
                                resultList = func(domain, resultList, verbose, limit, givevariations, keeporiginal, all=args.all_homoglyph)
                            else:
                                resultList = func(domain, resultList, verbose, limit, givevariations, keeporiginal)

        # Step 5: Final treatment
        if verbose:
            print(f"Total: {len(resultList)}")

        formatOutput(formatoutput, resultList, domain, pathOutput, givevariations, args.betterregex)
        
        # Step 6: DNS resolving for each domain name
        if args.dnsresolving:
            dnsResolving(resultList, domain, pathOutput, verbose, givevariations, dns_limited, args.catchall)

        resultList = list()
