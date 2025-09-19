##Tester version 2.2
import more_math
import pytest
import random
import assessMeTester_StringSimilarity
#TO RUN pytest --tb=short -s

def fact_test(test_value, expected_output,capsys, monkeypatch,printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "fact_testing"
        functionName = "fact"
          
        try:

            # invoke
            #inputs = iter(['John'])
            #expected_output = outputValue
            #monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            # Execute the function
            # invoke
          
            # invoke 
            result = more_math.fact(test_value)

            
            if result==None:
                 success=False
                 assertMessage="The function must return a value!"
                 raise
             
            # Part for string comparison!
            if result==expected_output:
                assert True
            else:
                success = False
                assertMessage=f"The {functionName} is not correct!\nExpected:{expected_output}"
                assertMessage+=f"\nReturned:{result}"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage


def test_fact_1(capsys, monkeypatch, printFeedback=True):
     test_value = 9
     expected_output = 362880

     fact_test(test_value,expected_output,capsys, monkeypatch,printFeedback)   


def test_fact_2(capsys, monkeypatch, printFeedback=True):
     test_value = -5
     expected_output = 0

     fact_test(test_value,expected_output,capsys, monkeypatch,printFeedback)   




def root_test(test_value, expected_output,capsys, monkeypatch,printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "root_testing"
        functionName = "root"
          
        try:

            # invoke
            #inputs = iter(['John'])
            #expected_output = outputValue
            #monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            # Execute the function
            # invoke
          
            # invoke 
            result = more_math.root(test_value)

            
            if result==None:
                 success=False
                 assertMessage="The function must return a value!"
                 raise
             
            # Part for string comparison!
            if result==expected_output:
                assert True
            else:
                success = False
                assertMessage=f"The {functionName} is not correct!\nExpected:{expected_output}"
                assertMessage+=f"\nReturned:{result}"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage


def test_root_1(capsys, monkeypatch, printFeedback=True):
    test_value = 64
    expected_value = 8
    root_test(test_value,expected_value,capsys, monkeypatch,printFeedback)   


def test_root_2(capsys, monkeypatch, printFeedback=True):
    test_value = -1
    expected_value = 0
    root_test(test_value,expected_value,capsys, monkeypatch,printFeedback)   
 




def trunk_test(test_value, expected_output,capsys, monkeypatch,printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "trunk_testing"
        functionName = "trunk"
          
        try:

            # invoke
            #inputs = iter(['John'])
            #expected_output = outputValue
            #monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            # Execute the function
            # invoke
          
            # invoke 
            result = more_math.trunk(test_value)

            
            if result==None:
                 success=False
                 assertMessage="The function must return a value!"
                 raise
             
            # Part for string comparison!
            if result==expected_output:
                assert True
            else:
                success = False
                assertMessage=f"The {functionName} is not correct!\nExpected:{expected_output}"
                assertMessage+=f"\nReturned:{result}"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage


def test_trunk(capsys, monkeypatch, printFeedback=True):
    test_value = 1234.5677
    expected_value = 1234
    trunk_test(test_value,expected_value,capsys, monkeypatch,printFeedback)   




def main_test(capsys, monkeypatch,printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "main_testing"
        functionName = "main"
          
        try:

            # invoke
            inputs = iter([10, 9, 10.5])
            expected_output = """10 factorial = 3628800
The square root of 9.0 = 3.0
10.5 truncated = 10"""

            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            # Execute the function
            random.seed(5)
            result = more_math.main();
            #Get the feedback
            captured = capsys.readouterr()
            
            # Check if the expected output is in the captured stdout
            result =  captured.out

            
            if result==None:
                 success=False
                 assertMessage="The function must return a value!"
                 raise
             
            # Part for string comparison!
            if result.replace("\n", "") == expected_output.replace("\n", ""):
                assert True
            else:
                success = False
                assertMessage=f"The {functionName} is not correct!\nExpected:{expected_output}"
                assertMessage+=f"\nReturned:{result}"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage

def test_main(capsys, monkeypatch, printFeedback=True):
     main_test(capsys, monkeypatch,printFeedback) 


def test_FinalGrade(capsys, monkeypatch):
    
    totalPoints = 0

    ## CALL the testers, do not print, otherwise you will mess with some of the testers
  
    test_functions = [
        (test_fact_1,15),
        (test_fact_2,15),
        (test_root_1,15),
        (test_root_2,15),
        (test_trunk,15),
        (test_main,25)
    ]

    outputFeedbac = "############ TOTAL POINTS ###################\n"
    
    for function, point in test_functions:
        try:
            function(capsys,monkeypatch,False)
            outputFeedbac=outputFeedbac+f"PASS:{function.__name__}: {point}"+"\n"
            totalPoints += point
        except AssertionError:
            outputFeedbac=outputFeedbac+f"FAIL:{function.__name__}: {0}\n"
        
    
    print(outputFeedbac)
    print("Total points",totalPoints)
    
   # Define emoji ranges based on points
    if 90 <= totalPoints <= 100:
          emoji = "🌟✨💫💖😍🎉👏😎🥇🚀👏👏👏👏👏👏"
    elif 80 <= totalPoints < 90:
          emoji = "😃👍👌🙌🤗🥳😁👌👌👌👌"
    elif 70 <= totalPoints < 80:
          emoji = "😊😉❤️🌸🌼💝💓👌👌"
    elif 60 <= totalPoints < 70:
          emoji = "😐🤔😕😬😟😞"  # Thinking + Unamused + Disappointed
    else:
          emoji = "😢😥😭😩😖"
    print(emoji)
    assert True


