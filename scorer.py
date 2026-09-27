def judge(question, expects, answer, results)-> bool:
    """ 
    q: 'give', expect: 'give'
    the expect is in the answer
    """
    return expects.lower().strip() in (answer.lower())


"""
LLM as judge
rapidfuzz (library)

0 libraries open == no libraries open
"""

def retriveal_hits(expects, results)-> bool:
    """ 
    any part of my expect in the results

    did i retrieve the correct chunks
    """
    return any(expects.lower().strip() for chunk in results)


def top_retrieval(expects, results)-> bool:
    """ 
    confirms the top chunk contains answer
    """
    pass


def has_source(answer)-> bool:
    """ 
    checks if each answer comes with a source
    """
    pass


def source_contains_relevant_info(expects, answer, results)-> bool:
    """ 
    confirms that each source that is cited contains relevant info 
    to the question
    """
    pass


def classify_out_of_scope(answer)-> bool:
    """ 
    confirms that out of scope questions are flagged appropriately
    """
    pass