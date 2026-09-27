def judge(question, expects, answer, results)-> bool:
    """ 
    q: 'give', expect: 'give'
    the expect is in the answer
    """
    return (retrieval_hits(expects, results) and has_source(answer, results))


def retrieval_hits(expects, results)-> bool:
    """
    any part of my expect in the results

    did i retrieve the correct chunks
    """
    return any(expects.lower().strip() in chunk.text.lower().strip() for chunk in results)


def has_source(answer, results)-> bool:
    """ 
    checks if each answer comes with a source
    """
    return any(r.source.lower() in answer.lower() for r in results)



# more specific criteria checks

def top_retrieval(expects, results)-> bool:
    """
    confirms the top chunk contains answer
    """
    if not results:
        return False
    return expects.lower().strip() in results[0].text.lower()



def source_contains_relevant_info(expects, answer, results)-> bool:
    """
    confirms that each source that is cited contains relevant info
    to the question
    """
    cited = {r.source for r in results if r.source.lower() in answer.lower()}
    if not cited:
        return False
    return all(
        any(expects.lower().strip() in r.text.lower() for r in results if r.source == source)
        for source in cited
    )


def classify_out_of_scope(answer)-> bool:
    """
    confirms that out of scope questions are flagged appropriately
    """
    from gate import REFUSAL

    return REFUSAL.lower() in answer.lower()