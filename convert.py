import fitz

def conv_header(page):
    # set ROI for the header
    page.set_cropbox(fitz.Rect(0, 0, 841, 101)) # set a cropbox for the page
    header_text = page.get_text()
    header_text_list = header_text.split("\n")
    
    grade_num = header_text_list[24]
    class_num = header_text_list[25]
    school_name = header_text_list[12]
    student_num = header_text_list[26]
    korean_test_takers_num = header_text_list[13] + ' ' + header_text_list[14]
    math_test_takers_num = header_text_list[15] + ' ' + header_text_list[16]
    english_test_takers_num = header_text_list[17] + ' ' + header_text_list[18]
    kor_history_test_takers_num = header_text_list[19] + ' ' + header_text_list[20]
    research_test_takers_num = header_text_list[21] + ' ' + header_text_list[22]
    date = header_text_list[23]

    header_text_list = [
        grade_num,
        class_num,
        school_name,
        student_num,
        korean_test_takers_num,
        math_test_takers_num,
        english_test_takers_num,
        kor_history_test_takers_num,
        research_test_takers_num,
        date
        ]

    return header_text_list

def conv_content(page):
    # set ROI for the content
    page.set_cropbox(fitz.Rect(0, 145, 98, 433)) # set a cropbox for the page
    content_text = page.get_text()
    content_text_list = content_text.split("\n")
    
    student_score_list = []

    for i in range(int((len(content_text_list)-1)/2)):
        student_score_sub_list = [content_text_list[i], content_text_list[i+8]]
        student_score_list.append(student_score_sub_list)

    page.set_cropbox(fitz.Rect(97, 145, 841, 433)) # set a cropbox for the page
    content_text = page.get_text()
    content_text_list = content_text.split("\n")

    for i in range(int((len(content_text_list)-1)/22)):
        student_score_list[i].append(content_text_list[i*22:i*22+22])

    return student_score_list

def conv_footer(page):
    # set ROI for the footer
    page.set_cropbox(fitz.Rect(0, 433, 841, 500)) # set a cropbox for the page
    footer_text = page.get_text()
    footer_text_list = footer_text.split("\n")
    
    class_avg_kor = footer_text_list[4]
    class_avg_math = footer_text_list[5]
    class_avg_research = footer_text_list[6]

    school_avg_kor = footer_text_list[8]
    school_avg_math = footer_text_list[9]
    school_avg_research = footer_text_list[10]
    
    nw_avg_kor = footer_text_list[12]
    nw_avg_math = footer_text_list[13]
    nw_avg_research = footer_text_list[14]

    footer_text_list = [
        class_avg_kor,
        class_avg_math,
        class_avg_research,
        school_avg_kor,
        school_avg_math,
        school_avg_research,
        nw_avg_kor,
        nw_avg_math,
        nw_avg_research
    ]

    return footer_text_list